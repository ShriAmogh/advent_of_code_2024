path = "day3_input.txt"

def take_input(path):
    mul_list = []
    with open(path, 'r') as f:
        for line in f:
            n = len(line)
            for i in range(n - 1):
                if line[i:i + 4] == "mul(":
                    initial = i
                    i += 4
                    while i < n and line[i] != ")":
                        i += 1
                    if i < n and line[i] == ")":
                        elem = line[initial:i]
                        if len(elem) <= 11:
                            mul_list.append(elem + ")")
    return mul_list

def apply_mul(mul_list):
    mul_sum = 0
    for each_elem in mul_list:
        nums_in_mul = each_elem[4:-1] 
        nums = nums_in_mul.split(',')

        try:
            a, b = map(int, nums)
            mul_sum += a * b
        except ValueError:
            pass  
    return mul_sum

res = apply_mul(take_input(path))
print(res)
