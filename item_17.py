# Item 17: Be defensive when iterating over arguments
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

def normalize_comp_copy(numbers):
    numbers = list(numbers)  # Works even if the iterator exhasted.
    total = sum(numbers)
    return [100*x/total for x in numbers]

visits = [15, 35, 80]
print(normalize(visits))
print(normalize_comp(visits))

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits('texas_tourlists.txt')
# Iterator already exhausted at this point, it cannot further go forward.
percentages = normalize(it)
print(percentages)

it2 = read_visits('texas_tourlists.txt')
# Iterator already exhausted at this point
percentages = normalize_comp_copy(it2)
print(percentages)

# The problem with this approach is the copy of the input iterator's contents could be large.


# Solution:
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path
        
    # Every time the instance of ReadVisits is called, new iterator object is allocated.
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

# Tip to detect a value is an iterator or a container:
assert iter(it2) == iter(it2)
