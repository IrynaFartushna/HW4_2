def sum_list(input_list):

    if not input_list:
        return 0

    sum_even_indices = sum(input_list[i] for i in range(0, len(input_list), 2))

    last_element = input_list[-1]

    result = sum_even_indices * last_element

    return result
print(sum_list([0,1,7,2,4,8]))
print(sum_list([1,3,5]))
print(sum_list([6]))
print(sum_list([]))