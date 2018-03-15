import random
s = 0

d = 0
arr = [None] * 100
for i in range(1, 100):

    arr[i] = i


arr[0] = random.randint(1, 99)
print(arr)
random.shuffle(arr)

arr3 = {}
arr2 = []

for x in arr :
    if x not in arr3 :
        arr3[x] = 1

    else :
        if arr3[x] == 1 :
            arr2.append(x)

        arr3[x] += 1

print(arr2)

