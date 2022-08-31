def two_sum(given_list: list, target: int) -> list:
    indexes_list = []
    for element in given_list:
        diff = abs(element - target)
        if diff in given_list:
            first_index = given_list.index(element)
            second_index = given_list.index(diff)
            indexes_list.append((first_index, second_index))
    return indexes_list


if __name__ == '__main__':
    input_list = [2, 3, 6, 8, 1, 4, 7, 9, 5, 0]
    for pair in two_sum(input_list, 9):
        index1, index2 = pair
        print(f'index1: {index1}\nindex2: {index2}\n')
