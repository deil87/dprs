# Implementation of DPRS scoring 

from itertools import combinations
import numpy as np


def index_combinations(combinations):
    gt_dict = { f"{pair_l[0]}{pair_r[0]}" if pair_l[0] < pair_r[0] else f"{pair_r[0]}{pair_l[0]}":(pair_l,pair_r)  for pair_l, pair_r in combinations }
    return gt_dict

def get_combinations(rank_list, debug=False):
    print(list(rank_list)) if debug else {}
    gt_with_positions = zip(rank_list, range(len(rank_list)))
    gt_combinations = list(combinations(gt_with_positions, 2))
    print(gt_combinations) if debug else {}
    return gt_combinations

    
def dprs_compute(ground_truth, predicted_ranking, penalize_pair_distance_change=True, return_penalties=False, debug=False):

    l_size = len(ground_truth)
    assert l_size == len(predicted_ranking), "Input lists must be of the same size."

    total_penalty = 0
    all_penalties = []

    gt_combinations = get_combinations(ground_truth, debug)
    rp_combinations = get_combinations(predicted_ranking, debug)

    # Construct dicts
    gt_dict = index_combinations(gt_combinations)
    rp_dict = index_combinations(rp_combinations)
    
    weights_raw = np.array(list(range(1, l_size + 1))[::-1])
    wn = weights_raw / sum(weights_raw)
    print(wn) if debug else {}
    
    orig_pair_weakness_weights = np.array(list(range(1, l_size - 1 + 1))[::-1])
    opww = orig_pair_weakness_weights / sum(orig_pair_weakness_weights)
    print(opww) if debug else {}
    
    pair_rel_dist_weights = np.array(list(range(1, (l_size - 1)*2 + 1))) # note: no reversion here!
    prdw = pair_rel_dist_weights / sum(pair_rel_dist_weights)
    print(prdw) if debug else {}

    for gt_key, gt_pair in gt_dict.items():
        print(f"Ground truth: {gt_pair}") if debug else {}
        predicted_pair = rp_dict[gt_key]
        print(f"Predicted value: {predicted_pair}") if debug else {}    
        
        # order check: penalty for wrong order
        (gt_l, gt_li), (gt_r, gt_ri) = gt_pair
        (pr_l, pr_li), (pr_r, pr_ri) = predicted_pair
        wrong_order = False
        if gt_l != pr_l:
            wrong_order = True
            print(f"{gt_l} vs {pr_l}  wrong order") if debug else {}
            (pr_r, pr_ri), (pr_l, pr_li) = (pr_l, pr_li), (pr_r, pr_ri)
            predicted_pair = (pr_l, pr_li), (pr_r, pr_ri)    
            
        left_travel_penalty =  sum(wn[gt_li:pr_li]) if gt_li < pr_li else sum(wn[pr_li: gt_li])
        right_travel_penalty = sum(wn[gt_ri:pr_ri]) if gt_ri < pr_ri else sum(wn[pr_ri: gt_ri])
        penalty = left_travel_penalty + right_travel_penalty
        
        # Account for original strength of the pair ( less distance, more impact). both cases should be valid - getting closer or further away)
        orig_pair_distance = abs(gt_ri - gt_li)
        penalty *= opww[orig_pair_distance - 1]
        
        # Multiply by rel distance change ( not absolute but relative aspect) 
        predicted_pair_dist = pr_ri - pr_li
        pair_dist_rel_change = orig_pair_distance - predicted_pair_dist
        penalty *= prdw[pair_dist_rel_change - 1]

        print(f"Penalty: {penalty}") if debug else {}
        
        total_penalty += penalty
        all_penalties.append(penalty)
        
        print("="*25) if debug else {}
    
    # print(f"Total penalty: {total_penalty}")
    if return_penalties:
        return total_penalty, all_penalties
    else:
        return total_penalty