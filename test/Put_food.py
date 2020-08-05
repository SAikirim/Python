import Fridge

f = Fridge.Fridge()
apple = Fridge.Food()
elephant = Fridge.Food()
banana = "banana"

print(f.opend(), "\n")
print(f.put(apple), "\n")
print(f.put(elephant), "\n")
print(f.put(banana), "\n")
print(f.close())