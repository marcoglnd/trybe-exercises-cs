from exercicio1 import fizz_buzz

def test_returns_expected_array_when_number_3_inserted():
    assert fizz_buzz(3) == [1, 2, 'Fizz']

def test_returns_expected_array_when_number_5_inserted():
    assert fizz_buzz(5) == [1, 2, 'Fizz', 4, 'Buzz']

def test_returns_expected_array_when_number_10_inserted():
    assert fizz_buzz(10) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']

def test_returns_expected_array_when_number_3_inserted():
    assert fizz_buzz(15) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
