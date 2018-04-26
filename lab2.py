''' Lab 3: Functions & Lab 4: Funtional programming


# Lab 3:
# Part 1: Exploring Arguments and Parameters
# Familiar Functions
def print_two(a,b):
    print("Arguments: {0} and {1}".format(a,b))

print_two(4,1)
print_two(a=4,b=1)
print_two(b=1,a=4)
# print_two(a=4,b=1,1) => invalid: positional argument follows keyword argument
# print_two(4,1,b=1) => invalid: print_two() got multiple values for argument 'b'

# Default Arguments
def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)	
	
keyword_args(5)
keyword_args(a=5)
keyword_args(5,2,c=4)
keyword_args(5,0,1)
keyword_args(5,2,d=8,c=4)	
keyword_args(5,2,[],5)
keyword_args(5,c=4)

# Exploring Variadic Arguments lists
def variadic(*args,**kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
	
variadic(2,3,5,7)
variadic(1,1,n=1)
variadic()
variadic(cs="computer science", pd="product design")
# variadic(cs="computer science", pd="product design", cs="CS") => invalid:  keyword argument repeated
variadic(5,8,k=1,swap=2)
variadic(8,*[3,4,5],k=1,**{'a':5, 'b':'x'})
variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'})
variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'}) # Positional: (3, 4, 5, 8, 4, 1), Keyword: {'k': 1, 'b': 'x', 'a': 5}
variadic({'a':5, 'b':'x'},*{'a':5, 'b':'x'},**{'a':5, 'b':'x'}) # Positional: ({'b': 'x', 'a': 5}, 'b', 'a'), Keyword: {'b': 'x', 'a': 5}
variadic({'a':5, 'b':'x'},**{'a':5, 'b':'x'})


# Putting it all together
def all_together(x,y,z=1,*nums,indent=True,spaces=4,**options):
    print("x:",x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)
	
# all_together(2) # missing 1 required positional argument: 'y'
all_together(2,5,7,8,indent=False) # => nums: (8,), spaces: keyword-only default parameters
# all_together() # => missing 2 required positional arguments: 'x' and 'y' 
all_together(dict(x=0,y=1),*range(10))
	# x: {'y': 1, 'x': 0}, y: 0, nums: (2, 3, 4, 5, 6, 7, 8, 9)
#all_together(*range(10),**dict(x=0,y=1)) # => got multiple values for argument 'y'
all_together([1,2],{3,4}) # => nums: (), options: {}
all_together(8,9,10,*[2,4,6],space=0,**{'a':5,'b':'x'}) # => spaces: 4, options: {'b': 'x', 'a': 5, 'space': 0}
all_together(8,9,10,*[2,4,6],space=0,**{'a':[4,5],'b':'x'}) # => options: {'b': 'x', 'a': [4, 5], 'space': 0}
all_together(8,9,10,*[2,4,6],*dict(z=1),space=0,**{'a':[4,5],'b':'x'}) # => nums: (2, 4, 6, 'z')


# Part 2: Writing functions
# speak_excitedly
def speak_excitedly(message,exc_number=1,cap=False):
    print(message.format(capitalize=cap,+'!',exc_number))
	
speak_excitedly("I love Python",1)
speak_excitedly("Keyword arguments are great",3)
speak_excitedly("I gues Java is okay...",0)
speak_excitedly("Let's go stanford",2,cap=True)
'''	
# average
def average(*number):
    if len(number) > 0
        return mean = map(mean,number)
	    # print(mean)
	else
		print("None")
		
average()
average(5)
average(6,8,9,11)

# challenge: make_table
def make_table(*parameters,**tablecontent):
	if parameters(0) == 'left'
	    sign = ':_<10'
	elif parameters(0) == 'right':
		sign = ':>10'
	else: # center
		sign = ':^10'
		
    print(sign.format(tablecontent{0}))
	
# Part 3: Function Nuances
# Return
def say_hello():
    print("Hello")

print(say_hello()) # => Hello

def echo(arg=None)
    print("arg:", arg)
    return arg	

print(echo()) # => arg: None, None
print(echo(5)) # => arg: 5, 5
print(echo("Hello")) # => arg: Hello, Hello

def drive(has_car):
    if not has_car
	    return "Oh no!"
	return 100
	
print(drive(False)) # => Oh no
print(drive(True)) # => 100

# Parameters and Object Reference
def reassign(arr):
    arr = [4,1]
    print("Inside reassign: arr = {}".format(arr))
	
def append_one(arr):
    arr.append(1)
    print("Inside append_one: arr = {}".format(arr))
	
l = [4]
print("Before reassign: arr = {}".format(l)) # => 4
reassign(l) # => 4, 1
print("After reassign: arr = {}".format(l)) # => 4	

l = [4]
print("Before append_one: arr = {}".format(l)) # => 4
append_one(l) # => 4, 1
print("After append_one: arr = {}".format(l)) # => 4, 1	

# Scope
	# case 1
x = 10
def foo():
	print("(Inside foo) x:", x)
	y = 5
	print('value:', x*y)
		
    
print("(outside foo) x:", x) # => 10
foo() # => 10, 50
print("(after foo) x:", x) # => 10

	# case 2
x = 10
def foo():
	x = 8 
	print("(Inside foo) x:", x)
	y = 5
	print('value:', x*y)
	
print("(outside foo) x:", x) # => 10
foo() # => 8, 40
print("(after foo) x:", x) # => 10

# UnboundLocalError
x = 10
def foo():
	print("(Inside foo) x:", x)
    x = 8 
	y = 5
	print('value:', x*y)
#??	
print("(outside foo) x:", x) # => 10
foo() # => 10, 40
print("(after foo) x:", x) # => 10

lst = [1,2,3]
def foo():
    lst.append(4)

foo() 
lst # => 1,2,3,4

lst = [1,2,3]
def foo():
    lst = lst + [4]
	
foo() # => UnboundLocalError, local variable 'lst' referenced before assignment

# Default Mutable Arguments 
x = 5

def square(num=x):
    return num * num
	
x = 6
square() # => 25, not 36: A function's default values are evaluated at the point of 
						# function definition in the defining scope. 
square(x) # => 36

def append_twice(a, lst=[]):
    lst.append(a)
	lst.append(a)
	return lst
	
print(append_twice(1, lst=[4])) # => [4,1,1]
print(append_twice(11, lst=[2,3,5,7])) # => [2,3,5,7,11,11]

print(append_twice(1)) # => [1,1]  (lst default value is [])
print(append_twice(2)) # => [1,1,2,2] (lst default value is [1,1])
print(append_twice(3)) # => [1,1,2,2,3,3] 

def append_twice(a, lst=None):
	'''If you don’t want the default value to be shared between subsequent calls, you can use a sentinel value (or a flag value)
	   as the default value (to signal that no keyword argument was explicitly provided by the caller).
	'''
    if lst is None:
        lst = []
    lst.append(a)
    lst.append(a)
    return lst
	
''' Sometimes, however, this odd keyword value initialization behavior can be desirable. 
	For example, it can be used as a cache that is modifiable and accessible by all invocations of a function:
'''	
def fib(n, cache={0: 1, 1: 1}):
    if n in cache: # Note: default value captures our base cases
	    return cache[n]
    out = fib(n-1) + fib(n-2)
	cache[n] = out
	return out
	
# Investigate Function Objects
'''
functionName.__xx__

xx: code, annotation, defaults, kwdefualts, doc

__module__ refers to the module that was active at the time the function was defined. 
Any functions defined in the interactive interpreter will have __module__ == '__main__', 
but, for example, encrypt_caesar.__module__ == 'crypto'.
'''




