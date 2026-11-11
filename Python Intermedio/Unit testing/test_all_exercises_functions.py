from func_exercise3 import plus
from func_exercise4 import word_inverse
from func_exercise5 import i
from func_exercises6 import order
from func_exercises7 import is_prime,filter_primes


#------Ejercicio 3------

def test_plus_example():
    # Arrange
    numbers = [4, 6, 2, 29]
    expected = 41

    # Act
    result = plus(numbers)

    # Assert
    assert result == expected


def test_plus_negative_numbers():
    # Arrange
    numbers = [10, -4, -6, 3]
    expected = 3

    # Act
    result = plus(numbers)

    # Assert
    assert result == expected


def test_plus_single_element():
    # Arrange
    numbers = [7]
    expected = 7

    # Act
    result = plus(numbers)

    # Assert
    assert result == expected



#------Ejercicio 4------


def test_word_inverse_example():
    # Arrange
    text = "Hola mundo"
    expected = "odnum aloH"

    # Act
    result = word_inverse(text)

    # Assert
    assert result == expected


def test_word_inverse_palindrome():
    # Arrange
    text = "radar"
    expected = "radar"

    # Act
    result = word_inverse(text)

    # Assert
    assert result == expected


def test_word_inverse_empty_string():
    # Arrange
    text = ""
    expected = ""

    # Act
    result = word_inverse(text)

    # Assert
    assert result == expected




#------Ejercicio 5------

def test_count_upper_lower_example():
    # Arrange
    text = "I love Nación Sushi"
    expected = (3, 13)

    # Act
    result = i(text)

    # Assert
    assert result == expected


def test_count_upper_lower_only_uppercase():
    # Arrange
    text = "ABC"
    expected = (3, 0)

    # Act
    result = i(text)

    # Assert
    assert result == expected


def test_count_upper_lower_ignores_digits_and_symbols():
    # Arrange
    text = "hello world 123!"
    expected = (0, 10)

    # Act
    result = i(text)

    # Assert
    assert result == expected


#------Ejercicio 6------

def test_order_example():
    # Arrange
    text = "python-variable-funcion-computadora-monitor"
    expected = "computadora-funcion-monitor-python-variable"

    # Act
    result = order(text)

    # Assert
    assert result == expected


def test_order_reverse_order():
    # Arrange
    text = "c-b-a"
    expected = "a-b-c"

    # Act
    result = order(text)

    # Assert
    assert result == expected


def test_order_single_word():
    # Arrange
    text = "python"
    expected = "python"

    # Act
    result = order(text)

    # Assert
    assert result == expected


#------Ejercicio 7------


def test_filter_primes_example():
    # Arrange
    numbers = [1, 4, 6, 7, 13, 9, 67]
    expected = [7, 13, 67]

    # Act
    result = filter_primes(numbers)

    # Assert
    assert result == expected


def test_filter_primes_all_primes():
    # Arrange
    numbers = [2, 3, 5, 7]
    expected = [2, 3, 5, 7]

    # Act
    result = filter_primes(numbers)

    # Assert
    assert result == expected


def test_filter_primes_no_primes():
    # Arrange
    numbers = [0, 1, 4, 6, 8, 9]
    expected = []

    # Act
    result = filter_primes(numbers)

    # Assert
    assert result == expected