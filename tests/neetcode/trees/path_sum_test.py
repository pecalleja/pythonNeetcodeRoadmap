import pytest

from src.neetcode.trees.path_sum import Solution


@pytest.mark.parametrize(
    "lst, target_sum, expected",
    [
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
        ([1, 2, 3], 5, False),
        ([1, 2], 1, False),
        ([1, 2], 3, True),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 26, True),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 19, False),
        ([], 0, False),
        ([1], 1, True),
    ],
)
def test_hasPathSum(list_to_tree, lst, target_sum, expected):
    solution = Solution()
    root = list_to_tree(lst)
    assert solution.hasPathSum(root, target_sum) == expected
