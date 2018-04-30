# Lab3: Functional Programming
# 4/27/2018 Created
# 4/30/2018 Finishedl and updated with solutions

import random       # choice
import functools    # reduce, wraps
import operator     # mul
import itertools    # permutations, cycle, starmap, zip_longest
import collections  # OrderedDict
import inspect      # Signature


#### Functional Tools

# Lambdas
# Map
map(int,['12','-2','0'])
map(len,['hello','world'])
map(lambda s:s[::-1],['hello','world'])
map(lambda x:(x,x**2,x**3),range(2,6))
map(lambda l, r: l * r, zip(range(2,5),range(3,9,2))) # => [6, 15, 28]

# Filter
filter(lambda a: int(a) >= 0, ['12','-2','0'])
filter(lambda a: a == 'world',['hello','world'])
filter(lambda a: a%3==0 or a%5==0,range(20))

## Useful Modules
def gcd(a, b):
    """Reference implementation of finding the
    greatest common denominator of two numbers"""
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*args):
	"""Reference implementation of finding the
    least common multiple of two numbers"""
	return functools.reduce(lambda x, y: x * y / gcd(x, y), args)

def fact(n):
    return functools.reduce(operator.mul, range(n))
	
# operator
import operator
operator.add(1,3)
operator.pow(2,3)
operator.itemgetter(1)([1,2,3]) # => 2

# sort, max, min
words = ['pear', 'cabbage', 'apple', 'bananas']
min(words)  # => 'apple'
words.sort(key=lambda s: s[-1])  # Alternatively, key=operator.itemgetter(-1)
words  # => ['cabbage', 'apple', 'pear', 'bananas'] ... Why 'cabbage' > 'apple'? original order
    # Because the builtin sort is stable - even though they both have the smae
    # value after application of the key function, cabbage appears before apple
    # in the original list, so it also is before apple in the sorted list
max(words, key=len)  # 'cabbage' ... Why not 'bananas'? original order
min(words, key=lambda s: s[1::2])  # What will this value be? bananas, 'cabbage'[1::2] => abg


def highest_alphanumeric_score():
    def alpha_score(upper_letters):
        """Computes the alphanumeric sum of letters in a string.
        Prerequisite: upper_letters is composed entirely of capital letters.
        """
        return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

    # alpha_score('ABC')  # => 6 = 1 ('A') + 2 ('B') + 3 ('C')

    def two_best(words):
        words.sort(key=lambda word: alpha_score(filter(str.isupper, word)), reverse=True)
        return words[:2]

    print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))
    # => ['PyThOn', 'wOrLD']

#### Purely Functional Programming
def functional():
    """
    if score == 1:
        return "Winner"
    elif score == -1:
        return "Loser"
    else:
        return "Tied"
    """
    # return (score == 1 and "Winner") or (score == -1 or "Loser") or "Tied"
	
# replace action seq
just_do_it = lambda f: f()
# Suppose f1, f2, f3 are actions
map(just_do_it, [f1, f2, f3])

## Iterators
def iterator_consumption():
    it = iter(range(100))
    67 in it  # => True
    # After the above two lines are executed, the iterator has been
    # run until it finds the 67, that is, until the point when next(it)
    # returned 68

    next(it)  # => 68
    37 in it  # => False, and in searching runs the iterator to exhaustion
    next(it)  # => raises StopIteration

# Module: itertools
import itertools
import operator
# permutations('ABCD', 2)	 	--> AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)	 	--> AB AC AD BC BD CD
# cycle('ABCD') --> A B C D A B C D ...
# starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000

# Linear Algebra
def dot_product(u, v):
    assert len(u) == len(v)
    return sum(itertools.starmap(operator.mul, zip(u, v)))

dot_product([1, 3, 5], [2, 4, 6])	
	
def transpose(m):
	return tuple(zip(*m))
	
# Lazy generation
def transpose_lazy(m):
    return zip(*m)

