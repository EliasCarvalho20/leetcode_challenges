from pytest import mark

from LeetCode.medium.max_profit import max_profit


@mark.parametrize(
    "prices, expected_result",
    [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
    ],
)
def test_max_profit(prices, expected_result):
    assert expected_result == max_profit(prices)
