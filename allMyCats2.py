
catNames = []
while True:
    print('Enter the name of the cat '+ str(len(catNames)+1)  +
            ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #List concatenation

print('The cat name are:')
for name in catNames:
    print(' ' + name) 