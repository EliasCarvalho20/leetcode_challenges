from pytest import mark

from LeetCode.medium.rotate_array import rotate


@mark.parametrize(
    "nums, k, expected_result",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ],
)
def test_rotate(nums, k, expected_result):
    assert expected_result == rotate(nums, k)
