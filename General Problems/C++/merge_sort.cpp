#include <iostream>
#include <string>

using namespace std;

int* merge_sort(int* elements, int number_of_elements, bool reversed=false);
void print_list(int* elements, int number_of_elements, string name);

int main()
{
    int list[21] = {2, 5, 3, 1, 7, 4, 9, 8, 6, 15, 13, 18, 12, 11, 14, 17, 19, 20, 10, 16};
    int listLength = 20;
    int* orderedList = merge_sort(list, listLength);
    int* reversedOrderedList = merge_sort(list, listLength, true);
    print_list(list, listLength, "List");
    print_list(orderedList, listLength, "Ordered List");
    print_list(reversedOrderedList, listLength, "Reversed Ordered List");

}

/**
 * Sorts an array of integers using the merge sort algorithm.
 *
 * @param elements The array of integers to be sorted.
 * @param number_of_elements The number of elements in the array.
 * @param reversed A boolean indicating whether to sort in ascending (false) or descending (true) order.
 * @return A pointer to the sorted array.
 */
int* merge_sort(int* elements, int number_of_elements, bool reversed){
  // Base case: If there is only one element, return it as it is already sorted.
  if (number_of_elements == 1) {
    int* element = (int*) malloc(sizeof(int));
    *element = *elements;
    return element;
  } else {
    // Allocate memory for the sorted array.
    int* sorted_elements = (int*) malloc(sizeof(int) * number_of_elements);
    // Split the array into two halves.
    int* left_elements = (int*) malloc(sizeof(int) * (number_of_elements / 2));
    int* right_elements = (int*) malloc(sizeof(int) * (number_of_elements - number_of_elements / 2));

    // Recursively sort the left and right halves.
    left_elements = merge_sort(elements, number_of_elements / 2, reversed);
    right_elements = merge_sort(elements + number_of_elements / 2, number_of_elements - number_of_elements / 2, reversed);

    // Merge the sorted left and right halves.
    int left_index = 0;
    int right_index = 0;
    while (left_index + right_index < number_of_elements) {
      if (reversed) {
        // If sorting in descending order, compare elements in reverse.
        if (left_index < number_of_elements / 2 && right_index < number_of_elements - number_of_elements / 2) {
          if (*(left_elements + left_index) >= *(right_elements + right_index)) {
            *(sorted_elements + left_index + right_index) = *(left_elements + left_index);
            left_index++;
          } else {
            *(sorted_elements + left_index + right_index) = *(right_elements + right_index);
            right_index++;
          }
        } else {
          // If one half is exhausted, append the remaining elements from the other half.
          if (left_index == number_of_elements / 2) {
            *(sorted_elements + left_index + right_index) = *(right_elements + right_index);
            right_index++;
          } else {
            *(sorted_elements + left_index + right_index) = *(left_elements + left_index);
            left_index++;
          }
        }
      } else {
        // If sorting in ascending order, compare elements normally.
        if (left_index < number_of_elements / 2 && right_index < number_of_elements - number_of_elements / 2) {
          if (*(left_elements + left_index) <= *(right_elements + right_index)) {
            *(sorted_elements + left_index + right_index) = *(left_elements + left_index);
            left_index++;
          } else {
            *(sorted_elements + left_index + right_index) = *(right_elements + right_index);
            right_index++;
          }
        } else {
          // If one half is exhausted, append the remaining elements from the other half.
          if (left_index == number_of_elements / 2) {
            *(sorted_elements + left_index + right_index) = *(right_elements + right_index);
            right_index++;
          } else {
            *(sorted_elements + left_index + right_index) = *(left_elements + left_index);
            left_index++;
          }
        }
      }
    }
    return sorted_elements;
  }
}

/**
 * Prints an array of integers.
 *
 * @param elements The array of integers to be printed.
 * @param number_of_elements The number of elements in the array.
 * @param name The name to be printed before the array.
 */
void print_list(int* elements, int number_of_elements, string name) {
  cout << name << ": ";
  for (int index = 0; index < number_of_elements; index++)
    cout << elements[index] << " ";
  cout << endl;
}
