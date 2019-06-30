def inversion_control(arr, start, end):
    count = 0
    if (start >= end):
        return 0
    mid = start + ((end - start) // 2)
    count += inversion_control(arr, start, mid)
    count += inversion_control(arr, mid + 1, end)

    count += merge(arr, start, mid+1, mid + 1, end+1)

    return count


def merge(arr, l_start, l_end, r_start, r_end):
    count = 0
    l_index = l_start
    r_index = r_start
    output_list = []
    while (l_index < l_end and r_index < r_end):
        if (arr[l_index] > arr[r_index]):
            output_list.append(arr[r_index])
            count += l_end-(l_index)
            r_index += 1
        else:
            output_list.append(arr[l_index])
            l_index += 1
    if (l_index <l_end):
        output_list.extend(arr[l_index:l_end])
        l_index+=1
    else:
        output_list.extend(arr[r_index:r_end])
    for i in range(len(output_list)):
        arr[i + l_start] = output_list[i]
    return count


def count_inversions(arr):
    count = 0
    count = inversion_control(arr,0, len(arr)-1)
    print(count)
    return count


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")

arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)
print(arr)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)