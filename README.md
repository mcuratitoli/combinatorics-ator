# combinatorics-ator

The idea is to build some combinatorics concepts, in particular into enumerative combinatoric (like *permutations*, *combinations*, etc) in **Python** and compare amatorial algorithms with standard solutions provided by Python.

### MyProgressPercentage()
is a simple class to print the percentage of a working procedure;

`set(tot, pre_str)` method allow to set the inital information about a work (like total number of steps in `tot` variable) and the string to print before of the percentage that can explain the working procedure;

`step()` allow to go on and calculate the correct percentage

### StandardSimplePermutator()
is the class that allow to obtain all permutations of a string using the standard solution provided by Python with the `itertools` module.

In `__init__` there are basic elements of the class: 

- `string` to permute 
- string `to_check` into permutations
- `list_char` that represent the input string 
- `length` of the input (and of any permutation)
- `num_p` the number of all permutation (calculate as factorial of length)

`set_values(input_s, check_s)`, `check(string)` are inutitive method to set all values and check matching between two string.

`permutation()` is the principal method where a cicle allow to obtain all permutation of a string with the structure *permutation* included into the *itertools* method, and check them.

### MySimplePermutator()
have the same structure of *StandardSimplePermutator()* with a different core:

- `permutation()` call a recursive method `permute(s1, s2)` with two string as attributes: an empty string and the input string;
- `permute(s1, s2)` recursively identify *s1* as the "fixed" prefix of a permutation and *s2* as the remaining char to permutate.

