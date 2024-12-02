path  = 'day_1_input.txt'
def take_input(path):
    left = []
    right = []
    with open(path, 'r') as f:
        for line in f:
            if line.split():
                l, r = map(int, line.split())
                left.append(l)
                right.append(r)

    return left, right

def similarity(left, right):
    sim_sum = 0
    
    for i in range(len(left)):
        curr_elem = left[i]
        count = 0
        for elem in right:
            if elem == curr_elem:
                count += 1 
        sim_sum += curr_elem * count

    
    return sim_sum

left, right = take_input(path=path)
res = similarity(left=left, right=right)
print(res)                 
