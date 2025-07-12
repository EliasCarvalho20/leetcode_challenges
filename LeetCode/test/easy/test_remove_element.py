from pytest import mark

from LeetCode.easy.remove_element import remove_element


@mark.parametrize(
    "nums, val, expected_result",
    [
        ([3, 2, 2, 3], 3, 2),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
    ],
)
def test_merge(nums, val, expected_result):
    assert expected_result == remove_element(nums, val)
