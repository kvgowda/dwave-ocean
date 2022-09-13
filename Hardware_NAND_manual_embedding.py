#Hardware NAND with 4-qbit
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)
Q = {('x','x'):-2, ('y','y'):-2, ('z','z'):-0.5, ('zz','zz'):-0.5, ('x','y'):1, ('x','z'):2, ('x','zz'):0, ('y','z'):0, ('y','zz'):2, ('z','zz'):-2}
response = sampler_embedded.sample_qubo(Q, num_reads=5000)
for datum in response.data(['sample', 'energy', 'num_occurrences']):
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)