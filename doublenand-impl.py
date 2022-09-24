#Name: Kantha Vishwas Gowda
#Unity ID: kgowda


#Double NAND
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)

#Create empty Qubo or specify any existing QUBO
Q = {}
#Number of cascading n-NAND gates
n = 2

#This function adds a NAND Gate Qubo to your existing qubo
def Add_2input_NAND(Existing_QUBO, input1, input2, output):
  #Define Simple NAND QUBO
  Simple_NAND_QUBO = {(str(input1), str(input1)): -2, (str(input2), str(input2)): -2, (str(output), str(output)): -3,
                      (str(input1), str(input2)): 1, (str(input1), str(output)): 2, (str(input2), str(output)): 2}
  
  #Check if the Qbit/chain strength exits else append
  for key in Simple_NAND_QUBO.keys():
    if key in Existing_QUBO:
      Existing_QUBO[key] = Existing_QUBO[key] + Simple_NAND_QUBO[key]
    else:
      Existing_QUBO[key] = Simple_NAND_QUBO[key]
  
  return Existing_QUBO

#Loop through the number of nand gates that need to be cascaded
for i in range(n):
  in1 = 'q' + str(2*i) ; in2 = 'q' + str(2*i+1) ; out1 = 'q' + str(2*i+2)
  Q = Add_2input_NAND(Q, in1, in2, out1)

#print(Q)
# n = 4 NAND gates QUBO from above Definition/Function
#{('q0', 'q0'): -2, ('q1', 'q1'): -2, ('q2', 'q2'): -5, ('q0', 'q1'): 1, ('q0', 'q2'): 2, ('q1', 'q2'): 2,
#                   ('q3', 'q3'): -2, ('q4', 'q4'): -5, ('q2', 'q3'): 1, ('q2', 'q4'): 2, ('q3', 'q4'): 2, 
#                   ('q5', 'q5'): -2, ('q6', 'q6'): -5, ('q4', 'q5'): 1, ('q4', 'q6'): 2, ('q5', 'q6'): 2, 
#                   ('q7', 'q7'): -2, ('q8', 'q8'): -3, ('q6', 'q7'): 1, ('q6', 'q8'): 2, ('q7', 'q8'): 2
#}

#Mathematical Function:QUBO for n NAND gates
#Summation n=0 to n-1 : -2(Q2n) -2(Q2n+1) -3(Q2n+2) + 1(Q2n,Q2n+1) + 2(Q2n,Q2n+2) + 2(Q2n+1,Q2n+2)

response = sampler_embedded.sample_qubo(Q, num_reads=5000)

for datum in response.data(['sample', 'energy', 'num_occurrences']):
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)

#OUTPUT
#{'q0': 0, 'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1} Energy:  -6.0 Occurrences:  871
#{'q0': 1, 'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1} Energy:  -6.0 Occurrences:  777
#{'q0': 1, 'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1} Energy:  -6.0 Occurrences:  637
#{'q0': 0, 'q1': 1, 'q2': 1, 'q3': 1, 'q4': 0} Energy:  -6.0 Occurrences:  493
#{'q0': 1, 'q1': 1, 'q2': 0, 'q3': 1, 'q4': 1} Energy:  -6.0 Occurrences:  590
#{'q0': 0, 'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1} Energy:  -6.0 Occurrences:  801
#{'q0': 1, 'q1': 0, 'q2': 1, 'q3': 1, 'q4': 0} Energy:  -6.0 Occurrences:  358
#{'q0': 0, 'q1': 0, 'q2': 1, 'q3': 1, 'q4': 0} Energy:  -6.0 Occurrences:  470
#{'q0': 0, 'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1} Energy:  -5.0 Occurrences:  1
#{'q0': 1, 'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1} Energy:  -5.0 Occurrences:  1
#{'q0': 0, 'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0} Energy:  -5.0 Occurrences:  1