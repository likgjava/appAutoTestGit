import traceback

t = {
    "name": "likg",
    "age": 18
}

for k, w in t.items():
    print(k)
    print(w)
    print("------------")

print("===============================")
for k in t.keys():
    print(k)
    print(t.get(k))

traceback.print_exc()




