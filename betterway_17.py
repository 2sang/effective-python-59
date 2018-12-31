def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

def normalize_comp(numbers):
    total = sum(numbers)
    return [100*x/total for x in numbers]

visits = [15, 35, 80]
print(normalize(visits))
print(normalize_comp(visits))

