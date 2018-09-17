import itertools

lists = ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M',
         'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M',
         'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']

# lst = itertools.combinations_with_replacement(list, 30)
lst = list(set(itertools.permutations(lists)))
print(lst)

for p in lst:
    print(p)
