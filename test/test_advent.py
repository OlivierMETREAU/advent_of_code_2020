from pytest import mark
from src.day1 import day1
from src.day2 import day2

@mark.parametrize("test_input, expected_result", [
   ([1721, 979, 366, 299, 675, 1456], 1721 * 299),
   ([1000, 555, 777, 1020], 1000 * 1020)
])
def test_day1_example_order_2(test_input, expected_result):
   assert day1(test_input) == expected_result

def test_day1_example_order_3():
   assert day1([1721, 979, 366, 299, 675, 1456], order=3) == 979 * 366 * 675

@mark.parametrize("test_input, expected_result", [
   (["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"], 2),
   (["1-3 a: abcde"], 1)
])
def test_day2_example(test_input, expected_result):
   assert day2(test_input) == expected_result

@mark.parametrize("test_input, expected_result", [
   (["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"], 1)
])
def test_day2_example_new_policy(test_input, expected_result):
   assert day2(test_input, new_policy=True) == expected_result