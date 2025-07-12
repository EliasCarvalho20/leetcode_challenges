from pytest import mark

from LeetCode.easy.remove_duplicates import remove_duplicates


@mark.parametrize(
    "nums, expected_result",
    [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
    ],
)
def test_merge(nums, expected_result):
    assert expected_result == remove_duplicates(nums)
