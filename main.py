import cobra
from cobra import Model, Reaction, Metabolite
style = Model('chance')

ko=Reaction('ko')
ko.lower_bound = 1
ko.upper_bound = 1

ko1 = Reaction('ko1')
ko1.lower_bound = 0
ko1.upper_bound = 1000

ko2 = Reaction('ko2')
ko2.lower_bound = 0
ko2.upper_bound = 1000

ko3 = Reaction('ko3')
ko3.lower_bound = .5
ko3.upper_bound = .5

M = Reaction('M')
M.lower_bound = 0
M.upper_bound = 1000

energy = Reaction('energy')
energy.lower_bound = 0
energy.upper_bound = 1000
A = Metabolite(
    'A', compartment='c')
B = Metabolite(
    'B', compartment='c')
C = Metabolite(
    'C', compartment='c')
energy = Metabolite(
    'energy', compartment='c')
ko.add_metabolites({A: 1})
ko1.add_metabolites({A: -1, B: 1})
ko2.add_metabolites({B: -1, C: 1})
ko3.add_metabolites({energy: -1})
M.add_metabolites({C: -1})
energy.add_metabolites({A: -1, energy: 1})
style.add_reactions([ko, ko1, ko2, ko3, M, energy])
style.objective = 'M'
style.optimize()