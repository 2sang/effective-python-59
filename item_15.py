
def sort_proirity(values, group):
    def helper(x):
        if x in group:
            return (0, x) # Will be sorted by first element in tuple then second item, and so on.
        return (1, x)
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_proirity(numbers, group)
print(numbers)



numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}

def sort_proirity2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_proirity2(numbers, group)  # Not working
print("found: {}".format(found))
print(numbers)


def sort_proirity2(numbers, group):
    found = False
    def helper(x):
        nonlocal found # nonlocal keyword finds the variable name up to one enclosing scope
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_proirity2(numbers, group)  # Now working
print("found: {}".format(found))
print(numbers)
