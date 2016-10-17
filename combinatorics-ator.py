
import sys
import time
from itertools import permutations


# Utility to print the percentage of work in progress
# ------------------------------------------------------------

class ProgressPercentage():
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
        k = round((100*self.now/self.tot),2)
        s = '\r' + self.pre_string + str(k) + '%'
        sys.stdout.write(s)
        sys.stdout.flush()


# Utilities
# ------------------------------------------------------------

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def compare_string(target, temp):
    if  temp == target:
        print('\n<!> found "%s"' %target)
        return True


# Permutator with standard library for simple permutations
# ------------------------------------------------------------

class StandardPermutator():
    def __init__(self):
        self.string = ''
        self.to_check = ''
        self.list_char = []
        self.string_length = 0  # length of string
        self.tot_p = 0          # number of permutations
        self.start_time = None
        self.w2d = 0            # helper, what to do?
        self.progress = None
        self.writer = None

    def set_values(self, input_string, check_string, w2d):
        self.string = input_string
        self.to_check = check_string
        for char in input_string:
            self.list_char.append(char)
        self.string_length = len(self.string)
        self.tot_p = factorial(self.string_length)
        self.w2d = w2d

    def permutation(self):
        print('_____________________________________')
        print('%% Standard Permutator %%')
        print('input string          : "%s"' %self.string)
        if self.to_check:
            print('string to check       : "%s"' %self.to_check)
        print('length string         :', self.string_length)
        print('num perm without repe :', self.tot_p)

        if self.w2d == 0:
            self.progress = ProgressPercentage()
            self.progress.set(self.tot_p, 'permutating >_ ')
        if self.w2d == 2:
            self.progress = ProgressPercentage()
            self.progress.set(self.tot_p, 'permutating >_ ')
            self.writer = open('output_StandardPermutator.txt', 'w')

        self.start_time = time.time()
        for n, perm in enumerate(permutations(self.list_char)):
            to_string = ''
            for x in perm:
                to_string += x
            if self.w2d == 0: # print progress percentage
                self.progress.step()
            if self.w2d == 1: # write on file permutation
                print(to_string)
            if self.w2d == 2: # write on file permutation
                self.progress.step()
                self.writer.write(to_string + '\n')
            if self.to_check and compare_string(self.to_check, to_string):
                break
        else:
            print()
            if self.to_check:
                print('<!> NOT found "%s"' %self.to_check)
        print('execution time: %s s\n' %(time.time() - self.start_time))


# Permutator home made for permutations:
# it automatically detect if there are repetitions
# and calculate all permutations with or without repetitions
# ------------------------------------------------------------
class MyPermutator():
    def __init__(self):
        self.string = ''            # string to permutate
        self.to_check = ''          # string to find into permutations
        self.find = False
        self.repetitions = False
        self.string_length = 0      # length of string
        self.tot_p = 0              # num of permutations without repetititons
        self.tot_p2 = 0             # num of permutations with repetititons
        self.w2d = 0                # helper, what to do?
        self.start_time = None
        self.progress = None
        self.writer = None

    def set_values(self, input_string, to_check_string, w2d):
        self.string = input_string
        self.to_check = to_check_string
        self.w2d = w2d
        self.string_length = len(self.string)
        self.tot_p = factorial(self.string_length)
        self.repetitions = self.detect_repetitions()
        if self.repetitions:
            list = self.count_repetitions()
            self.tot_p2 = int( factorial(self.string_length) / self.calculate_d(list) )
        if w2d == 0:
            self.progress = ProgressPercentage()
        if w2d == 2:
            self.progress = ProgressPercentage()
            self.writer = open('output_myPermutator.txt', 'w')

    def detect_repetitions(self):
        for x, char in enumerate(self.string):
            for c in self.string[0:x]:
                if c == char:
                    return True
        return False

    def count_repetitions(self):
        list =[]
        match = False
        for char in self.string:
            for c in list:
                if not match:
                    if c[0] == char:
                        match = True
                        c[1] += 1
            if not match:
                list.append([char, 1])
            match = False
        return list

    def calculate_d(self, list):
        d = 1
        for x in list:
            d *= factorial(x[1])
        return d

    def what_to_do(self, permutation):
        if self.w2d == 0: # print progress percentage
            self.progress.step()
        if self.w2d == 1: # print on terminal permutation
            print(permutation)
        if self.w2d == 2: # write on file permutation
            self.progress.step()
            self.writer.write(permutation + '\n')

    def helper(self, pre, post, x):
        new_pre = pre + post[x]
        new_post = ''
        for y, z in enumerate(post):
            if y != x:
                new_post += z
        if not (self.permute(new_pre, new_post)):
            return False

    def permute(self, pre, post):
        if self.to_check and not self.find:
            len_post = len(post)
            if len_post == 1:
                pre += post
                self.what_to_do(pre)
                if self.to_check:
                    if compare_string(self.to_check, pre):
                        self.find = True
                        return False
                    else:
                        return True
            else:
                for x, c in enumerate(post):
                    if self.repetitions:
                        if not (c in post[0:x]):
                            self.helper(pre, post, x)
                    else:
                        self.helper(pre, post, x)
                return True

    def permutation(self):
        print('_____________________________________')
        print('%% My Permutator %%')
        print('input string          : "%s"' %self.string)
        if self.to_check:
            print('string to check       : "%s"' %self.to_check)
        print('length string         :', self.string_length)
        print('num perm without repe :', self.tot_p)
        if self.repetitions:
            print('num perm with repe    :', self.tot_p2)

        if self.w2d == 0 or self.w2d == 2:
            if self.repetitions:
                self.progress.set(self.tot_p2, 'permutating >_ ')
            else:
                self.progress.set(self.tot_p, 'permutating >_ ')

        self.start_time = time.time()
        if self.permute('', self.string):
            if self.to_check and not self.find:
                print('\n<!> NOT found "%s"' %self.to_check)
        if not self.to_check:
            print()
        print('execution time: %s s\n' % (time.time() - self.start_time))



class DoPermutations():
    def __init__(self):
        self.init = False
        self.input_string = None
        self.check_string = None
        self.what_to_do = 0

    # input into terminal
    def terminal_input(self):
        self.input_string = input('\n\tEnter the string to permutate:\n\t>_ ')
        self.check_string = input('\tEnter the string to check '
                             '(to not check, press Enter):\n\t>_ ')
        self.what_to_do = int(input('\tWhat to do with permutations?:\n'
                           '\t 0: print progress percentage\n'
                           '\t 1: print permutations on terminal\n'
                           '\t 2: write permutations on file\n\t>_ '))

    def check_input_from_user(self):
        if self.check_string and len(self.input_string) != len(self.check_string):
            print('\n* <!> length of two strings is different.\n* retry')
        elif not((self.what_to_do == 0) or (self.what_to_do == 1) or (self.what_to_do == 2)):
            print('\n* <!> what_to_do input incorrect.\n* retry')
        else:
            self.init = True

    def main(self):

        while(not self.init):
            self.terminal_input()
            self.check_input_from_user()

        mine_rp = MyPermutator()
        mine_rp.set_values(self.input_string, self.check_string, self.what_to_do)
        mine_rp.permutation()

        standard = StandardPermutator()
        standard.set_values(self.input_string, self.check_string, self.what_to_do)
        standard.permutation()

dp = DoPermutations()
dp.main()
