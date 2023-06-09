def unique_list(numbers):
    unique = []
    for item in numbers :
        if item not in unique:
            unique.append(item)
    return unique

print(unique_list([1,23, 2, 3,22,22,65]))
