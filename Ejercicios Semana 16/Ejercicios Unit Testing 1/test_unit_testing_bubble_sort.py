#Ejercicios de Unit Testing 1

from unit_testing_bubble_sort import bubble_sort
import random
import pytest

# Unit Test for Small lists
def test_unit_testing_small_lists_bubble_sort():
    #Arrange
    list_to_sort = [7, 5, 3, 2, 8, 1, 4, 9, 6]
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #Act
    bubble_sort(list_to_sort)
    #Assert
    assert list_to_sort == sorted_list


# Unit Test for Large lists
def test_unit_testing_large_lists_bubble_sort():
    #Arrange
    list_size = 200
    list_to_sort = [random.randint(1,1000) for index in range (list_size)]
    sorted_list = sorted(list_to_sort.copy())
    #Act
    bubble_sort(list_to_sort)
    #Assert
    assert list_to_sort == sorted_list
    assert len(list_to_sort) == list_size


# Unit Test for Empty lists
def test_unit_testing_empty_lists_bubble_sort():
    #Arrage
    empty_list = []
    #Act
    bubble_sort(empty_list)
    #Assert
    assert empty_list == []


# Unit Test for Invalid lists
def test_unit_testing_invalid_lists_bubble_sort():
    #Arrange
    #Act
    #Assert
    with pytest.raises(TypeError):
        bubble_sort("test")

    with pytest.raises(TypeError):
        bubble_sort("3.14")