#include<iostream>
#include<sstream>
#include<string>
#include<vector>

using namespace std;

vector<int> read_integers(string vector_name);
vector<int> concatenate_integers(vector<int> first_vector, vector<int> second_vector);
vector<int> operation_on_integers(char operation, vector<int> first_vector, vector<int> second_vector);
void show_integers(vector<int> integers);

int main()
{
    vector<int> first_vector = read_integers("First Vector");
    vector<int> second_vector = read_integers("Second Vector");
    show_integers(concatenate_integers(first_vector, second_vector));
    show_integers(operation_on_integers('+', first_vector, second_vector));
    show_integers(operation_on_integers('-', first_vector, second_vector));
    show_integers(operation_on_integers('X', first_vector, second_vector));
    show_integers(operation_on_integers(':', first_vector, second_vector));

    return 0;
}

vector<int> read_integers(string vector_name)
{
    cout << vector_name <<": ";
    string input;
    int integer;
    char separator;
    cin > > input;
    stringstream str_stream(input);
    vector<int> integers;
    while (str_stream > > integer)
    {
        integers.push_back(integer);
        str_stream > > separator;
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
    cout << endl;
    return;
}

vector<int> operation_on_integers(char operation, vector<int> first_vector, vector<int> second_vector)
{
    vector<int> result;
    int index = 0;
    int first_length = first_vector.size();
    int second_length = second_vector.size();

    if (first_length != second_length)
    {
        cout << "The vectors are not the same size" << endl;
    }

    while(first_length || second_length)
    {
        if (first_length && second_length)
        {
            switch(operation)
            {
                case '+':
                result.push_back(first_vector[index] + second_vector[index]);
                break;

                case '-':
                result.push_back(first_vector[index] - second_vector[index]);
                break;

                case 'X':
                result.push_back(first_vector[index] * second_vector[index]);
                break;

                case ':':
                result.push_back(first_vector[index] / second_vector[index]);
                break;
            }
            first_length--;
            second_length--;
        }
        else if(first_length)
        {
            if (operation != 'X' && operation != ':')
            {
                result.push_back(first_vector[index]);
            }
            else
            {
                result.push_back(0);
            }
            first_length--;

        }
        else if(second_length)
        {
            if (operation != 'X' && operation != ':')
            {
                result.push_back(second_vector[index]);
            }
            else
            {
                result.push_back(0);
            }
            second_length--;

        }
        index++;
    }
    return result;
}

