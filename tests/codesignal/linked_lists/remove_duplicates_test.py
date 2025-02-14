import pytest

from src.codesignal.linked_lists.remove_duplicates import solution


# fmt: off
@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1, 2, 2, 3, 3, 4, 5, 5, 5], [1, 2, 3, 4, 5]),
        ([1, 1, 1, 1], [1]),
        ([-1, -1, 2, 2, 3, 3], [-1, 2, 3]),
        ([-5, -5, -5, -4, -4, -4, -3, -3], [-5, -4, -3]),
        ([1000, 100, 10, 1, 1, 10, 100, 1000], [1000, 100, 10, 1]),
        ([34, 35, 35, 36, 37, 37, 37, 38, 39, 39], [34, 35, 36, 37, 38, 39]),
        ([0, 0, 0], [0]),
        ([100, 100, 200, 200, 300, 300, 400, 400], [100, 200, 300, 400]),
        ([1, -1, 2, -2, 3, -3, 4, -4, 5, -5], [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]),  # noqa
        ([10, 20, 10, 30, 20, 40, 30], [10, 20, 30, 40]),
        ([5, 15, 25, 5, 35, 25, 45], [5, 15, 25, 35, 45]),
        ([7, 8, 9, 8, 10, 9, 11], [7, 8, 9, 10, 11]),
        ([1, 4, 5, 4, 1, 6, 5], [1, 4, 5, 6]),
        ([0, 2, 4, 2, 6, 4, 8, 6], [0, 2, 4, 6, 8]),
        ([9, 7, 5, 3, 7, 1, 9], [9, 7, 5, 3, 1]),
        ([100, 200, 300, 100, 400, 300, 500, 200], [100, 200, 300, 400, 500]),
        ([50, 60, 70, 80, 90, 60, 70], [50, 60, 70, 80, 90]),
        ([21, 31, 41, 21, 51, 31, 61, 41], [21, 31, 41, 51, 61]),
        ([13, 23, 33, 13, 43, 23, 53], [13, 23, 33, 43, 53]),
        ([89, 78, 89, 67, 56, 45, 67], [89, 78, 67, 56, 45]),
    ],
)
# fmt: on
def test_remove_duplicates(
    list_to_linkedlist, linkedlist_to_list, input_list, expected_output
):
    head = list_to_linkedlist(input_list)
    result = solution(head)
    assert linkedlist_to_list(result) == expected_output
