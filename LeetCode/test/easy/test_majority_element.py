from pytest import mark

from LeetCode.easy.majority_element import majority_element


@mark.parametrize(
    "nums, expected_result",
    [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
    ],
)
def test_majority_element(nums, expected_result):
    assert expected_result == majority_element(nums)
