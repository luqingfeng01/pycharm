import pickle
l = [1,2,3,]
print(pickle.dumps(l))


b = pickle.dumps(l)

print(pickle.loads(b))


d = {"name":"陆庆锋","age":18,"sex":"男"}
print(pickle.dumps(d))

b = pickle.dumps(d)
print(pickle.loads(b))