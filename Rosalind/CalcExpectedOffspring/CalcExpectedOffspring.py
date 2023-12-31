'''
ROSALIND
Calculating Expected Offspring

The Need for Averages
Averages arise everywhere. In sports, we want to project the average number of games that a team is expected to win; in gambling, we want to project the average losses incurred playing blackjack; in business, companies want to calculate their average expected sales for the next quarter.

Molecular biology is not immune from the need for averages. Researchers need to predict the expected number of antibiotic-resistant pathogenic bacteria in a future outbreak, estimate the predicted number of locations in the genome that will match a given motif, and study the distribution of alleles throughout an evolving population. In this problem, we will begin discussing the third issue; first, we need to have a better understanding of what it means to average a random process.

Problem

For a random variable X taking integer values between 1 and n, the expected value of X is E(X)=∑nk=1k×Pr(X=k). The expected value offers us a way of taking the long-term average of a random variable over a large number of trials.

As a motivating example, let X be the number on a six-sided die. Over a large number of rolls, we should expect to obtain an average of 3.5 on the die (even though it's not possible to roll a 3.5). The formula for expected value confirms that E(X)=∑6k=1k×Pr(X=k)=3.5.

More generally, a random variable for which every one of a number of equally spaced outcomes has the same probability is called a uniform random variable (in the die example, this "equal spacing" is equal to 1). We can generalize our die example to find that if X is a uniform random variable with minimum possible value a and maximum possible value b, then E(X)=a+b2. You may also wish to verify that for the dice example, if Y is the random variable associated with the outcome of a second die roll, then E(X+Y)=7.

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

Sample Dataset
1 0 0 1 0 1

Sample Output
3.5

Hint: Solve for probabilities per couple
'''

f = open("rosalind_iev.txt")
l = f.read()

l = l.strip().split(' ')

couple = [int(x) for x in l]
child = 2

# displaying the dominant phenotype
prob_AA_AA = couple[0] * child * (4/4)
prob_AA_Aa = couple[1] * child * (4/4)
prob_AA_aa = couple[2] * child * (4/4)
prob_Aa_Aa = couple[3] * child * (3/4)
prob_Aa_aa = couple[4] * child * (2/4)
prob_aa_aa = couple[5] * child * (0/4)

E = prob_AA_AA + prob_AA_Aa + prob_AA_aa + prob_Aa_Aa + prob_Aa_aa + prob_aa_aa

print(E)