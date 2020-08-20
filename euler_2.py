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

'''import time
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
    pin+=2
    composites = []

print('The {}th prime is {}.'.format(len(primes),primes[len(primes)-1]))
print('Computation has taken {} seconds so far.'.format(time.time()-start_time))
print('Prime density: {}'.format(len(primes)/primes[len(primes)-1]))'''



#problem 8

'''

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?


str_01 = '73167176531330624919225119674426574742355349194934'
str_02 = '96983520312774506326239578318016984801869478851843'
str_03 = '85861560789112949495459501737958331952853208805511'
str_04 = '12540698747158523863050715693290963295227443043557'
str_05 = '66896648950445244523161731856403098711121722383113'
str_06 = '62229893423380308135336276614282806444486645238749'
str_07 = '30358907296290491560440772390713810515859307960866'
str_08 = '70172427121883998797908792274921901699720888093776'
str_09 = '65727333001053367881220235421809751254540594752243'
str_10 = '52584907711670556013604839586446706324415722155397'
str_11 = '53697817977846174064955149290862569321978468622482'
str_12 = '83972241375657056057490261407972968652414535100474'
str_13 = '82166370484403199890008895243450658541227588666881'
str_14 = '16427171479924442928230863465674813919123162824586'
str_15 = '17866458359124566529476545682848912883142607690042'
str_16 = '24219022671055626321111109370544217506941658960408'
str_17 = '07198403850962455444362981230987879927244284909188'
str_18 = '84580156166097919133875499200524063689912560717606'
str_19 = '05886116467109405077541002256983155200055935729725'
str_20 = '71636269561882670428252483600823257530420752963450'

mega_str = str_01 + str_02 + str_03 + str_04 + str_05 + str_06 + str_07 + str_08 + str_09 + str_10 \
     + str_11 + str_12 + str_13 + str_14 + str_15 + str_16 + str_17 + str_18 + str_19 + str_20

maxp = 0

for i in range(0,len(mega_str)-13):
    p =   int(mega_str[i]) * int(mega_str[i+1]) *  int(mega_str[i+2]) *\
        int(mega_str[i+3]) * int(mega_str[i+4]) *  int(mega_str[i+5]) *\
        int(mega_str[i+6]) * int(mega_str[i+7]) *  int(mega_str[i+8]) *\
        int(mega_str[i+9]) * int(mega_str[i+10]) * int(mega_str[i+11]) *int( mega_str[i+12])
    if p > maxp:
        maxp = p
print(maxp)
'''

'''
problem 9


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

'''triplets = []

def findTriplet():
    for k in range(1,1000):
        for j in range(2,k):
            for i in range(1,j):
                if i+j+k == 1000:

                    if k**2 == i**2 + j**2:
                        
    #                    triplets.append([i,j,k])
                        print('Triplet of {}, sum of {}'.format([i,j,k],i+j+k))
                        print('Magic triplet found!')
                        print('Product is: {}'.format(i*j*k))
                        return([i,j,k])

triplet = findTriplet()
'''

# problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# answer = 142913828922

# old code here: ----

# import time
# start_time = time.time()

# primes = [2]
# composites = []

# #print(len(primes))

# pin = 3

# #200000: 73s
# #300000: 228s
# #500000: 

# maxn = 300000

# while primes[len(primes)-1]<maxn:
#     for p in range(0,len(primes)-1):
#         if pin % primes[p] == 0:
#             pin+=2
#             continue

#     primes.append(pin)
#     if len(primes)%1000==0:
#         print('\nPassing prime # {}'.format(len(primes)))
#         print('Prime value: {}'.format(pin))
#         print('Computation has taken {} seconds so far.'.format(time.time()-start_time))
#         print('Prime density: {}'.format(len(primes)/pin))
        
#     pin+=2

# print('\nFinished!')
# print('Last prime before {} is: {}'.format(maxn,primes[len(primes)-2]))
# print('Computation has taken {} seconds so far.'.format(time.time()-start_time))
# print('Prime density: {}'.format(len(primes)/pin))
# print('The sum of the first {} primes is: {}'.format(len(primes)-1,sum(primes)-primes[len(primes)-1]))

# print('The {}th prime is {}.'.format(len(primes),primes[len(primes)-1]))
# print('Computation has taken {} seconds so far.'.format(time.time()-start_time))
# print('Prime density: {}'.format(len(primes)/primes[len(primes)-1]))


# end old code---


# import time
# from math import floor

# time_start = time.time()

# nmax = 2000000

# primes = [2]

# candidates = [True for iter in range(nmax)]


# pin = 3

# def updateSieve(prime):
#     for i in range(0,floor(nmax/prime)):
#         candidates[i*prime] = False
#     return

# def checkPrime(candidate):
#     for p in primes:
#         if candidate % p == 0:
#             return
#     primes.append(candidate)
#     if len(primes)%1000 == 0:
#         print('\nPrime # {} found in {} seconds.'.format(len(primes),time.time()-time_start))
#         print('Prime value: {}'.format(candidate))
#         print('Prime density: {}'.format(len(primes)/candidate))

#     updateSieve(p)
#     return


# for i in range(2,nmax):
#     if candidates[i] == True:
#             checkPrime(i)

# time_end = time.time()

# print('There are {} primes below {}.'.format(len(primes),nmax))

# print('\nFinished!')
# print('Last prime before {} is: {}'.format(nmax,primes[len(primes)-1]))
# print('Computation has taken {} seconds so far.'.format(time.time()-time_start))
# print('Prime density: {}'.format(len(primes)/primes[len(primes)-1]))
# print('The sum of the first {} primes is: {}'.format(len(primes),sum(primes)))

import time
from math import floor

time_start = time.time()

nmax = 2000000

primes = []

candidates = [True for iter in range(nmax)]

def updateSieve(prime):
    for i in range(0,floor(nmax/prime)):
        candidates[i*prime] = False
        try:
            candidates[i*prime+prime] = False
        except IndexError:
            None
        if (nmax-1)%prime == 0:
            candidates[nmax-1] = False
        
    return


for i in range(2,nmax):
    if candidates[i] == True:
        primes.append(i)
        updateSieve(i)
        if len(primes)%1000 == 0:
            print('\nPrime # {} found in {} seconds.'.format(len(primes),time.time()-time_start))
            print('Prime value: {}'.format(i))
            print('Prime density: {}'.format(len(primes)/i))

time_end = time.time()

print('There are {} primes below {}.'.format(len(primes),nmax))

print('\nFinished!')
print('Last prime before {} is: {}'.format(nmax,primes[len(primes)-1]))
print('Computation has taken {} seconds so far.'.format(time.time()-time_start))
print('Prime density: {}'.format(len(primes)/primes[len(primes)-1]))
print('The sum of the first {} primes is: {}\n'.format(len(primes),sum(primes)))

# answer = 142913828922