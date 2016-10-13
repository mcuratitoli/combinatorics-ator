# combinatorics-ator

The idea is to build some combinatorics concepts, in particular into enumerative combinatoric (like *permutations*, *combinations*, etc) in **Python** and compare amatorial algorithms with standard solutions provided by Python.

### ProgressPercentage()
is a simple class that allow to print the percentage of a working procedure;

`set(tot, pre_str)` allow to set the inital information about a work (like total number of steps in `tot` variable) and the string to print before of the percentage that can explain the working procedure;

`step()` allow to go on and calculate the correct percentage

### StandardPermutator()
is the class that allow to obtain all simple permutations of a string (without repetitions of char) using the standard solution provided by Python with the `itertools` module.

In `__init__` there are basic elements of the class: 

- `string`: string to permute 
- `to_check`: string to search into permutations
- `list_char`: list that represent the input string 
- `string_length`: length of the input (and of any permutation)
- `tot_p`: the number of all permutation without repetitions (calculate as factorial of length)
- `w2d`: int that indicate "what to do" [0 = print progress percentage; 1 = print on terminal all permutations, 2 = write on file]

`set_values(input_s, check_s, w2d)`, `check_string(string)`: methods to set all values and check matching between two string.

`permutation()`: the principal method where a cicle allow to obtain all permutation of a string with the structure *permutation* included into the *itertools* method, and check them.

### MyPermutator()
class very similar to *StandardPermutator()*.

In `__init__` the differences are: 

- `repetitions`: a boolean that allow to know if there are repetitions in *input_string*
- `tot_p2`: if there are repetitions, is the number of permutations with repetitions

`set_values()` as in *StandardPermutator()* is sets all values and counts the number of permutations with (if there are) and without repetitions;

`detect_count_repetitions()`, `calculate_d(list)`: methods to detect if there are repetitons and if true, it helps to calculate *tot_p2*;

`what_to_do(p)`: a sort of switch that help the choice of what to do;
 
`permutation()`: principal method, it calls a recursive method `permute(s1, s2)` with two string as attributes: an empty string and the input string;

`permute(s1, s2)` recursively identify *s1* as the prefix of a permutation and *s2* as the remaining chars to permutate. It use `check_in_list(list, elem)` to verify if a char has already been "used" in prefix, to evitate to calculate unnecessary permutations and `what_to_do(p)` to help the choice of what to do.