def matmul(m1, m2):
    return tuple(map(lambda row: tuple(dot_product(row, col) for col in transpose(m2)), m1))

def matmul_lazy(m1, m2):
    return map(lambda row: (dot_product(row, col) for col in transpose(m2)), m1)

#### Generator Expressions
# Generator Expressions vs. list comprehension
count = 1
a = 0
## Generators
def generate_triangles():
    n = 0
    total = 0
    while True:
        total += n
        n += 1
        yield total

def triangles_under(n):
    for triangle in generate_triangles():  # Lazy generation
        if triangle >= n:
            break
        print(triangle)

		
# Prime number and composite number
## Functions in Data Structures
def make_divisibility_test(n):
    return lambda m: m % n == 0

def generate_composites():
    tests = []
    i = 2
    while True:
        if not any(map(lambda test: test(i), tests)):
            tests.append(make_divisibility_test(i))
        # If not prime, then composite!
        else:
            yield i
        i += 1

def nth_composite(n):
    """ Pre: n > 0
    1 -> 4
    2 -> 6
    3 -> 8
    4 -> 9
    """
    g = generate_composites()
    for i in range(n - 1):
        next(g)
    return next(g)

# nth_composite(1000) # => 1197
	
# Nested Functions and Closures
def outer():
    def inner(a):
        return a
    return inner

f = outer()
print(f)  # <function outer.<locals>.inner at 0x1044b61e0>
f(10)  # => 10

f2 = outer()
print(f2)  # <function outer.<locals>.inner at 0x1044b6268> (Different from above!)
f2(11)  # => 11


# Closures
# Example 1
def make_adder(n):
    def add_n(m):  # Captures the outer variable `n` in a closure
        return m + n
    return add_n

add1 = make_adder(1)
print(add1)  # <function make_adder.<locals>.add_n at 0x103edf8c8>
add1(4)  # => 5
add1(5)  # => 6
add2 = make_adder(2)
print(add2)  # <function make_adder.<locals>.add_n at 0x103ecbf28>
add2(4)  # => 6
add2(5)  # => 7	
	
# Example 2
def foo(a, b, c=-1, *d, e=-2, f=-3, **g):
    def wraps():
        print(a, c, e, g)

w = foo(1, 2, 3, 4, 5, e=6, f=7, y=2, z=3)
list(map(lambda cell: cell.cell_contents, w.__closure__)) # ?? AttributeError: 'NoneType' object has no attribute '__closure__'
# = > [1, 3, 6, {'y': 2, 'z': 3}]		

# Example 3
def outer(l):
    def inner(n):
        return l * n
    return inner
    
l = [1, 2, 3]
f = outer(l)
print(f(3))  # => [1, 2, 3, 1, 2, 3, 1, 2, 3]

l.append(4)
print(f(3))  # => [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

#### Building Decorators
def debug(function):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return function(*args, **kwargs)
    return wrapper

def print_args(function):
    def wrapper(*args, **kwargs):
        # (1) You could do something here
		retval = function(*args, **kwargs)
		# (2) You could also do something here
		return retval
    return wrapper
	
	
@cache
def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else 1

fib(10)  # 55 (takes a moment to execute)
fib(10)  # 55 (returns immediately)
fib(100) # doesn't take forever
fib(400) # doesn't raise RuntimeError


'''Hint: You can set arbitrary attributes on a function (e.g. fn._cache). When you do so, 
the attribute-value pair also gets inserted into fn.__dict__. 
Take a look for yourself. Are the extra attributes and .__dict__ always in sync?
'''

# Dynamic Type Checker
@enforce_types
def foo(a: int, b: str) -> bool:
    if a == -1:
        return 'Gotcha!'
    return b[a] == 'X'

foo(3, 'abcXde')  # => True
foo(2, 'python')  # => False
foo(1, 4)  # prints "Invalid argument type for b: expected str, received int
foo(-1, '')  # prints "Invalid return type: expected bool, received str


	
	













