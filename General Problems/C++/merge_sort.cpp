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

int* merge_sort(int* elements, int number_of_elements, bool reversed)
{
  if (number_of_elements == 1)
    {
      int* element = (int*) malloc(sizeof(int));
      *element = *elements;
      return element;
    }
  else
    {
      int* sorted_elements = (int*) malloc(sizeof(int) * number_of_elements);
      int* left_elements = (int*) malloc(sizeof(int) * (number_of_elements / 2));
      int* right_elements = (int*) malloc(sizeof(int) * (number_of_elements - number_of_elements / 2));

      left_elements = merge_sort(elements, number_of_elements / 2, reversed);
      right_elements = merge_sort(elements + number_of_elements / 2, number_of_elements - number_of_elements / 2, reversed);

      int left_index = 0;
      int right_index = 0;
      while (left_index + right_index < number_of_elements)
      {
        if (reversed)
        {
          if (left_index < number_of_elements / 2 && right_index < number_of_elements - number_of_elements / 2)
          {
            if (*(left_elements + left_index) >= *(right_elements + right_index))
            {
              *(sorted_elements + left_index + right_index) = *(left_elements + left_index);
              left_index++;
            }
            else
            {
              *(sorted_elements + left_index + right_index) = *(right_elements + right_index);
              right_index++;
            }
          }
          else
          {
            if (left_index == number_of_elements / 2)
            {
              *(sorted_elements + left_index + right_index) = *(right_elements + right_index);
              right_index++;
            }
            else
            {
              *(sorted_elements + left_index + right_index) = *(left_elements + left_index);
              left_index++;
            }
          }
        }
        else
        {
          if (left_index < number_of_elements / 2 && right_index < number_of_elements - number_of_elements / 2)
          {
            if (*(left_elements + left_index) < *(right_elements + right_index))
            {
              *(sorted_elements + left_index + right_index) = *(left_elements + left_index);
              left_index++;
            }
            else
            {
              *(sorted_elements + left_index + right_index) = *(right_elements + right_index);
              right_index++;
            }
          }
          else
          {
            if (left_index == number_of_elements / 2)
            {
              *(sorted_elements + left_index + right_index) = *(right_elements + right_index);
              right_index++;
            }
            else
            {
              *(sorted_elements + left_index + right_index) = *(left_elements + left_index);
              left_index++;
            }
          }
        }
      }
    return sorted_elements;
   }
}

void print_list(int* elements, int number_of_elements, string name)
{
    cout << name << ": ";
    for(int index = 0; index < number_of_elements; index++)
        cout << elements[index] << " ";
    cout << endl;
}
