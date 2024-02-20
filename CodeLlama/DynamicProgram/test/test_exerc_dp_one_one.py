from exerc_dp_one import climbStairs

def test_exerc_dp_one_pass():
    n = 4
    ways = climbStairs(n)
    assert ways == 5
