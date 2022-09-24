#include <iostream>

using namespace std;

int binary_search(int orderedElements[], int number_of_elements, int element);

int main()
{
    int list[12] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
    int element = 10;
    int index = binary_search(list, 11, element);
    if (index != -1)
        cout << "Element " << element << " is present on position " << index <<".";
    else
        cout << "Element " << element << " is not present.";
}

int binary_search(int orderedElements[], int number_of_elements, int element)
{
    if (element > orderedElements[number_of_elements - 1] || element < orderedElements[0])
        return -1;


    int left = 0;
    int right = number_of_elements - 1;
    int middle = (left + right) / 2;

    while(orderedElements[middle] != element)
    {
        cout << middle;
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
        if(left == right)
            return -1;
    }
    return middle;
}
