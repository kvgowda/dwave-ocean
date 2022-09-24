#Name: Kantha Vishwas Gowda
#Unity ID: kgowda

#XOR from NAND
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)

Q = {}

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


#MAIN program starts Here

#Define XOR gate using 4 NAND gates
Q = Add_2input_NAND(Q, 'q0', 'q1', 'q2')
Q = Add_2input_NAND(Q, 'q0', 'q2', 'q3')
Q = Add_2input_NAND(Q, 'q1', 'q2', 'q4')
Q = Add_2input_NAND(Q, 'q3', 'q4', 'q5')

#print(Q)
response = sampler_embedded.sample_qubo(Q, num_reads=10000)

for datum in response.data(['sample', 'energy', 'num_occurrences']):
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)

#OUTPUT
#{'q0': 0, 'q1': 1, 'q2': 1, 'q3': 1, 'q4': 0, 'q5': 1} Energy:  -12.0 Occurrences:  2266
#{'q0': 0, 'q1': 0, 'q2': 1, 'q3': 1, 'q4': 1, 'q5': 0} Energy:  -12.0 Occurrences:  2605
#{'q0': 1, 'q1': 1, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 0} Energy:  -12.0 Occurrences:  1981
#{'q0': 1, 'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 1} Energy:  -12.0 Occurrences:  2117
#{'q0': 0, 'q1': 1, 'q2': 1, 'q3': 1, 'q4': 0, 'q5': 1} Energy:  -12.0 Occurrences:  1
#{'q0': 0, 'q1': 1, 'q2': 1, 'q3': 1, 'q4': 0, 'q5': 0} Energy:  -11.0 Occurrences:  62
#{'q0': 0, 'q1': 1, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 0} Energy:  -11.0 Occurrences:  73
#{'q0': 0, 'q1': 0, 'q2': 1, 'q3': 1, 'q4': 1, 'q5': 1} Energy:  -11.0 Occurrences:  1
#{'q0': 1, 'q1': 1, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 1} Energy:  -11.0 Occurrences:  45
#{'q0': 1, 'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1, 'q5': 1} Energy:  -11.0 Occurrences:  76
#{'q0': 1, 'q1': 0, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -11.0 Occurrences:  76
#{'q0': 0, 'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 1} Energy:  -11.0 Occurrences:  102
#{'q0': 1, 'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -11.0 Occurrences:  71
#{'q0': 1, 'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0} Energy:  -11.0 Occurrences:  61
#{'q0': 0, 'q1': 1, 'q2': 1, 'q3': 1, 'q4': 1, 'q5': 0} Energy:  -11.0 Occurrences:  64
#{'q0': 0, 'q1': 0, 'q2': 1, 'q3': 1, 'q4': 0, 'q5': 1} Energy:  -11.0 Occurrences:  71
#{'q0': 1, 'q1': 0, 'q2': 1, 'q3': 1, 'q4': 1, 'q5': 0} Energy:  -11.0 Occurrences:  48
#{'q0': 1, 'q1': 1, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 1} Energy:  -11.0 Occurrences:  1
#{'q0': 0, 'q1': 0, 'q2': 1, 'q3': 1, 'q4': 1, 'q5': 1} Energy:  -11.0 Occurrences:  61
#{'q0': 1, 'q1': 1, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 1} Energy:  -11.0 Occurrences:  49
#{'q0': 0, 'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -11.0 Occurrences:  71
#{'q0': 1, 'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 0} Energy:  -11.0 Occurrences:  64
#{'q0': 1, 'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -10.0 Occurrences:  2
#{'q0': 1, 'q1': 0, 'q2': 0, 'q3': 0, 'q4': 1, 'q5': 1} Energy:  -10.0 Occurrences:  3
#{'q0': 0, 'q1': 0, 'q2': 1, 'q3': 1, 'q4': 0, 'q5': 0} Energy:  -10.0 Occurrences:  1
#{'q0': 0, 'q1': 1, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 1} Energy:  -10.0 Occurrences:  3
#{'q0': 0, 'q1': 0, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -10.0 Occurrences:  4
#{'q0': 0, 'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 1} Energy:  -10.0 Occurrences:  2
#{'q0': 1, 'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 1} Energy:  -10.0 Occurrences:  3
#{'q0': 1, 'q1': 1, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 0} Energy:  -10.0 Occurrences:  3
#{'q0': 0, 'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0} Energy:  -10.0 Occurrences:  5
#{'q0': 0, 'q1': 1, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 1} Energy:  -10.0 Occurrences:  4
#{'q0': 1, 'q1': 0, 'q2': 1, 'q3': 1, 'q4': 0, 'q5': 1} Energy:  -10.0 Occurrences:  1
#{'q0': 1, 'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1, 'q5': 0} Energy:  -10.0 Occurrences:  3