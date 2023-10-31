'''
ROSALIND
Mortal Fibonacci Rabbits

Wabbit Season
In “Rabbits and Recurrence Relations”, we mentioned the disaster caused by introducing European rabbits into Australia. By the turn of the 20th Century, the situation was so out of control that the creatures could not be killed fast enough to slow their spread (see Figure 1).

The conclusion? Build a fence! The fence, intended to preserve the sanctity of Western Australia, was completed in 1907 after undergoing revisions to push it back as the bunnies pushed their frontier ever westward (see Figure 2). If it sounds like a crazy plan, the Australians at the time seem to have concurred, as shown by the cartoon in Figure 3.

By 1950, Australian rabbits numbered 600 million, causing the government to decide to release a virus (called myxoma) into the wild, which cut down the rabbits until they acquired resistance. In a final Hollywood twist, another experimental rabbit virus escaped in 1991, and some resistance has already been observed.

The bunnies will not be stopped, but they don't live forever, and so in this problem, our aim is to expand Fibonacci's rabbit population model to allow for mortal rabbits.

Problem

Figure 4. A figure illustrating the propagation of Fibonacci's rabbits if they die after three months.
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Sample Dataset
6 3

Sample Output
4

Check pattern from this expansion of the sequence. Example is for ff configuration - rabbits die after one year of maturity or 3 years to live.
---
month   new     mating  3_yrs   total_rabbits
1       1       0       0       1
2       0       1       0       1
3       1       0       1       2
4       1       1       0       2
5       1       1       1       3
6       2       1       1       4
7       2       2       1       5
8       3       2       2       7
9       4       3       2       9
10      5       4       3       12
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