import io
import unittest
from contextlib import redirect_stdout

from main import (
    add_mohammad_to_list, 
    check_length_is_even, 
    check_length_is_odd, 
    eliminate_team, 
    second_half_of_list_if_even
)


class ContainersTestCase(unittest.TestCase):
    def setUp(self):
        self.response = io.StringIO()

    def test_length_is_odd(self):
        with redirect_stdout(self.response):
            self.assertTrue(check_length_is_odd([1]))
            self.assertTrue(check_length_is_odd([1, 2, 3]))
            self.assertTrue(check_length_is_odd([1, 2, 3, 4, 5]))

    def test_length_is_event(self):
        with redirect_stdout(self.response):
            self.assertTrue(check_length_is_even([1, 2]))
            self.assertTrue(check_length_is_even([1, 2, 3, 4]))
            self.assertTrue(check_length_is_even([1, 2, 3, 4, 5, 6]))

    def test_adding_mohammad(self):
        with redirect_stdout(self.response):
            value = add_mohammad_to_list(["sensei"])[-1]
            self.assertEqual(value.lower(), "mohammad")

    def test_eliminate_team(self):
        with redirect_stdout(self.response):
            teams = ["Brazil", "Germany", "Italy"]
            actual = eliminate_team(teams.copy())
            expected = teams[-1]
            self.assertEqual(actual, expected)

    def test_second_half_of_list_if_even(self):
        # second_half_of_list_if_even(["apple", "orange", "banana", "kiwi"]) -> ["banana", "kiwi"]
        # second_half_of_list_if_even(["apple", "orange", "banana", "kiwi", "blueberry"]) -> []
        with redirect_stdout(self.response):
            fruits = ["apple", "orange", "banana", "kiwi"]
            actual = second_half_of_list_if_even(fruits.copy())
            expected = fruits[-2:]
            self.assertEqual(actual, expected)

            fruits.append("blueberry")
            actual = second_half_of_list_if_even(fruits.copy())
            expected = []
            self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()
