from dprs import dprs

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
    
    
#0,1,2     7,8,9
#2,1,0     9,8,7
#(0,2) -> (2,0) vs  (7,9) -> (9,7) vs (0,8) -> (8,0)
