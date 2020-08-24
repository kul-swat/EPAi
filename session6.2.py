vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

def card_dec():
    '''each element of 1 loop merge with every element of 2nd loop'''
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    collection = []
    for i in suits:
        for j in vals:
            each_card = f"{i}-{j}"
            collection.append(each_card)
    print(collection)

card_dec()