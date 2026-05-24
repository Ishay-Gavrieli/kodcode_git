# question 1
def sum_list(lst):
    count = 0
    for n in lst:
        count += n
    return count

# question 2
def max_list(lst):
    max_l = lst[0]
    for n in lst:
        if n > max_l:
            max_l = n
    return max_l

# question 3
def list_numbers(lst,value):
    count = 0
    for n in lst:
        if n == value:
            count += 1
    return count

# question 4
def reversed_list(lst):
    new = []
    for n in range(1,len(lst)+1):
        new.append(lst[-n])
    return new


# question 5
def removed_duplicates(lst):
    new = set(lst)
    return list(new)

# question 6
def second_largest(lst):
    if len(lst) < 2:
        return None 
    
    first_l = float('-inf')
    second_l = float('-inf')

    for i in lst:
        if i > first_l:
            second_l = first_l
            first_l = i
        elif i > second_l and i != first_l:
            second_l = i

    return second_l if second_l != float('-inf') else None


# question 7
# 1 
def sorted_list(lst1,lst2):
    lst1.extend(lst2)
    return sorted(lst1)

# 2
def sorted_list(lst1, lst2):
    merged = []
    i, j = 0, 0
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
            
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    
    return merged


# question 8
def rotate_list(lst, k):
    if not lst:
        return lst
        
    k = k % len(lst)
    
    part1 = lst[-k:] 
    part2 = lst[:-k]  
    
    return part1 + part2




