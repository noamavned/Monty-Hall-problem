from random import randint as gen

n = 1000000  # can be changed
s = 0

for i in range(n):
    s += 1 if gen(0,2) == gen(0,2) else 0


res = s/n*100
ss = 100-res

print(f"no switch: {res}\nswitch: {ss}")
