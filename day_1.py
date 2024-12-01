'''left = [3,4,2,1,3,3]
right = [4,3,5,3,9,3]

left.sort()
right.sort()'''
#print(left, right)

path = 'day_1_input.txt'


def star(left, right):
    left.sort()
    right.sort()
    n = len(left)
    total_sum = 0
    new = []

    for i in range(n):
        new_elem = abs(left[i] - right[i])
        new.append(new_elem)

    for i in range(n):
        total_sum += new[i]

    return total_sum


def take_input(path):
    left = []
    right = []

    with open(path, 'r') as f:
        for line in f:
            if line.strip(): 
                l, r = map(int, line.split())
                left.append(l)
                right.append(r)

    return left, right

left, right = take_input(path=path)
res = star(left=left, right=right)
print(res)
