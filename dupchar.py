# In this problem, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.
# Strings in the initial list will be lowercase only, no spaces.
random_array = ["abracadabra","allottee","assessee"]
# function that takes an array of strings (in lowercase)
def dup(arr):
    # declare our variables
    # a new empty array to store our modified strings
    modified_array = []
    # loop through the given array of strings
    for i in range(len(arr)):
        # for each element in the array
        word = arr[i]
        print("IN LOOP 1")
        print(word)
        # go through the string element 
        j = 0
        while (j < len(word) - 1):
            print(j)
            # look at the two chars next to each other (in sequential order) [ex: abcd]
            # compare them [ex: compare a and b]
            print("IN LOOP 2")
            print(word)
            if (word[j:j + 1] == word[j + 1:j + 2]):
                # if they are identical, remove one of them
                word = word[0:j + 1] + word[j + 2:]
                print("IN CONDITION IDENTICAL")
                print(word)
                j -= 1
            # if not identical, increment to the next two chars [ex: b and c]
            j += 1
        # append the solved string to the new array
        modified_array.append(word)
    # return an array of the same strings but without the duplicated letters
    return modified_array
print(dup(["aaaabbbracadabraaaa", "secondasdpojaes", "aaaaaaaabbbbssss"]))
# ["abracadabra","alote","asese"]
# dup(["kelless","keenness"]) = ["keles","kenes"].