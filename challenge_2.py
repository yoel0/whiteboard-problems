def digits(num):
    digit_array = []
    # set an empty list for the digits
    result = []
    # set an empty list for the result 
    string_numbers = str(num)
    # convert the numbers into a string to allow for iteration
    for i in range(0, len(string_numbers) - 1):
    # iterate up through the string of numbers 
    # up until the second to last element
        for j in range(i + 1, len(string_numbers)):
        # iterate up to the end from the next number after each element
            digit_array.append(string_numbers[i] + string_numbers[j])
            # add both elements to the the digit_array as a string of two
            # numbers, like this '85'
    for numbers in digit_array:
    # iterate each element in the digit list, which should be a string
    # of length 2 of each possible number combination
        result.append(int(numbers[0]) + int(numbers[1]))
        # add both integer values together in each element of the digit_array
        # and append them to the result list
    return result

print(digits(156))
# should return [ 6, 7, 11 ]
print(digits(81596))
# should return [ 9, 13, 17, 14, 6, 10, 7, 14, 11, 15 ]
print(digits(3852))
# should return [ 11, 8, 5, 13, 10, 7 ]
print(digits(3264128))
# should return [ 5, 9, 7, 4, 5, 11, 8, 6, 3, 4, 10, 10, 7, 8, 14, 5, 6, 12, 3, 9, 10 ]
print(digits(999999))
# should return [ 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18 ]