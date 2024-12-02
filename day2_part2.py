def find_count(n_list):
    list_of_lists = []
    for i in range(len(n_list)):  
        new_list = n_list[:i] + n_list[i+1:]  
        list_of_lists.append(new_list)
    
    safe_count = 0 
    for list_of_list in list_of_lists:
        increasing = all(list_of_list[i] < list_of_list[i + 1] for i in range(len(list_of_list) - 1))
        decreasing = all(list_of_list[i] > list_of_list[i + 1] for i in range(len(list_of_list) - 1))

        diff = all(abs(list_of_list[i] - list_of_list[i + 1]) in {1, 2, 3} for i in range(len(list_of_list) - 1))
        if (increasing or decreasing) and diff:
            safe_count += 1 
            break

    return safe_count 

def take_input(path):
    t_safe_count = 0

    with open(path, 'r') as f:
        for line in f:
            line = line.strip().split()
            n_list = [int(x) for x in line]
            valid_diff_count = find_count(n_list)
            t_safe_count += valid_diff_count

    return t_safe_count

path = "day_2_input.txt"
res = take_input(path=path)
print(f"Safe count: {res}")
