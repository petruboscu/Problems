#include <iostream>
#include <fstream>
#include <string.h>
#include <string>

using namespace std;

int** read_matrix(string path, int& rows, int& collumns);
void show_matrix(int** matrix, int rows, int collumns);
int** rotate_matrix(int** matrix, int rows, int collumns, string direction);

int main(){
  int** matrix;
  int rows, collumns;
  matrix = (int**) read_matrix("input_matrix.txt", rows, collumns);
  cout << "Original Matrix:" << endl;
  show_matrix(matrix, rows, collumns);
  cout << "Rotated 'Right' Matrix:" << endl;
  show_matrix(rotate_matrix(matrix, rows, collumns, "right"), collumns, rows);
  cout << "Rotated 'Left' Matrix:" << endl;
  show_matrix(rotate_matrix(matrix, rows, collumns, "left"), collumns, rows);
}

int** read_matrix(string path, int& rows, int& collumns){
  ifstream file;
  file.open(path);

  file > > rows > > collumns;

  int **matrix = (int **)malloc(rows * sizeof(int*));
  for(int index = 0; index < rows; index++)
    matrix[index] = (int *)malloc(collumns * sizeof(int));

  for(int row_index = 0; row_index < rows; row_index++)
    for(int collumn_index = 0; collumn_index < collumns; collumn_index++)
      file > > matrix[row_index][collumn_index];

  return matrix;
}

void show_matrix(int** matrix, int rows, int collumns){
  for(int row_index = 0; row_index < rows; row_index++){
    for(int collumn_index = 0; collumn_index < collumns; collumn_index++)
      cout << matrix[row_index][collumn_index] << " ";
    cout << endl;
  }
}

int** rotate_matrix(int** matrix, int rows, int collumns, string direction){
  int **rotated_matrix = (int **)malloc(collumns * sizeof(int*));
  for(int index = 0; index < collumns; index++)
    rotated_matrix[index] = (int *)malloc(rows * sizeof(int));

  if (direction.compare("right") == 0){
    for(int collumn_index = 0; collumn_index < collumns; collumn_index++)
      for(int row_index = rows - 1; row_index > -1; row_index--)
        rotated_matrix[collumn_index][rows - row_index - 1] = matrix[row_index][collumn_index];
  }

  else if (direction.compare("left") == 0){
    for(int collumn_index = collumns - 1; collumn_index > - 1; collumn_index--)
      for(int row_index = 0; row_index < rows; row_index++)
        rotated_matrix[collumns - collumn_index - 1][row_index] = matrix[row_index][collumn_index];
  }

  return rotated_matrix;
}
