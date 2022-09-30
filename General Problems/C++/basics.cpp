#include<iostream>
#include<sstream>
#include<string>
#include<vector>

using namespace std;

vector<int> read_integers(string text);
vector<int> concatenate_integers(vector<int> first_vector, vector<int> second_vector);
void show_integers(vector<int> integers);

int main()
{
    vector<int> first_vector = read_integers("First Vector");
    vector<int> second_vector = read_integers("Second Vector");
    show_integers(concatenate_integers(first_vector, second_vector));

    return 0;
}

vector<int> read_integers(string text)
{
    cout << text <<": ";
    string input;
    int integer;
    char separator;
    cin >> input;
    stringstream str_stream(input);
    vector<int> integers;
    while (str_stream >> integer)
    {
        integers.push_back(integer);
        str_stream >> separator;
    }
    return integers;
}

vector<int> concatenate_integers(vector<int> first_vector, vector<int> second_vector)
{
    vector<int> result;
    int length = first_vector.size();
    for (int index = 0; index < length; index++)
    {
        result.push_back(first_vector[index]);
    }
    length = second_vector.size();
    for (int index = 0; index < length; index++)
    {
        result.push_back(second_vector[index]);
    }
    return result;
}

void show_integers(vector<int> integers)
{
    int length = integers.size();
    cout << "Integers:";
    for (int index = 0; index < length; index++)
    {
        cout << " " << integers[index];
    }
    return;
}
