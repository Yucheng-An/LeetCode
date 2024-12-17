fruits = ['apple', 'banana', 'cherry','cherry','cherry','cherry']
myMap = {}
for index,value in enumerate(fruits):
    myMap[value] = index
if "apple" not in myMap:
    print("here")
print(myMap)
