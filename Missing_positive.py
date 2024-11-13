def first_missing_positive(numbers):
    #taking only positive numbers and create a set of them 
    positive_nb = set()
    for num in numbers:
        if num > 0:
            positive_nb.add(num)
    # searching for the smallest missing positive number
    n = len(positive_nb)
    for i in range(1, n + 2):  # checking from 1 to the end of the list
        if i not in positive_nb:
            return i  # return the first missing positive integer
print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([1, 2, 0]))
