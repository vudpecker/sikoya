from exerc_dp_one import climbStairs


def test_exerc_dp_one_fail():
    n = 2
    ways = climbStairs(n)
    assert ways != 1