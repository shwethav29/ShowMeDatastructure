def mergesort(l, start, end):
    if (end-start <=1):
        return
    mid = (end - start) // 2
    mergesort(l, start, start + mid)
    mergesort(l, start + mid, end)
    merge(l, start, start + mid, start + mid, end)


def merge(l, left_start, left_end, right_start, right_end):
    left_index = left_start
    right_index = right_start
    temp_list = list()
    while (left_index < left_end and right_index < right_end):
        if (l[left_index] < l[right_index]):
            temp_list.append(l[left_index])
            left_index +=1
        else:
            temp_list.append(l[right_index])
            right_index +=1
    while (left_index < left_end):
        temp_list.append(l[left_index])
        left_index +=1
    while (right_index < right_end):
        temp_list.append(l[right_index])
        right_index +=1
    for i,element in enumerate(temp_list):
        l[left_start + i] = element


def sort_string(string):
    l = list(string)
    mergesort(l,0,len(string))
    return "".join(l)

def find_indexOf_lowercase(sorted_string):
    ascii_a = ord('a')
    i=0
    for element in list(sorted_string):
        if(ord(element) < ascii_a):
            i+=1
        else:
            return i

def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list

    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    sorted_string = sort_string(string)
    output_list = list()
    ascii_a = ord('a')
    ascii_A = ord('A')
    lowercase_index = find_indexOf_lowercase(sorted_string)
    uppercase_index = 0
    for i,char in enumerate(list(string)):
        if(ord(char)<ascii_a and ord(char) >= ascii_A):
            output_list.append(sorted_string[uppercase_index])
            uppercase_index+=1
        else:
            output_list.append(sorted_string[lowercase_index])
            lowercase_index+=1


    return "".join(output_list)


def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]

    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")

test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)

test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)