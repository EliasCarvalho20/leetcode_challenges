from pytest import mark

from LeetCode.easy.merge_sorted_array import merge


@mark.parametrize(
    "nums1, m, nums2, n, expected_result",
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ],
)
def test_merge(nums1, m, nums2, n, expected_result):
    assert expected_result == merge(nums1, m, nums2, n)
