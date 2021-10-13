a = {1,1,2,3,4,5,10}
b = {20,30,40,15}

print(a.union(b))
print(a.intersection(b))
print(a.isdisjoint(b))

m = {1,1,2,3,4,5}
n = {10,20,30,40,15,3}
print(m.isdisjoint(n))

k = {'name': 78965432, 'age': 24}
print(k['age'])
print(k.keys())
print(k.values())

def tasneem(s):
    for i in s:
        print(i)
tasneem([1,2,3,4,6,9,0]) 

f = open('hi.txt', 'w')
b = f.write('this is visualstudio day65')
print(b)
f.close()

f = open('hi.txt', 'r')
b = f.read()
print(b)
f.close()

