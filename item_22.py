# Item 22: Preffer helper classes over bookkeeping with dictionaries and tuples
class SimpleGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book = SimpleGradebook()
book.add_student('Issac Newton')
book.report_grade('Issac Newton', 90)
print(book.average_grade('Issac Newton'))

# If we want to extend the above classs to keep a list of grades by subject:

class BySubjectGradeBook(object):

    """Docstring for BySubjectGradeBook. """

    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}  # inner dictionaries

    # And so on..


# Imagine our requirements change again. Now we want to average the student's score
# by certain weights, positional arguments in class methods are getting more unclear.

# Refactoring to classes
