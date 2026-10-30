import pytest
from bubble_sort import my_bubble_sort



def test_small_list():
    #Arrange 
    lista = [1,5,2,4]
    expected = [1,2,4,5]

    #Act
    result = my_bubble_sort(lista)

    #Assert 
    assert result == expected
    



def test_biggest_list():
    # Arrange
    lista = [
        34, 26, 100, 85, 79, 82, 22, 94, 83, 2,
        23, 1, 62, 74, 25, 50, 27, 45, 77, 80,
        48, 3, 52, 39, 15, 49, 11, 33, 17, 95,
        66, 70, 43, 60, 89, 99, 67, 92, 58, 30,
        21, 88, 35, 61, 32, 14, 64, 4, 57, 87,
        46, 63, 59, 24, 93, 41, 37, 68, 72, 81,
        44, 53, 36, 40, 76, 19, 97, 38, 18, 6,
        91, 96, 98, 78, 29, 16, 73, 90, 55, 71,
        86, 31, 9, 54, 56, 12, 5, 28, 65, 8,
        75, 47, 13, 69, 10, 7, 84, 51, 20, 42,
        101,
    ]
    expected = sorted(lista)

    # Act
    result = my_bubble_sort(lista)

    # Assert
    assert len(lista) > 100
    assert result == expected



def test_empty_list():

    #Arrange
    lista = []
    expected = []

    #Act
    result = my_bubble_sort(lista)

    #Assert 



    assert result == expected


def test_not_a_list():

    with pytest.raises(TypeError):
        my_bubble_sort(5)

    with pytest.raises(TypeError):
        my_bubble_sort("abc")

    with pytest.raises(TypeError):
        my_bubble_sort(None)

    with pytest.raises(TypeError):
        my_bubble_sort((1, 2, 3))