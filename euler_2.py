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

'''import time
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

'''

#problem 11
# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48


# What is the greatest product of four adjacent numbers in the same direction 
# (up, down, left, right, or diagonally) in the 20×20 grid?

'''
row_01 = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08'
row_02 = '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00'
row_03 = '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65'
row_04 = '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91'
row_05 = '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80'
row_06 = '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50'
row_07 = '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70'
row_08 = '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21'
row_09 = '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72'
row_10 = '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95'
row_11 = '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92'
row_12 = '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57'
row_13 = '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58'
row_14 = '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40'
row_15 = '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66'
row_16 = '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69'
row_17 = '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36'
row_18 = '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16'
row_19 = '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54'
row_20 = '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

w , h = 20,20
cells = [[0 for x in range(w)] for y in range(h)] 
for j in range(0,20):
    cells[0][j] = int(row_01[3*j:3*j+2])
    cells[1][j] = int(row_02[3*j:3*j+2])
    cells[2][j] = int(row_03[3*j:3*j+2])
    cells[3][j] = int(row_04[3*j:3*j+2])
    cells[4][j] = int(row_05[3*j:3*j+2])
    cells[5][j] = int(row_06[3*j:3*j+2])
    cells[6][j] = int(row_07[3*j:3*j+2])
    cells[7][j] = int(row_08[3*j:3*j+2])
    cells[8][j] = int(row_09[3*j:3*j+2])
    cells[9][j] = int(row_10[3*j:3*j+2])
    cells[10][j] = int(row_11[3*j:3*j+2])
    cells[11][j] = int(row_12[3*j:3*j+2])
    cells[12][j] = int(row_13[3*j:3*j+2])
    cells[13][j] = int(row_14[3*j:3*j+2])
    cells[14][j] = int(row_15[3*j:3*j+2])
    cells[15][j] = int(row_16[3*j:3*j+2])
    cells[16][j] = int(row_17[3*j:3*j+2])
    cells[17][j] = int(row_18[3*j:3*j+2])
    cells[18][j] = int(row_19[3*j:3*j+2])
    cells[19][j] = int(row_20[3*j:3*j+2])
    
maxp = 0

high = 20
wide = 20

#vertical
for j in range(0,high-4):    
    for i in range(0,wide):
    
        if cells[i][j] * cells[i][j+1] \
            * cells[i][j+2] * cells[i][j+3] > maxp:
            maxp = cells[i][j] * cells[i][j+1] \
            * cells[i][j+2] * cells[i][j+3] 

#horizontal
for i in range(0,wide-4):
    for j in range(0,high):
        if cells[i][j] * cells[i+1][j] \
            * cells[i+2][j] * cells[i+3][j] > maxp:
            maxp = cells[i][j] * cells[i+1][j] \
            * cells[i+2][j] * cells[i+3][j] 

#diagonal negative slope
for i in range(0,wide-4):
    for j in range(0,high-4):
        if cells[i][j] * cells[i+1][j+1] \
            * cells[i+2][j+2] * cells[i+3][j+3] > maxp:
            maxp = cells[i][j] * cells[i+1][j+1] \
            * cells[i+2][j+2] * cells[i+3][j+3] 

#diagonal positive slope
for i in range(0,wide-4):
    for j in range(3,high):
        if cells[i][j] * cells[i+1][j-1] \
            * cells[i+2][j-2] * cells[i+3][j-3] > maxp:
            maxp = cells[i][j] * cells[i+1][j-1] \
            * cells[i+2][j-2] * cells[i+3][j-3] 

print(maxp)
'''

# problem 12

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

'''
from math import sqrt
from math import floor

def buildTri(number):
    triangle = 0
    for i in range(1,number+1):
        triangle+=i
    return triangle

def factorize(number):
    factors = []
    for i in range(1,floor(sqrt(number))+1):
        if number % i == 0:
            factors.append(i)
            factors.append(int(number / i))
    return factors

# print(buildTri(41))
# print(factorize(buildTri(41)))
factors =[]

limit = 500

i = 1
while len(factors) < limit:
    number = buildTri(i)
    factors = factorize(number)
#    print(str(i)+': Length: {:>4}: {:>10}: {}'.fo      rmat(len(factors),number,factors))
    print('Triangle number {:>4} is {:>4}.  It has {:>4} factors.'.format(i,number,len(factors)))
    i+=1
'''
#problem 13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# with 100 digits, the impact from the rightmost column will at most propagate to the third rightmost column.
# Looking at the leftmost 13 columns is sufficient.

