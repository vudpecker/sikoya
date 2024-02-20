from exerc_dp_one import climbStairs

def test_exerc_dp_one_negate():
    n = 5
    ways = climbStairs(n)
    assert ways != 4
