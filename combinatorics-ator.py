
import sys
import time
from itertools import permutations

# ------------------------------------------------------------
# Utilities to print the percentage of work in progress
# ------------------------------------------------------------
class MyProgressPercentage():
    def __init__(self):
        self.now = 1
        self.tot = 0
        self.pre_string = ''

    def set(self, t, p_str):
        self.now = 0
        self.tot = t
        self.pre_string = p_str

    def step(self):
        self.now += 1
        # k = int(100*self.now/self.tot)
        k = round((100*self.now/self.tot),5)
        s = '\r' + self.pre_string + str(k) + '%'
        sys.stdout.write(s)
        sys.stdout.flush()


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# ------------------------------------------------------------
# Permutator with standard library for simple permutations
# ------------------------------------------------------------
class StandardSimplePermutator():
    def __init__(self):
        self.string = ''
        self.to_check = ''
        self.list_char = []
        self.length = 0 # length of string and any permutation
        self.num_p = 0 # number of all possible permutations
        self.start_time = None

    def set_values(self, input_string, check_string):
        self.string = input_string
        self.to_check = check_string
        for char in input_string:
            self.list_char.append(char)
        self.length = len(self.string)
        self.num_p = factorial(self.length)

    def check(self, temp):
        if  temp == self.to_check:
            print('\n<!> found "%s"' %self.to_check)
            return True

    def permutation(self):
        print('_________________________________')
        print('%% StandardPermutator %%')
        print('input string    : "%s"' %self.string)
        print('string to check : "%s"' %self.to_check)
        print('length string   :', self.length)
        print('num permutation :', self.num_p)

        progress = MyProgressPercentage()
        progress.set(self.num_p, 'permutating >_ ')

        self.start_time = time.time()
        for n, perm in enumerate(permutations(self.list_char)):
            to_string = ''
            for x in perm:
                to_string += x
            progress.step()
            if self.check(to_string):
                break
        else:
            print('\n<!> NOT found "%s"' %self.to_check)
        print('execution time: %s s\n' %(time.time() - self.start_time))

# ------------------------------------------------------------
# my Permutator home made for simple permutations
# ------------------------------------------------------------
class MySimplePermutator():
    def __init__(self):
        self.string = ''
        self.to_check = ''
        self.length = 0 # length of string and any permutation
        self.num_p = 0 # number of all possible permutations
        self.start_time = None
        self.progress = MyProgressPercentage()

    def set_values(self, input_string, check_string):
        self.string = input_string
        self.to_check = check_string
        self.length = len(self.string)
        self.num_p = factorial(self.length)

    def check(self, temp):
        if temp == self.to_check:
            print('\n<!> found "%s"' %self.to_check)
            return True

    def permute(self, pre, post):
        len_pre = len(pre)
        len_post = len(post)
        if len_post == 1:
            if len_pre == (self.length - 1):
                pre += post
                self.progress.step()
                if self.check(pre):
                    return False
                else:
                    return True
        else:
            for x in range(len_post):
                new_pre = pre + post[x]
                new_post = ''
                for y, z in enumerate(post):
                    if y != x:
                        new_post += z
                if not (self.permute(new_pre, new_post)):
                    return False
            return True

    def permutation(self):
        print('_________________________________')
        print('%% MyPermutator %%')
        print('input string    : "%s"' %self.string)
        print('string to check : "%s"' %self.to_check)
        print('length string   :', self.length)
        print('num permutation :', self.num_p)

        self.progress.set(self.num_p, 'permutating >_ ')

        self.start_time = time.time()
        if self.permute('', self.string):
            print('\n<!> NOT found "%s"' %self.to_check)
        print('execution time: %s s\n' % (time.time() - self.start_time))

input_string = input('Enter the string to permutate: ')
check_string = input('Enter the string to check: ')

# some example of input/check string
# input_string = '123'
# check_string = '321'
# input_string = '12333'
# check_string = '33312'
# input_string = '1234567890'
# check_string = '0987654312'

standard = StandardSimplePermutator()
standard.set_values(input_string, check_string)
standard.permutation()

mine = MySimplePermutator()
mine.set_values(input_string, check_string)
mine.permutation()
