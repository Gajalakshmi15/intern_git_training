In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:
def animals(chickens,cows,pigs):
    total_chickens=2*chickens
    total_cows=4*cows
    total_pigs=4*pigs
    return total_chickens+total_cows+total_pigs
print('The total no of legs is:')
print(animals(2,4,4))
l1=['1','2','3','4']
l2=['a','b','c','d']
d={}
for i in l1:
    d[i[0]]=i[1]
    print(d)
