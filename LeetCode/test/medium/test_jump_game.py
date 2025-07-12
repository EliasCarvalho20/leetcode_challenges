from pytest import mark

from LeetCode.medium.jump_game import can_jump


@mark.parametrize(
    "nums, expected_result",
    [
        ([1, 1, 2, 2, 0, 1, 1], True),
        ([3, 2, 1, 0, 4], False),
        ([1, 1, 1, 0], True),
        ([2, 3, 1, 1, 4], True),
        ([0], True),
    ],
)
def test_jump_game(nums, expected_result):
    assert expected_result == can_jump(nums)