'''
str_001='37107287533902102798797998220837590246510135740250'
str_002='46376937677490009712648124896970078050417018260538'
str_003='74324986199524741059474233309513058123726617309629'
str_004='91942213363574161572522430563301811072406154908250'
str_005='23067588207539346171171980310421047513778063246676'
str_006='89261670696623633820136378418383684178734361726757'
str_007='28112879812849979408065481931592621691275889832738'
str_008='44274228917432520321923589422876796487670272189318'
str_009='47451445736001306439091167216856844588711603153276'
str_010='70386486105843025439939619828917593665686757934951'
str_011='62176457141856560629502157223196586755079324193331'
str_012='64906352462741904929101432445813822663347944758178'
str_013='92575867718337217661963751590579239728245598838407'
str_014='58203565325359399008402633568948830189458628227828'
str_015='80181199384826282014278194139940567587151170094390'
str_016='35398664372827112653829987240784473053190104293586'
str_017='86515506006295864861532075273371959191420517255829'
str_018='71693888707715466499115593487603532921714970056938'
str_019='54370070576826684624621495650076471787294438377604'
str_020='53282654108756828443191190634694037855217779295145'
str_021='36123272525000296071075082563815656710885258350721'
str_022='45876576172410976447339110607218265236877223636045'
str_023='17423706905851860660448207621209813287860733969412'
str_024='81142660418086830619328460811191061556940512689692'
str_025='51934325451728388641918047049293215058642563049483'
str_026='62467221648435076201727918039944693004732956340691'
str_027='15732444386908125794514089057706229429197107928209'
str_028='55037687525678773091862540744969844508330393682126'
str_029='18336384825330154686196124348767681297534375946515'
str_030='80386287592878490201521685554828717201219257766954'
str_031='78182833757993103614740356856449095527097864797581'
str_032='16726320100436897842553539920931837441497806860984'
str_033='48403098129077791799088218795327364475675590848030'
str_034='87086987551392711854517078544161852424320693150332'
str_035='59959406895756536782107074926966537676326235447210'
str_036='69793950679652694742597709739166693763042633987085'
str_037='41052684708299085211399427365734116182760315001271'
str_038='65378607361501080857009149939512557028198746004375'
str_039='35829035317434717326932123578154982629742552737307'
str_040='94953759765105305946966067683156574377167401875275'
str_041='88902802571733229619176668713819931811048770190271'
str_042='25267680276078003013678680992525463401061632866526'
str_043='36270218540497705585629946580636237993140746255962'
str_044='24074486908231174977792365466257246923322810917141'
str_045='91430288197103288597806669760892938638285025333403'
str_046='34413065578016127815921815005561868836468420090470'
str_047='23053081172816430487623791969842487255036638784583'
str_048='11487696932154902810424020138335124462181441773470'
str_049='63783299490636259666498587618221225225512486764533'
str_050='67720186971698544312419572409913959008952310058822'
str_051='95548255300263520781532296796249481641953868218774'
str_052='76085327132285723110424803456124867697064507995236'
str_053='37774242535411291684276865538926205024910326572967'
str_054='23701913275725675285653248258265463092207058596522'
str_055='29798860272258331913126375147341994889534765745501'
str_056='18495701454879288984856827726077713721403798879715'
str_057='38298203783031473527721580348144513491373226651381'
str_058='34829543829199918180278916522431027392251122869539'
str_059='40957953066405232632538044100059654939159879593635'
str_060='29746152185502371307642255121183693803580388584903'
str_061='41698116222072977186158236678424689157993532961922'
str_062='62467957194401269043877107275048102390895523597457'
str_063='23189706772547915061505504953922979530901129967519'
str_064='86188088225875314529584099251203829009407770775672'
str_065='11306739708304724483816533873502340845647058077308'
str_066='82959174767140363198008187129011875491310547126581'
str_067='97623331044818386269515456334926366572897563400500'
str_068='42846280183517070527831839425882145521227251250327'
str_069='55121603546981200581762165212827652751691296897789'
str_070='32238195734329339946437501907836945765883352399886'
str_071='75506164965184775180738168837861091527357929701337'
str_072='62177842752192623401942399639168044983993173312731'
str_073='32924185707147349566916674687634660915035914677504'
str_074='99518671430235219628894890102423325116913619626622'
str_075='73267460800591547471830798392868535206946944540724'
str_076='76841822524674417161514036427982273348055556214818'
str_077='97142617910342598647204516893989422179826088076852'
str_078='87783646182799346313767754307809363333018982642090'
str_079='10848802521674670883215120185883543223812876952786'
str_080='71329612474782464538636993009049310363619763878039'
str_081='62184073572399794223406235393808339651327408011116'
str_082='66627891981488087797941876876144230030984490851411'
str_083='60661826293682836764744779239180335110989069790714'
str_084='85786944089552990653640447425576083659976645795096'
str_085='66024396409905389607120198219976047599490197230297'
str_086='64913982680032973156037120041377903785566085089252'
str_087='16730939319872750275468906903707539413042652315011'
str_088='94809377245048795150954100921645863754710598436791'
str_089='78639167021187492431995700641917969777599028300699'
str_090='15368713711936614952811305876380278410754449733078'
str_091='40789923115535562561142322423255033685442488917353'
str_092='44889911501440648020369068063960672322193204149535'
str_093='41503128880339536053299340368006977710650566631954'
str_094='81234880673210146739058568557934581403627822703280'
str_095='82616570773948327592232845941706525094512325230608'
str_096='22918802058777319719839450180888072429661980811197'
str_097='77158542502016545090413245809786882778948721859617'
str_098='72107838435069186155435662884062257473692284509516'
str_099='20849603980134001723930671666823555245252804609722'
str_100='53503534226472524250874054075591789781264330331690'

strings = [str_001,str_002,str_003,str_004,str_005,str_006,str_007,str_008,str_009,str_010,\
    str_011,str_012,str_013,str_014,str_015,str_016,str_017,str_018,str_019,str_020, \
        str_021,str_022,str_023,str_024,str_025,str_026,str_027,str_028,str_029,str_030, \
            str_031,str_032,str_033,str_034,str_035,str_036,str_037,str_038,str_039,str_040, \
                str_041,str_042,str_043,str_044,str_045,str_046,str_047,str_048,str_049,str_050, \
                    str_051,str_052,str_053,str_054,str_055,str_056,str_057,str_058,str_059,str_060, \
                        str_061,str_062,str_063,str_064,str_065,str_066,str_067,str_068,str_069,str_070, \
                            str_071,str_072,str_073,str_074,str_075,str_076,str_077,str_078,str_079,str_080, \
                                str_081,str_082,str_083,str_084,str_085,str_086,str_087,str_088,str_089,str_090, \
                                    str_091,str_092,str_093,str_094,str_095,str_096,str_097,str_098,str_099,str_100]

short_numbs =[]

for string in strings:
    short_numbs.append(int(string[0:13]))
print(str(sum(short_numbs))[0:10])

'''

