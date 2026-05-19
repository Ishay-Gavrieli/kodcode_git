# question 1
def sum_dic(dic):
    count = 0
    for value in dic.values():
        count += value

    return count

# question 2
def max_key(dic):
    max_v = float('-inf')
    for key,value in dic.items():
        if value > max_v:
            max_v = value
            max_k = key

    return max_k

# question 3
def count_characters(user_str):
    dic = dict()
    for i in user_str:
        dic[i] = dic.get(i,0)+1
        
    return dic

# question 4
def invert_dictionary(dic):
    new = dict()
    for key,value in dic.items():
        new[value] = key
    return new


# question 5
# 1
def Merge_two_dictionaries(dic1,dic2):
    dic1.update(dic2)

    return dic1

# 2
def Merge_two_dictionaries(dic1,dic2):
    return dic1 | dic2


# question 6
def filter_by_value(dic,threshold):
    new = dict()
    for key,value in dic.items():
        if value > threshold:
            new[key] = value   

    return new


# question 7
def group_by_first_letter(lst):
    result = dict()
    for i in lst:
        result.setdefault(i[0],[]).append(i)
    return result


# question 8
# 1
def  word_frequency(user_str):
    new_str = user_str.split()
    dic = dict()
    for i in new_str:
        dic[i] = dic.get(i,0)+1
    return dic

# 2
def  word_frequency(user_str):
    new_str = user_str.split()
    dic = dict()
    for i in new_str:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic


# question 9
def common_keys(dic1,dic2):
    result = []
    for key in dic1:
        if key in dic2:
            result.append(key)
    return result


# question 10
# 1
def most_frequent_value(dic):
    new_dic = dict()
    for value in dic.values():
        new_dic[value] = new_dic.get(value,0)+1


    max_value = float("-inf")
    for key,value in new_dic.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key

# 2
def most_frequent_value(dic):
    new_dic = dict()
    for value in dic.values():
        new_dic[value] = new_dic.get(value,0)+1
        
    return max(new_dic.items(), key=lambda item: item[1])[0]
  
