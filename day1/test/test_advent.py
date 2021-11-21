from pytest import mark
from src.day1 import day1

@mark.parametrize("test_input, expected_result", [
   ([1721, 979, 366, 299, 675, 1456], 1721 * 299),
   ([1000, 555, 777, 1020], 1000 * 1020)
])
def test_day1_example_oreder_2(test_input, expected_result):
   assert day1(test_input) == expected_result

def test_day1_example_oreder_3():
   assert day1([1721, 979, 366, 299, 675, 1456], order=3) == 979 * 366 * 675