#problem 14


# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

'''
import time
time_start = time.time()

def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return 3 * number + 1

point = 1000

maxlen = 0
maxnum = 0

for j in range(2,1000000):
#n = 13
    n = j
    point = n
    chain = []

    while point != 1:
        point = collatz(point)
        chain.append(point)
    #print('\n {:>6} complete. Chainlength of {:>3}.'.format(j,len(chain)))
    if len(chain)>maxlen:
        maxlen = len(chain)
        maxnum = j


print('The starting number with the longest chain is {}, with a chainlength of {}'.format(maxnum,maxlen))
print('Time elapsed: {:06.2f} seconds'.format(time.time()-time_start))
'''

# problem 17


# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.
'''
from math import floor

def numParse(number):
    part2 = ''
    part2 = ''
    part1 = ''
    
    ones = 0
    teens = 0
    tens = 0
    hundreds = 0

    if number >= 100:
        hundreds = int(floor(number/100))
    if number - 100 * hundreds >= 20:
        tens = int(floor((number - hundreds * 100)/10))
    if number - 100 * hundreds >= 10 and number - 100 * hundreds < 20:
        teens = number - 100 * hundreds
    if number - 100 * hundreds - 10 * tens > 0 and teens ==0:
        ones = number - 100 * hundreds - 10 * tens 
    


    if hundreds == 0:
        part1 = ''
    elif hundreds == 1:
        part1 = 'one'
    elif hundreds == 2:
        part1 = 'two'
    elif hundreds == 3:
        part1 = 'three'
    elif hundreds == 4:
        part1 = 'four'
    elif hundreds == 5:
        part1 = 'five'
    elif hundreds == 6:
        part1 = 'six'
    elif hundreds == 7:
        part1 = 'seven'
    elif hundreds == 8:
        part1 = 'eight'
    else: part1 = 'nine'

    if part1 == '':
        part1 = ''
    else: part1 = part1 + 'hundred'

    if tens == 0 and teens == 0 and ones == 0:
        part2 = ''
        part2 = ''
    elif teens != 0:
        if teens == 10:
            part2 = 'ten'
        elif teens == 11:
            part2 = 'eleven'
        elif teens == 12:
            part2 = 'twelve'
        elif teens == 13:
            part2 = 'thirteen'
        elif teens == 14:
            part2 = 'fourteen'
        elif teens == 15:
            part2 = 'fifteen'            
        elif teens == 16:
            part2 = 'sixteen'
        elif teens == 17:
            part2 = 'seventeen'
        elif teens == 18:
            part2 = 'eighteen'            
        else:part2 = 'nineteen'
    else:
        if tens ==2:
            part2 = 'twenty'
        elif tens ==3:
            part2 = 'thirty'
        elif tens ==4:
            part2 = 'forty'
        elif tens ==5:
            part2 = 'fifty'
        elif tens ==6:
            part2 = 'sixty'
        elif tens ==7:
            part2 = 'seventy'
        elif tens ==8:
            part2 = 'eighty'
        elif tens ==9:
            part2 = 'ninety'
        else: part2 =''

    if ones ==0:
        part3 = ''
    else:
        if ones ==1:
            part3 = 'one'
        elif ones ==2:
            part3 = 'two'
        elif ones ==3:
            part3 = 'three'
        elif ones ==4:
            part3 = 'four'
        elif ones ==5:
            part3 = 'five'
        elif ones ==6:
            part3 = 'six'
        elif ones ==7:
            part3 = 'seven'                                                
        elif ones ==8:
            part3 = 'eight'
        else:
            part3 = 'nine'
    
    output = ''

    if part1 != '' and (part2 != '' or part3 !=''):
        output = part1+'and'+part2+part3
    else: output = part1+part2+part3

    #print(output)

    #print(len(part1)+len(part2)+len(part3))

    #print(len(output))
    #longword += len(output)
    return output, len(output)

    #print('{} breaks down into {} hundreds, {} tens, {} teens and {} ones.'.format(number,hundreds,tens,teens,ones))

longword = 0



for i in range(1,1000):
    word = numParse(i)
#    print('{:>3}: {:>20}'.format(str(i),word[0]))
    longword += word[1]

# one thousand == 11 characters...
print(longword+11)
'''


#problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

'''
def factorial(n):
    f = 1
    for i in range(2,n+1):
        f = f*i
    return f

def sumDigits(number):
    nLength = len(str(number))
    nSum = 0

    for i in range(0,nLength):
        nSum += int(str(number)[i])
    return nSum

print(factorial(100))
print(sumDigits(factorial(100)))
'''

#problem 21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
'''
from math import sqrt
from math import floor

def getFactors(n):
    factors =[]
    for i in range(1,floor(sqrt(n))+1):
        if n%i ==0:
            factors.append(i)
            factors.append(int(n/i))
    factors = list(dict.fromkeys(factors))
    factors.sort()
    factors.pop(len(factors)-1)
    return factors

def dn(factors):
    return sum(factors)

amicable =[]

for i in range(2,10000):
    f = getFactors(i)
    fsum = dn(f)
    #print('{}: d(n) = {} | {}'.format(i,fsum,f))

    if fsum == 1:
        continue
    if i == dn(getFactors(fsum)) and i != fsum:
        amicable.append(i)


for a in amicable:
    gf = getFactors(a)
    dngf = dn(gf)
    print('dn({:4d})=   {:4d} | Factors: {}'.format(a,dngf,gf))
    
print(sum(amicable))
'''


#problem 22


# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this 
# value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

'''
import csv

import string


with open('p022_names.txt', newline='') as f:
    reader = csv.reader(f)
    
    data = list(reader)

nameList = data[0]

nameList.sort()


namesum = 0
position = 0
namescore = 0

for i in range (0,len(nameList)):
    namesum = 0
    position += 1
    for j in range(0,len(nameList[i])):
        namesum += (string.ascii_uppercase.index(nameList[i][j]))+1
    #print('Name = {:>10}, position = {}, nameScore = {}, combinedScore = {}, running score = {}.'.format(nameList[i],position,namesum,position*namesum,namescore + namesum*position))
    namescore += namesum * position
    
print(namescore)
'''

