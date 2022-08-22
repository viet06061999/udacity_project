def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def sort_012(input_list):
    if input_list == None:
        return None
    if len(input_list)==0:
        return []
    s = 0
    f = 0
    mid = 1
    n = len(input_list) - 1
    while s <= n:
        if input_list[s] < mid:
            input_list[s],input_list[f] =  swap(input_list[s], input_list[f])
            s = s + 1
            f = f + 1
        elif input_list[s] > mid:
            input_list[s],input_list[n] =  swap(input_list[s], input_list[n])
            n = n - 1
        else:
            s = s + 1
    return input_list
         


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([])
test_function([1])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])