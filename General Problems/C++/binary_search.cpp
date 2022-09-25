#include <iostream>

using namespace std;

int binary_search(int orderedElements[], int number_of_elements, int element);

int main()
{
    int list[10] = {1, 2, 4, 5, 6, 7, 9, 10, 11};
    int listLength = 9;

    int index;
    for (int element = 1; element <= 11; element++)
    {
        index = binary_search(list, listLength, element);
        if (index != -1)
            cout << "Element " << element << " is present on position " << index << "." << endl;
        else
            cout << "Element " << element << " is not present." << endl;
    }
}

int binary_search(int orderedElements[], int number_of_elements, int element)
{
    if (element > orderedElements[number_of_elements - 1] || element < orderedElements[0])
        return -1;


    int left = -1;
    int right = number_of_elements;
    int middle = (left + right) / 2;

    while (orderedElements[middle] != element)
    {
        if (element > orderedElements[middle])
        {
            left = middle;
            middle = (left + right) / 2;
        }
        else if (element < orderedElements[middle])
        {
            right = middle;
            middle = (left + right) / 2;
        }
        if(left == right - 1)
            return -1;
    }
    return middle;
}