#problem 25


# The Fibonacci sequence is defined by the recurrence relation:

#     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

# Hence the first 12 terms will be:

#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144

# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

'''
def fib(n):
    if n ==0:
        return 1
    elif n ==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

flen = 1
i = 2
limit = 3
while flen < limit:
    fibi = fib(i)
    flen = len(str(fibi))
    i += 1
print('First term with more than {} digits is {}. The fibonacci number is {}'.format(limit-1,i,fibi))
'''

#problem 26

# A unit fraction contains 1 in the numerator. 
# The decimal representation of the unit fractions with denominators 2 to 10 are given:

#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1 

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
from math import floor

d = 1000
d = 10

# floating point math will ruin the party.
# here's 1/3: 0.33333333333333331482962

digits= [0 for iter in range(d)]
#print(digits)

def decimalize(num,denom):
    i = 0
    while num < denom:
        num = num * 10
        i+=1
    dvnd = int(floor(num/denom))
    rmdr = num%denom

    return i,dvnd,rmdr
'''
#problem 30


# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#     1634 = 14 + 64 + 34 + 44
#     8208 = 84 + 24 + 04 + 84
#     9474 = 94 + 44 + 74 + 44

# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# how to set an upper limit for this?
'''
from math import floor

fifths =[]

numlen = len(str(i))

'''

# problem 31

# In the United Kingdom the currency is made up of pound (£) and pence (p). 
# There are eight coins in general circulation:

#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

# It is possible to make £2 in the following way:

#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?

'''
ways = 0

needed = 200

for a in range(0,int(needed/100) + 1):
    for b in range(0,int((needed-a*100)/50)+1):
        for c in range(0,int((needed-a*100-b*50)/20)+1):
            for d in range(0,int((needed-a*100-b*50-c*20)/10)+1):
                for e in range(0,int((needed-a*100-b*50-c*20-d*10)/5)+1):
                    for f in range(0,int((needed-a*100-b*50-c*20-d*10-e*5)/2)+1):
                        for g in range(0,int((needed-a*100-b*50-c*20-d*10-e*5-f*2)/1)+1):
                            if 100*a + 50*b + 20*c + 10*d + 5*e + 2*f + 1*g == 200:
                                print('1£: {}, 50p: {} 20p: {} 10p: {} 5p:{} 2p: {} 1p: {}'.format(a,b,c,d,e,f,g))
                                ways+=1
print(ways+1) # +1 for the 2£ coin.
'''


#Problem 35

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

import time

from math import floor

print('Starting...')

time_start = time.time()

nmax = 1000000

primes = []

candidates = [True for iter in range(nmax)]

def updateSieve(prime):
    for i in range(0,floor(nmax/prime)):
        candidates[i*prime] = False
        try:
            candidates[i*prime+prime] = False
        except IndexError:
            None       
    return

print('Generating primes...({})'.format(time.time()-time_start))

for i in range(2,nmax):
    if candidates[i] == True:
        primes.append(i)
        updateSieve(i)

print('Primes generated...({})'.format(time.time()-time_start))

# rotate primes
# check for rotation in list of primes...

def checkPrime(candidate):
    if candidate in primes:
        return True
    else: return False

def rotatePrime(prime,i):
    pstr = str(prime)
    pr = pstr[-len(pstr)+i:]+pstr[0:i]
    return int(pr)

#test = 456

#print(rotatePrime(456,1))
cprimes = []

print('Starting the rotations...')
for prime in primes:
    loops = 0
    primetest = []
    # the "in" is too slow...
    while loops < len(str(prime)):
        tempprime = rotatePrime(prime,loops)
        # if tempprime %2 ==0:
        #     continue
        if tempprime in primes: 
            isPrime = 1 
        else: 
            isPrime = 0
            continue
            #loops  = len(str(prime))


        print('{} tested and result is {}'.format(prime,isPrime))
        primetest.append(isPrime)
        loops +=1
    if sum(primetest) == len(str(prime)):
        cprimes.append(prime)

print(cprimes)
print('There are {} circular primes below 1 million.'.format(len(cprimes)))
print('It only took {} seconds to figure this out.'.format(time.time()-time_start))
