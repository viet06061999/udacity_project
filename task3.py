def rearrange_digits(input_list):
    if len(input_list)<=1:
        return [-1, -1]
        
    firstNum = "" 
    secondNum = ""
    freq_input = [0]*10
    for val in input_list:
        freq_input[val] += 1 
    left = True
    for val in range(len(input_list)):
        maxNum = max(temp);
        maxIndex = temp.index(maxNum)
        if (val % 2 == 0) :
            firstNum += str(maxNum);
        
        else :
            secondNum += str(maxNum);
        
        temp.pop(maxIndex)
    return [int(firstNum), int(secondNum)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
