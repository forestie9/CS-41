def fizzbuzz(n):
    """Returns the sum of all numbers < n divisible by 3 or 5.
    This iterative approach will work really well, and if it gets the job done
    reasonably quickly, that's all we should ask for.
    If you want to write this in one line, the following will work:
        return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])
    However, that line isn't particularly Pythonic, since we're basically just
    compressing the syntax of an iterative for loop into one line - no big changes
    except for the use of `sum`.
    Another approach, as we'll learn about soon, is to use `filter`:
        return sum(filter(lambda i: i % 3 == 0 and i % 5 == 0, range(n)))
    However, in many ways, this isn't much different, since we're still
    specifying a function (admittedly, a `lambda` or anonymous function
    - which we'll learn about Week 4) over our range of numbers. For a
    job this simple, the iterative approach will suffice. """
    count = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    return count


def collatz_seq(n):
    seq = n
    while n != 1:
        if n%2 == 0:
            seq.append(n/2) # 'int' object has no attribute 'append', n //= 2, integer division
            n = n//2
        else:
            seq.append(3*n+1)
            n = 3*n+1
    return seq
'''
    arrow = '{}'.format('-'.join('>'))
    print(seq, sep=arrow)

Based on the solution:  A dictionary is used as a cache of previous
results, and since the dictionary passed in is mutable, our changes will reflect
in the caller. 
'''

def Fah_2_Cel():
    Fah = float(input("Temp F? "))
    # Cel = (Fah-32) * 5/9
    return (Fah-32) * 5/9


    

