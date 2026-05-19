# question 1
def remove_duplicates(lst):
    new = set(lst)
    return list(new)


# question 2
def count_unique_elements(lst):
    new = set(lst)
    count = 0
    for i in new:
        count += 1
    return count



# question 3
def common_elements(lst1,lst2):
    new1 = set(lst1)    
    new2 = set(lst2)
    return list(new1 & new2)


# question 4
def different_elements(lst1,lst2):
    new1 = set(lst1)    
    new2 = set(lst2)
    return list(new1 ^ new2)


# question 5
def is_subnet(lst1,lst2):
    for i in lst1:
        if i not in lst2:
            return False
    return True 

        

# question 6
def unique_characters(user_str):
    new = set(user_str)
    return len(new) == len(user_str)



# question 7
def  repeated_element(user_lst):
    new = set()
    for i in user_lst:
        if i in new:
            return i
        new.add(i)
    return None


# question 8
def distinct_words(user_lst):
    new = user_lst.lower().split()
    return len(set(new))



# question 9
# 1 
def pair_sum_exists(user_lst,target):
    new = set()
    for n in user_lst:
        result = target - n
        if result in new:
            return True
        new.add(n)
    return False

# 2
def pair_sum_exists(user_lst,target):
    new = set(user_lst)
    for i in user_lst:
        for j in user_lst:
            if i + j == target:
                return True
    return False



# question 10
# 1
def symmetric_difference(lst1, lst2):
    new = []

    for i in lst1:
        if i not in lst2:
            new.append(i)
            
    for i in lst2:
        if i not in lst1:
            new.append(i)
            
    return sorted(new)

# 2
def symmetric_difference_fast(lst1, lst2):
    set1,set2 = set(lst1),set(lst2)
    result = [i for i in set1 if i not in set2] + [i for i in set2 if i not in set1]

    return sorted(result)

