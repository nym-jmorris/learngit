'''
problem 2
fib = [1,2]

while fib[len(fib)-1]<4000000:
    fib.append(fib[len(fib)-2] + fib[len(fib)-1])

#print(fib)
#print(len(fib))
fib.remove(fib[len(fib)-1])
print(fib)

sum = 0

for f in fib:
    if f%2 == 0: sum+=f

print(sum)
'''

'''
problem 3
'''


'''# What is the largest prime factor of the number 600851475143 ?
n = 600851475143
#n = 4101
#n = 13195 

factors =[]

from math import sqrt
from math import floor

for i in range(1,floor(sqrt(n))+1):
    if n%i == 0:
        factors.append(i)
        factors.append(int(n/i))
factors.sort()
factors.pop(len(factors)-1)
factors.pop(0)
print('Factors: {}'.format(factors))

dead_factors = []
pfactors = []

for f in range(len(factors)-1,-1,-1):
    for g in range(0,len(factors)):
        if int(factors[f])%int(factors[g])==0 and int(factors[f]) != int(factors[g]):
            if int(factors[f]) not in dead_factors:
                dead_factors.append(int(factors[f]))

dead_factors.sort()
print('Dead factors: {}'.format(dead_factors))

for f in factors:
#    print(f)
#    print('{} is in dead: {}.'.format(f,int(f) in dead_factors))

    if int(f) not in dead_factors:
        pfactors.append(int(f))
        
print('Prime Factors: {}'.format(pfactors))'''

'''
problem 4



A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.




from math import floor

def isPalindrome(number):
    word = str(number)

    for i in range(0,floor(len(word)/2)+1):
        if word[i] != word[len(word)-i-1]:
            return False
    return True

maxPal = 0 

for i in range(100,1000):
    for j in range (100,1000):
        if isPalindrome(i*j):
            if i*j>maxPal: maxPal = i*j

print(maxPal)
'''

'''
problem 5


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# select the minimum prime factorization for each of 2..20
# 2**4, 3**2, 5,7,11,13,17,19

'''
problem 6

The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1+2+3+...+10)**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 - 385 = 2640.

Find the difference between the sum of the squares of 
the first one hundred natural numbers and the square of the sum.

sum_sqr = 0
sqr_sum = 0

for i in range(1,101):
    sum_sqr += i**2
    sqr_sum += i

sqr_sum = sqr_sum**2

print(sqr_sum - sum_sqr)'''

'''
problem 7


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import time
start_time = time.time()


primes = [2]
checked = [2]
composites = []

#print(len(primes))

pin = 3

while len(primes)<10001:
    for p in range(0,len(primes)-1):
        if pin%primes[p] == 0:
            composites.append(pin)
    # if pin in composites:
    #     continue
    if pin not in composites:
        primes.append(pin)
        if len(primes)%1000==0:
            print('Passing prime # {}'.format(len(primes)))
            print('Computation has taken {} seconds so far.'.format(time.time()-start_time))
            print('Prime density: {}'.format(len(primes)/pin))
    pin+=1
    composites = []

print('The {}th prime is {}.'.format(len(primes),primes[len(primes)-1]))
print('Computation has taken {} seconds so far.'.format(time.time()-start_time))
print('Prime density: {}'.format(len(primes)/primes[len(primes)-1]))