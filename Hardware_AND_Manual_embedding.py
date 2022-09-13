#from dwave.system.samplers import DWaveSampler
from dwave.system import DWaveSampler
sampler_manual = DWaveSampler(solver={'topology__type': 'chimera'})
#import dwave.inspector
from dwave.system.composites import FixedEmbeddingComposite
embedding = {'x': {0}, 'y': {4}, 'z': {1}, 'zz': {5}}
sampler = DWaveSampler()
sampler_embedded = FixedEmbeddingComposite(sampler, embedding)
Q = {('x','y'):1, ('y','z'):-2, ('x','zz'):-2, ('z','zz'):-2, ('z','z'):2.5, ('zz','zz'):2.5}
response = sampler_embedded.sample_qubo(Q, embedding, num_reads=5000)
dwave.inspector.show(response)
for datum in response.data(['sample', 'energy', 'num_occurrences']):
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)