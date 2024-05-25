#include <iostream>

using namespace std;

int* merge_sort(int* elements, int number_of_elements, bool reversed=false);
int get_index_of_element(int elements[], int number_of_elements, int element);

int main()
{
  int maxWeight, objectCount;
  int backpacks[100];

  // cin > > maxWeight > > objectCount;// read the max Weight and the number of objects
  maxWeight = 6;
  objectCount = 5;
  int objects[6] = {3, 2, 6, 4, 3};

  int* sortedObjects = merge_sort(objects, objectCount, true);

  int objectWeight;
  int currentBackpackWeight = 0;
  int backpackCount = 1;

  bool added;
  int index;

  for(int oCount = 0; oCount < objectCount; oCount++)
    {
        added = false;
        // cin > > objectWeight;
        objectWeight = sortedObjects[oCount];

        // Check if we can put the object in our previous backpacks
        if(backpackCount > 1)
        {
          for (int weight = objectWeight; weight < maxWeight; weight++)
          {
            index = get_index_of_element(backpacks, backpackCount, maxWeight - weight);
            if(index != -1)
            {
              backpacks[index] += objectWeight;
              added = true;
              break;
            }
          }
        }
        // If we can't put the oject in previous backpacks
        if (!added)
        {
          // Check if we can put the object in our current backpack
          if(maxWeight - currentBackpackWeight >= objectWeight)
            currentBackpackWeight += objectWeight;
          // If we can't, add the current backpack to previous backpacks list and add the object to a new backpack
          else
          {
            backpacks[backpackCount] = currentBackpackWeight;
            backpackCount ++;
            currentBackpackWeight = objectWeight;
          }
        }
    }
  cout << "We need " << backpackCount << " Backpacks to carry all the objects.";
  return 0;
}

int get_index_of_element(int elements[], int number_of_elements, int element)
{
  for(int index = 1; index < number_of_elements; index++)
  {
    if (elements[index] == element)
      return index;
  }
  return -1;
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
