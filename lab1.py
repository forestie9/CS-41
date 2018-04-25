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
    However, in many ways, this isn't much different, since we're still specifying a
    function (admittedly, a `lambda` or anonymous function - which we'll learn about Week 4)
    over our range of numbers.
    For a job this simple, the iterative approach will suffice.
    """
    count = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    return count

def 
