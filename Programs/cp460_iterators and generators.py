#--------------------------
# Python Iterators & Generators
#--------------------------

import math
import itertools

#-----------------------
# is prime function
#-----------------------
def is_prime(n):
    if n > 1:
        if n ==2:
            return True
        if n %2 == 0:
            return False
        for i in range(3,int(math.sqrt(n)+1),2):
            if n%i == 0:
                return False
        return True
    return False
    
#-----------------------
# List Comprehension
#-----------------------
def what_is_list_comprehension():
    print("List Comprehension is a compact method to create and manipulate lists in Python")
    print("Syntax: <list_variable> = [<expression> for <item> in <list> if <conditional_statement>]")
    print()

    print('Example 1: Generate a list containing all odd numbers between 0 and 50')
    #Regular Method
    list1 = []
    for i in range(50):
        if i%2 == 1:
            list1.append(i)
    print('Regular method:\t\t',list1)
    #list comprehension
    list2 = [i for i in range(50) if i%2 == 1]
    print('List Comprehension:\t',list2)
    print()
    
    print('Example 2: Craete a new list from list of words after conversion to upper case')
    wordList = ['ant', 'bed', 'car', 'dip']
    #Regular Method
    wordList1 = []
    for word in wordList:
        wordList1+=[word.upper()]
    print('Regular method:\t\t',wordList1)
    #list comprehension
    wordList2 = [word.upper() for word in wordList]
    print('List Comprehension:\t',wordList2)
    print()

    print('Example 3: Create a list of words that start with j and end with x in engmix.txt')
    #regular method
    xList1 = []
    inFile = open('engmix.txt','r')
    for line in inFile:
        if line[-2] == 'x' and line[0] == 'j':
            xList1+=[line.strip()]
    inFile.close()
    print('Regular method:\t\t',xList1)
    #list comprehension
    inFile = open('engmix.txt','r')
    xList2 = [line.strip() for line in inFile if line[-2] == 'x' and line[0] == 'j']
    inFile.close()
    print('List Comprehension:\t',xList2)
    return


#-----------------------
# Iterable Objects
#-----------------------
def what_is_iterable():
    print("Lists, tuples, sets, strings and dictionaries are built-in python iterable objects")
    print("In simple terms: containers that can hold countable items which you can iterate through")
    print("you can use a 'for' statement to traverse an iterable object")
    print()
    
    l = [10,20,30]
    print('l = ',l)
    print('Using for statement to iterate list "l":')
    for i in l:
        print(i)
    print()
    
    print('Using for statement to iterate tuple "t":')
    t = (30,40,50)
    print('t = ',t)
    for i in t:
        print(i)
    print()

    print('Using for statement to iterate string "s":')
    s = 'luck'
    print('s = ',s)
    for i in s:
        print(i)
    print()

    print('Using for statement to iterate dictionary "d":')
    d = {'P':'Python', 'J':'Java', 'H':'HTML'}
    print('d = ',d)
    for i in d:
        print(i)
    print()

    # Reminder: in sets elements are not in order. 
    print('Using for statement to iterate set "e":')
    e = {100,300,200,400}
    print('e = ',e)
    for i in e:
        print(i)
    print()

    print('Remember: lists, dictionaries and sets are mutable, but tuples and strings are immutable, i.e. you can not change them')
    print()
    return


