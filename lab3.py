# Lab3: Functional Programming
# 4/27/2018

#### Functional Tools

# Lambdas
# Map
map(int,['12','-2','0'])
map(len,['hello','world'])
map(string.inverse,['hello','world'])
map(lambda x:[x,x*2,x*3],range(2,6)]
map(lambda x: x(0)*x(1),zip(range(2,5),range(3,9,2)))

# Filter
filter(lambda a: a(:end-1),['12','-2','0'])
filter(lambda a: a(1),['hello','world'])
filter(lambda a: a/3==0 and a/5==0,range(20))

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
max(words, key=len)  # 'cabbage' ... Why not 'bananas'? original order
min(words, key=lambda s: s[1::2])  # What will this value be? bananas, 'cabbage'[1::2] => abg

def two_best(words):
	'''return the two words with the highest alphanumeric score of uppercase letters
	'''
	return map(lambda l: max(sum(l, key=uppercase)), words)
	
list(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))

#### Purely Functional Programming
output = map(lambda s: (s==1 and print("Winner")) or (s==-1 and print("Loser")) or (s==0 and print("Tied")),score)

# replace action seq
just_do_it = lambda f: f()
# Suppose f1, f2, f3 are actions
map(just_do_it, [f1, f2, f3])

#### Iterators
# Iterator Consumption
it = iter(range(100))
next(it) # => 100
37 in it # => True
next(it) # => 101

# Module: itertools
import itertools
import operator
# permutations('ABCD', 2)	 	--> AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)	 	--> AB AC AD BC BD CD
# cycle('ABCD') --> A B C D A B C D ...
# starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000


def dot_product(u, v):
	list(itertools.starmap(operator.add,(itertools.accumulate([u,v], operator.mul))))

dot_product([1, 3, 5], [2, 4, 6])	
	
def transpose(m):
	pass
	
# Lazy generation


#### Generator Expressions
# Generator Expressions vs. list comprehension
count = 1
a = 0
def generate_triangles():
	'''Write a infinite generator that successively yields the triangle numbers 0, 1, 3, 6, 10, ...
	'''
	while count < 100: # UnboundLocalError: local variable 'count' referenced before assignment
		a.append(a + count)
		count += 1
	print(a)

# Prime number and composite number
	
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
list(map(lambda cell: cell.cell_contents, w.__closure__)) # AttributeError: 'NoneType' object has no attribute '__closure__'
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














