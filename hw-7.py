# less 1

n = int(input('quantity N: '))
list_number = []

for i in range(n):
    num = int(input('number N: '))
    list_number.append(num)

list_number.reverse()
print(*list_number)

# less 2

new_list = list(map(int, input().split()))
new_list.insert(0, new_list.pop())
print(*new_list)

# less 3

m = int(input('boat m: '))
n = int(input('fisher q: '))
t = []

for i in range(n):
    f = int(input('fisher m: '))
    t.append(f)

t.sort(reverse=True)

boat_count = 0

if t[0] > m:
    print('oops')
    exit()

while len(t):
    boat_count += 1
    k = m - t.pop()
    for i in range(len(t)):
        if t[i] <= k:
            t.pop(i)
            break

print(f'need {boat_count} boat')