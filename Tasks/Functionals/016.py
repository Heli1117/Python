def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

# Example
print(remove_duplicates([1, 2, 3, 2, 1, 4]))
