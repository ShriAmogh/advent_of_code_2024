def find_count(n_list):
    increasing_count = 0
    decreasing_count = 0
    safe_count = 0
    
    increasing = all(n_list[i] < n_list[i + 1] for i in range(len(n_list) - 1))
    
    decreasing = all(n_list[i] > n_list[i + 1] for i in range(len(n_list) - 1))

    diff = all(abs(n_list[i] - n_list[i + 1]) in {1, 2, 3} for i in range(len(n_list) - 1))
    

    if increasing or decreasing:
        if diff:
            safe_count += 1  
    else:
        safe_count += 0 

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
print(f"safe count: {res}")
