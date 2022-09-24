#Double NAND
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)

#Double NAND Qubo
Q = {('q0', 'q0'): -2, ('q1', 'q1'): -2, ('q2', 'q2'): -5, ('q0','q1'): 1, ('q0','q2'): 2, ('q1','q2'): 2, 
                       ('q3', 'q3'): -2, ('q4', 'q4'): -3, ('q2','q3'): 1, ('q2','q4'): 2, ('q3','q4'): 2
}
response = sampler_embedded.sample_qubo(Q, num_reads=5000)

#Function:QUBO for N nand gates
#Summation n=0 to n-1 : -2(Q2n) -2(Q2n+1) -3(Q2n+2) + 1(Q2n,Q2n+1) + 2(Q2n,Q2n+2) + 2(Q2n+1,Q2n+2)

#For n=4 Nand gates
#{('q0', 'q0'): -2, ('q1', 'q1'): -2, ('q2', 'q2'): -5, ('q0','q1'): 1, ('q0','q2'): 2, ('q1','q2'): 2 ,
#                   ('q3', 'q3'): -2, ('q4', 'q4'): -5, ('q2','q3'): 1, ('q2','q4'): 2, ('q3','q4'): 2 ,
#                   ('q5', 'q5'): -2, ('q6', 'q6'): -5, ('q4','q5'): 1, ('q4','q6'): 2, ('q5','q6'): 2 ,
#                   ('q7', 'q7'): -2, ('q8', 'q8'): -3, ('q6','q7'): 1, ('q6','q8'): 2, ('q7','q8'): 2
# }


for datum in response.data(['sample', 'energy', 'num_occurrences']):
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)
#OUTPUT
#{'q0': 0, 'q1': 0, 'q2': 1, 'q3': 1, 'q4': 0} Energy:  -6.0 Occurrences:  947
#{'q0': 0, 'q1': 1, 'q2': 1, 'q3': 1, 'q4': 0} Energy:  -6.0 Occurrences:  621
#{'q0': 1, 'q1': 0, 'q2': 1, 'q3': 1, 'q4': 0} Energy:  -6.0 Occurrences:  846
#{'q0': 1, 'q1': 1, 'q2': 0, 'q3': 1, 'q4': 1} Energy:  -6.0 Occurrences:  571
#{'q0': 0, 'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1} Energy:  -6.0 Occurrences:  360
#{'q0': 1, 'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1} Energy:  -6.0 Occurrences:  557
#{'q0': 1, 'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1} Energy:  -6.0 Occurrences:  544
#{'q0': 0, 'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1} Energy:  -6.0 Occurrences:  550
#{'q0': 1, 'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1} Energy:  -5.0 Occurrences:  1
#{'q0': 1, 'q1': 0, 'q2': 1, 'q3': 1, 'q4': 1} Energy:  -5.0 Occurrences:  2
#{'q0': 0, 'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0} Energy:  -5.0 Occurrences:  1