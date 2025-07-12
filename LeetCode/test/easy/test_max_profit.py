from pytest import mark

from LeetCode.easy.max_profit import max_profit


@mark.parametrize(
    "prices, expected_result",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_max_profit(prices, expected_result):
    assert expected_result == max_profit(prices)
