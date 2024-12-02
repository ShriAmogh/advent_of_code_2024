#6 list containing 5 levels
'''l1 = [7, 6, 4, 2, 1]
l2 = [1, 2, 7, 8, 9]
l3 = [9, 7, 6, 2, 1]
l4 = [1, 3, 2, 5, 5]
l5 = [8, 6, 4, 4, 1]
l6 = [1, 3, 6, 7, 9]


lenght_each = []
for n in range(1,7):
    elem_name = f"l{n}"
    leng = len(elem_name)
    print(leng)
    lenght_each.append(leng)

print(lenght_each)
l_names = [l1,l2,l3,l4,l4,l5,l6]
n = len(l1)
curr_elem = 0
first_elem = l1[0]'''
#diff = [1,2,3,-1,-2,-3]


def find_count(n_list):
    emp_list = []
    safe_count = 0
    unsafe_count = 0
    diff = [1,3]
    for i in range(len(n_list) - 1): 
        difference = abs(n_list[i] - n_list[i + 1])
        if difference in diff:
            emp_list.append("d")
        else:
            emp_list.append("n")
            break

    if "n" in emp_list:
        unsafe_count += 1
    elif all(elem == "d" for elem in emp_list):
        safe_count += 1


    return unsafe_count, safe_count

def take_input(path):
    t_safe_count = 0
    t_unsafe_count = 0

    with open(path, 'r') as f:
        for line in f:
            line = line.strip().split()
            n_list = [int(x) for x in line]
            unsafe_count, safe_count = find_count(n_list)

            t_unsafe_count += unsafe_count
            t_safe_count += safe_count

    return t_unsafe_count, t_safe_count



path = "day_2_input.txt"
res = take_input(path=path)
print(f"unsafe count: {res[0]}")
print(f"safe count: {res[1]}")
