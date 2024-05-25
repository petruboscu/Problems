#include <iostream>
#include <vector>
#include <random>
#include <unordered_set>
#include <fstream>

int binary_search(int orderedElements[], int number_of_elements, int element);
void quick_sort(std::vector<int>& arr, int left, int right);
std::vector<int> generate_unique_random_numbers(int size, int max_value);

int main()
{
    int size = 20;
    int max_value = 100;
    std::vector<int> vec = generate_unique_random_numbers(size, max_value);

    std::cout << "Generated Vector: ";
    for (const auto& i : vec) {
        std::cout << i << ' ';
    }
    std::cout << '\n';

    quick_sort(vec, 0, vec.size() - 1);

    std::cout << "Sorted Vector: ";
    for (const auto& i : vec) {
        std::cout << i << ' ';
    }
    std::cout << '\n';

    // Open file in append mode
    std::ofstream file("vectors.txt", std::ios_base::app);
    if (!file.is_open()) {
        std::cerr << "Failed to open file." << std::endl;
        return 1;
    }

    // Write the sorted vector to the file
    for (const auto& i : vec) {
        file << i << ' ';
    }
    file << '\n';
    file.close();

    int largest_number = vec.back();

    for (int i = 0; i < largest_number; ++i) {
        int* arr = &vec[0];
        int index = binary_search(arr, vec.size(), i);
        if (index != -1)
            std::cout << "Element " << i << " is present on position " << index << "." << std::endl;
        else
            std::cout << "Element " << i << " is not present." << std::endl;
    }

    return 0;
}

int binary_search(int orderedElements[], int number_of_elements, int element)
{
    if (element > orderedElements[number_of_elements - 1] || element < orderedElements[0])
        return -1;

    int left = 0;
    int right = number_of_elements - 1;
    int middle;

    while (left <= right)
    {
        middle = (left + right) / 2;

        if (orderedElements[middle] == element)
            return middle;
        else if (element > orderedElements[middle])
            left = middle + 1;
        else
            right = middle - 1;
    }

    return -1;
}

void quick_sort(std::vector<int>& arr, int left, int right)
{
    if (left >= right) return;

    int pivot = arr[(left + right) / 2];
    int i = left, j = right;

    while (i <= j) {
        while (arr[i] < pivot) ++i;
        while (arr[j] > pivot) --j;

        if (i <= j) {
            std::swap(arr[i], arr[j]);
            ++i;
            --j;
        }
    }

    quick_sort(arr, left, j);
    quick_sort(arr, i, right);
}

std::vector<int> generate_unique_random_numbers(int size, int max_value)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(0, max_value);

    std::unordered_set<int> set;
    while (set.size() < size) {
        set.insert(dis(gen));
    }

    std::vector<int> vec(set.begin(), set.end());
    return vec;
}
