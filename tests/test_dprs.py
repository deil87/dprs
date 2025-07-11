from dprs import dprs
import pytest

def test_two_same():
    """Test that is checking that score for same lists is zero."""
    lista = range(10)
    assert dprs(lista,lista) == 0
    
    
def test_rank_shift_direction():
    """
    Test checks that for a single ranking position it is important whether shift happens to the left or to the right. 
    For the sake of test travelling distance should be the same.
    Scores must be differet (bigger if shift is towards top of the ranking)
    """
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_shift_right = [0, 1, 2, 3, 4, 5, 6, 9, 8, 7]  # 7 <-> 9
    list_shift_left = [0, 1, 2, 3, 4, 7, 6, 5, 8, 9]   # 7 <-> 5

    assert dprs(lista,list_shift_right) < dprs(lista,list_shift_left)
    
    

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (0, 0, 0),
])
def test_add(a, b, expected):
    """Test add function with various inputs."""
    assert a <= b
    
#0,1,2     7,8,9
#2,1,0     9,8,7
#(0,2) -> (2,0) vs  (7,9) -> (9,7) vs (0,8) -> (8,0)


def test_monotonic_discount():
    """
    Test checks that similar swaps lead to a different scores depending on the location
    """
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_shift_right = [0, 1, 2, 3, 4, 5, 6, 9, 8, 7]  # 7 <-> 9
    list_shift_left = [0, 1, 2, 3, 4, 7, 6, 5, 8, 9]   # 7 <-> 5

    assert True == False
    
    
def test_equal_lengths():
    pass

def test_unusual_case():
    """
    Unusual case 1 (NDCG 0.8939 -> 0.9325 vs 0.6678 -> 0.6355  ): [4, 0, 3, 2, 5, 1, 6] [5, 0, 3, 2, 4, 1, 6]
    
    4 and 5 swap. Originaly 4 and 5 have dist. 1 ( next to each other). 
    Then if the order is changed it should be seen as worser version. 
    Less relevat item took first rank and rel order changed. But NDCG still shows it as having less disagreement with orig
    """
    
def test_alphacharacters():
    pass

def test_edge_sizes_of_lists():
    pass

def test_unusual_case_2():
    pass