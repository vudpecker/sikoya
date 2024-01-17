from exerc_dp_one import climbStairs

def test_exerc_dp_one_negate():
    n = 5
    ways = climbStairs(n)
    assert ways != 4

def test_exerc_dp_one_pass():
    n = 4
    ways = climbStairs(n)
    assert ways == 5

def test_exerc_dp_one_fail():
    n = 2
    ways = climbStairs(n)
    assert ways != 1