#-----------------------
# Iterable Objects
#-----------------------
def what_is_iterator():
    print("An interator is an object that you can use to iterate/traverse through an itereable object")
    print("More technically: An object that implements the iterable protocol, i.e. iter() and next()")
    print("You can get an iterator from an iterable object by calling the iter() function")
    print()

    l = [10,20,30]
    print('l = ',l)
    print('Creating l_iterator for list "l":')
    l_iterator = iter(l)
    print('Calling next twice on l_iterator:')
    print(next(l_iterator))
    print(next(l_iterator))
    print()
    
    t = (30,40,50)
    print('t = ',t)
    print('Creating t_iterator for tuple "t":')
    t_iterator = iter(t)
    print('Calling next twice on t_iterator:')
    print(next(t_iterator))
    print(next(t_iterator))
    print()

    s = 'luck'
    print('s = ',s)
    print('Creating s_iterator for string "s":')
    s_iterator = iter(s)
    print('Calling next twice on s_iterator:')
    print(next(s_iterator))
    print(next(s_iterator))
    print()

    d = {'P':'Python', 'J':'Java', 'H':'HTML'}
    print('d = ',d)
    print('Creating d_iterator for dictionary "d":')
    d_iterator = iter(d)
    print('Calling next twice on d_iterator:')
    print(next(d_iterator))
    print(next(d_iterator))
    print()

    e = {100,300,200,400}
    print('e = ',e)
    print('Creating e_iterator for set "e":')
    e_iterator = iter(e)
    print('Calling next twice on e_iterator:')
    print(next(e_iterator))
    print(next(e_iterator))
    print()

    print('Note 1: when you call the for function on an iterable object, an iterator is created through iter() then next() is invoked in every loop')
    print('Note 2: The open function returns a file object which is an iterator.')
    print()
    return

#-----------------------
# Generator Objects
#-----------------------
def what_is_generator():
    print("A generator is a function-like object in python that behaves like an iterator")
    print('Actually, it does create a Python iterator; therefore, next() can be used on it')
    print("Unlike a function that complete computations and returns a full list, a generator yields only one element at a time")
    print("This is useful to save memory and speed computations for complex or large objects")
    print("A generator is defined through (def), uses one or multiple (yield) and returns an iterator")
    print()

    print('Example 1: Odd numbers between 0 and n')
    def get_odds(n):
        for i in range(n):
            if i%2 == 1:
                yield i
        return
    oddGen = get_odds(50)
    print('oddGen = ',oddGen)
    print('next(oddGen) = ',next(oddGen))
    print('next(oddGen) = ',next(oddGen))
    print('[next(oddGen) for i in range(20)] = ',[next(oddGen) for i in range(20)])
    print('for i in oddGen\n   print(i):')
    for i in oddGen:
        print(i)
    print()

    print('Example 2: Get the nth prime number')
    
    #get all primes between x and y
    def get_primes(x,y):
        for i in range(x,y+1):
            if is_prime(i):
                yield i
        return
    #get nth prime:
    cap = 1000000000
    primeGen = get_primes(1,cap)
    print('Get 6th prime number:')
    prime = 1
    for i in range(6):
        prime = next(primeGen)
    print('Get 6th prime number = ',prime)
    
    for i in range(100-6):
        prime = next(primeGen)
    print('Get the 100th prime number = ',prime)

    for i in range(1000-100):
        prime = next(primeGen)
    print('Get the 1000th prime number = ',prime)
    print('you may verify answers at: https://primes.utm.edu/nthprime/index.php#nth')
    print()
    return            
    

#-----------------------
# Generator Expressions
#-----------------------
def what_is_generator_expression():
    print("A generator expression is like a list comprehension except that it returns a generator")
    print("Syntax: <generator_variable> = (<expression> for <item> in <list> if <conditional_statement>)")
    print()

    print('Example 1: Get primes between x and y')
    x = 100
    y = 200
    print('x = ',x,'y =',y)
    # this is similar to the get_primes(x,y) function created above
    primeGen = (i for i in range(x,y+1) if is_prime(i))
    print('primeGen = ',primeGen)
    for num in primeGen:
        print(num,end=',')
    print()

    print('Example 2: Get all words that start with j and end with x in engmix.txt')
    # this is similar to the get_primes(x,y) function created above
    inFile = open('engmix.txt','r')
    wordGen = (line.strip() for line in inFile if line[-2] == 'x' and line[0] == 'j')
    for word in wordGen:
        print(word,end=',')
    inFile.close()
    print()
    return


#-----------------------------------------------------------
# Generate string permutations
#-----------------------------------------------------------
# method 1: list (memory inefficient)
def get_string_perm1(s):
    # method 1: built-in
    permList = list(itertools.permutations(s))
    for i in range(len(permList)):
        permList[i] = "".join(permList[i])
    return permList

# method 2: generator
def get_string_perm2(s):
    return (itertools.permutations(s))

def test_string_perm2():
    s = 'hello'
    print('s =',s)
    permGen = get_string_perm2(s)
    for i in permGen:
        print("".join(i))
