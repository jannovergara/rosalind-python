'''
ROSALIND
Consensus and Profile

Finding a Most Likely Common Ancestor
In “Counting Point Mutations”, we calculated the minimum number of symbol mismatches between two strings of equal length to model the problem of finding the minimum number of point mutations occurring on the evolutionary path between two homologous strands of DNA. If we instead have several homologous strands that we wish to analyze simultaneously, then the natural problem is to find an average-case strand to represent the most likely common ancestor of the given strands.A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the trings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

            A T C C A G C T
            G G G C A A C T
            A T G G A T C T
DNA Strings	A A G C A A C C
            T T G G A A C T
            A T G C C A T T
            A T G G C A C T

            A   5 1 0 0 5 5 0 0
Profile	    C   0 0 1 4 2 0 6 1
            G   1 1 6 3 0 1 0 0
            T   1 5 0 0 0 1 1 6

Consensus	A T G C A A C T


Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
'''

from Bio import SeqIO
import numpy as np
import pandas as pd

seq_object = SeqIO.parse("rosalind_cons.txt", "fasta")

seq_list = []
for seq in seq_object:
    lis_seq = list(seq.seq)
    seq_list.append(lis_seq)

arr_seq = np.array(seq_list)

col = arr_seq.shape[1]
A = []; C = []; G = []; T = []
for i in range(col):
    # A = A + ' ' + str(str(arr_seq[:,i]).count('A'))
    A.append(str(arr_seq[:,i]).count('A'))    
    C.append(str(arr_seq[:,i]).count('C'))
    G.append(str(arr_seq[:,i]).count('G'))
    T.append(str(arr_seq[:,i]).count('T'))

df_ACGT = pd.DataFrame(list(zip(A, C, G, T)))
df_ACGT.columns = ['A', 'C', 'G', 'T']

# find the column name of maximum values in every row
consensus = df_ACGT.idxmax(axis=1)

#  print result
print(''.join(str(item) for item in consensus))
print('A:', ' '.join(str(item) for item in A))
print('C:', ' '.join(str(item) for item in C))
print('G:', ' '.join(str(item) for item in G))
print('T:', ' '.join(str(item) for item in T))