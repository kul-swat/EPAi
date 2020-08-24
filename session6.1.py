a = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
b = ['spades', 'clubs', 'hearts', 'diamonds']

from itertools import repeat, chain
c = list(itertools.chain(*list(repeat(a,len(b)))))
d = list(itertools.chain(*list(repeat(b,len(a)))))

e = list(zip(c,d))
output = list(map(lambda suits, values: zip(suits,values), e))
for i in output:
    print(tuple(i))

