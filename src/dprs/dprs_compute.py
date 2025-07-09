# The simplest possible library function.
# Replace this file with your own fabulous code.

def dprs_compute(x, y):
    """Compute the sum of two numbers."""
    return x + y

from itertools import combinations

def index_combinations(combinations):
    gt_dict = { f"{pair_l[0]}{pair_r[0]}" if pair_l[0] < pair_r[0] else f"{pair_r[0]}{pair_l[0]}":(pair_l,pair_r)  for pair_l, pair_r in combinations }
    return gt_dict

def get_combinations(rank_list, debug=False):
    print(list(rank_list)) if debug else {}
    gt_with_positions = zip(rank_list, range(len(rank_list)))
    gt_combinations = list(combinations(gt_with_positions, 2))
    print(gt_combinations) if debug else {}
    return gt_combinations

    
def dprs_compute_real(ground_truth, predicted_ranking, penalize_pair_distance_change=True, debug=False):

    total_penalty = 0
    all_penalties = []

    gt_combinations = get_combinations(ground_truth, debug)
    rp_combinations = get_combinations(predicted_ranking, debug)

    # Construct dicts
    gt_dict = index_combinations(gt_combinations)
    rp_dict = index_combinations(rp_combinations)
    

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
            print(f"{gt_l} vs {pr_l}  penalize order") if debug else {}
            
        # distance changed: (9-6) - (1-0) = 2
        if penalize_pair_distance_change:
            distance_change = abs(abs(gt_li - gt_ri) - abs(pr_li - pr_ri))
        else:
            distance_change = 1
        print(f"distance_change: {distance_change}") if debug else {}
        
        # absolute location: 6 - 0 = 6
        importance_index = gt_li if gt_li < gt_ri else gt_ri
        importance_coef = len(ground_truth ) - importance_index
        print(f"importance coef.: {importance_coef}") if debug else {}
        
        penalty = (3 if wrong_order else 1) * (distance_change + 1) * importance_coef

        if gt_key in ["02", "09", "79", "07"]:
            print(f"Ground truth: {gt_pair} -> {predicted_pair}")
            print(f"{gt_key} penalty({penalty}) = (3 if wrong_order={wrong_order} else 1) * (distance_change={distance_change} + 1) * importance_coef={importance_coef}")
        #0,1,2     7,8,9
        #2,1,0     9,8,7
        
        #(0,2) -> (2,0) vs  (7,9) -> (9,7) vs (0,8) -> (8,0)
        
        
        print(f"Penalty: {penalty}") if debug else {}
        total_penalty += penalty
        all_penalties.append(penalty)
        print("="*25) if debug else {}
    
    # print(f"Total penalty: {total_penalty}")
    return total_penalty, all_penalties