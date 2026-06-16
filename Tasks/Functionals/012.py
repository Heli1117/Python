def flatten(nested_list):
    flat = []
    for item in nested_list:
        if type(item) == list:
            for element in item:
                flat.append(element)
        else:
            flat.append(item)
    return flat

# Example
print(flatten([[1, 2], [3, [4, 5]]]))
