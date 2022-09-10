from dimod import ExactSolver
sampler = ExactSolver() 

Q = {('x', 'y'): 1, ('x', 'z'): -2, ('y', 'z'): -2, ('z', 'z'): 3}

response = sampler.sample_qubo(Q)
print (response)
for datum in response.data('sample', 'energy’):
    print(datum.sample, datum.energy)