import random
dicts={"Pesty":90,"Magii":80,"Smoothy":50}
new_dicts={}
list1=[5,10,15]

for key,value in dicts.items():
    new_price=value-value*(random.choice(list1)/100)
    print(f'New price of {key} is: {new_price}')
    new_dicts[key]=new_price
print(new_dicts)