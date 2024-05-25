import unittest

class TestFindMissingRanges(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_missing_ranges([]), ['0 -> infinity'])

    def test_full_list(self):
        self.assertEqual(find_missing_ranges(list(range(100))), ['100 -> infinity'])

    def test_single_element_list(self):
        self.assertEqual(find_missing_ranges([5]), ['0 -> 4', '6 -> infinity'])

    def test_multiple_elements_list(self):
        self.assertEqual(find_missing_ranges([0, 1, 3, 50, 75]), ['2', '4 -> 49', '51 -> 74', '76 -> infinity'])

    def test_consecutive_elements_list(self):
        self.assertEqual(find_missing_ranges([0, 1, 2, 3, 4]), ['5 -> infinity'])

    def test_non_consecutive_elements_list(self):
        self.assertEqual(find_missing_ranges([0, 10, 20, 30, 40]), ['1 -> 9', '11 -> 19', '21 -> 29', '31 -> 39', '41 -> infinity'])

def find_missing_ranges(list_with_missing_elements: list) -> list:
    """
    This function takes a list of integers from 0 to infinity and returns a list of strings representing the missing ranges in the input list.

    For example, if the input list is [0, 1, 3, 50, 75], the function will return ['2', '4 -> 49', '51 -> 74'].

    If the input list is empty, it assumes all numbers from 0 to infinity are missing. If the input list contains consecutive numbers from 0 to some number, it returns the range of missing numbers from the last number in the list to infinity.
    """

    missing_ranges = list()

    if len(list_with_missing_elements) == 0:
        missing_ranges.append('0 -> infinity')

    else:
        previous_element = list_with_missing_elements[0]
        if previous_element != 0:
            missing_ranges.append(f'0 -> {previous_element - 1}')
        for element in list_with_missing_elements[1:]:
            if element - previous_element == 2:
                missing_ranges.append(f'{element - 1}')
            elif element - previous_element > 2:
                missing_ranges.append(
                    f'{previous_element + 1} -> {element - 1}')
            previous_element = element
        missing_ranges.append(f'{previous_element + 1} -> infinity')

    return missing_ranges


if __name__ == '__main__':
    print(find_missing_ranges([0, 1, 3, 50, 75]))
    unittest.main()

