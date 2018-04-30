# Lab 4: Object-Oriented Python

# 4/30/2018 created

# Basic Classes
# class StanfordCourse created in a file courses.py
# when import this class and create an instance of the class in the interactive interpreter:
$ python3
>>> from courses import StanfordCourse
>>> stanford_python = StanfordCourse("","","")

# Inheritance
# __le__
@total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
				
>>>	

# SimpleGraph
# Longest path
# D'ijkstras Algorithm
# A*
# Max Flow
# K-Clique
# Largest Connected Component
# is_bipartite
# hamiltonian_path_exists

# Timed Key-Value Store


