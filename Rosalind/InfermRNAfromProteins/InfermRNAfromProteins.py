'''
ROSALIND
Inferring mRNA from Protein

Pitfalls of Reversing Translation
When researchers discover a new protein, they would like to infer the strand of mRNA from which this protein could have been translated, thus allowing them to locate genes associated with this protein on the genome.

Unfortunately, although any RNA string can be translated into a unique protein string, reversing the process yields a huge number of possible RNA strings from a single protein string because most amino acids correspond to multiple RNA codons (see the RNA Codon Table).

Because of memory considerations, most data formats that are built into languages have upper bounds on how large an integer can be: in some versions of Python, an "int" variable may be required to be no larger than 231−1, or 2,147,483,647. As a result, to deal with very large numbers in Rosalind, we need to devise a system that allows us to manipulate large numbers without actually having to store large numbers.

Problem

For positive integers a and n, a modulo n (written a mod n in shorthand) is the remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.

Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that a and b are congruent modulo n if amodn=bmodn; in this case, we use the notation a≡bmodn.

Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn, then a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these rules, you may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.

As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

Sample Dataset
MA

Sample Output
12

Hint
What does it mean intuitively to take a number modulo 1,000,000?
'''

def fib(nth_month:int, m_live:int, mature_month:int = 2):
    generation = [1] + [0] * (m_live-1)
    for i in range(nth_month-1):
        print(generation)
        generation = [sum(generation[mature_month-1:])] + generation[:-1]
    return generation

f = open("rosalind_fibd_sample.txt")
l = f.read()

l = l.strip().split(' ')
l = [int(x) for x in l]

n = l[0]
m = l[1]

# print(n, m)
print(fib(n, m))
print(sum(fib(n, m)))