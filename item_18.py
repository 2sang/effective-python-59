# Item 18: Reduce visual noise with variable positional arguments
# The best practice is to always specify optional arguments using the keyword names and
# never pass them as positional arguments.

import json

# default parameter initialized at 'module load' time.
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 3

print("foo: {}".format(foo))
print("bar: {}".format(bar))


# Solution
def decode(data, default=None):
    """Load JSON data from a string.
    arguments:
    data -- JSON data to decode
    default -- Value to return if decoding fails
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

