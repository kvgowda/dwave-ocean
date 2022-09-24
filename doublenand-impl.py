#Hardware NAND with 4-qbit
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)
Q = {('x','x'):-2, ('y','y'):-2, ('z','z'):-0.5, ('zz','zz'):-0.5, ('x','y'):1, ('x','z'):2, ('x','zz'):0, ('y','z'):0, ('y','zz'):2, ('z','zz'):-2}
response = sampler_embedded.sample_qubo(Q, num_reads=5000)
for datum in response.data(['sample', 'energy', 'num_occurrences']):
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)
#OUTPUT
#{'x': 0, 'y': 1, 'z': 1, 'zz': 1} Energy:  -3.0 Occurrences:  1166
#{'x': 1, 'y': 1, 'z': 0, 'zz': 0} Energy:  -3.0 Occurrences:  962
#{'x': 1, 'y': 0, 'z': 1, 'zz': 1} Energy:  -3.0 Occurrences:  1289
#{'x': 0, 'y': 0, 'z': 1, 'zz': 1} Energy:  -3.0 Occurrences:  1540
#{'x': 0, 'y': 1, 'z': 1, 'zz': 0} Energy:  -2.5 Occurrences:  16
#{'x': 1, 'y': 0, 'z': 0, 'zz': 1} Energy:  -2.5 Occurrences:  25
#{'x': 0, 'y': 1, 'z': 0, 'zz': 0} Energy:  -2.0 Occurrences:  1
#{'x': 1, 'y': 1, 'z': 1, 'zz': 1} Energy:  -2.0 Occurrences:  1
