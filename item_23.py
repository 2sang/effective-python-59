from collections import defaultdict
# Item 23: Accept functions for simple interfaces instead of classes
# 'Hook' is used by APIs to call back your code while execute. For example,
names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x)) # Lambda function applied as a hook in sort() call.
print(names)

# Defines a hook
def log_missing():
    print('Key added')
    return 0

# collections.defaultdict() takes first argument in function form, it's called
# when key that isn't exists in dictionary when inserting.

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue',17),
    ('orange', 9),
]

result = defaultdict(log_missing, current)  # Second argument is used for initializing dict
print('Before:', dict(result))
for k, v in increments:
    result[k] += v
print('after:', dict(result))
# Supplying functions like log_missing makes APIs easy to build and testing.


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for k, v in increments:
        result[k] += v

    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2
