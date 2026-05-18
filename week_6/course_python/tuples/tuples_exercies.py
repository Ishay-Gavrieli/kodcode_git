# question 1

def sum_tuple(tup):
    count = 0 
    for n in tup:
        count += n
    return count


# question 2
def max_tuple(tup):
    max_n = tup[0]  
    for n in tup:
        if n > max_n:
            max_n = n
    return max_n


# question 3
def count_ccurrences(tup,value):
    count = 0
    for n in tup:
        if n == value:
            count += 1
    return count

# question 4
def reversed(tup):
    new = ()
    for n in range(1,len(tup)+1):
        new = new + (tup[-n],)
    return new

    
# question 5
# 1
def swap_pairs(tup):
    new = ()
    j = 0
    i = 0
    for n in range(len(tup)//2):
        new = new + (tup[j+1],tup[i])
        j += 2
        i += 2
  
    return new

# 2
def swap_pairs(tup):
    new = ()
    for n in range(0,len(tup),2):
        new = new + (tup[n+1],tup[n])
        
  
    return new


# question 6
def min_and_max_(tup):
    max_n = tup[0] 
    min_n = tup[0] 
    for n in tup:
        if n > max_n:
            max_n = n
        if n < min_n:
            min_n = n

    return max_n,min_n

# question 7
def distance(tup1,tup2):
    x1,y1 = tup1
    x2,y2 = tup2
    return( ((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5


# question 8
def merge_and_sort(tup1,tup2):
    return tuple(sorted(tup1 + tup2))



# question 9
# 1 
def count_tuple(tup):
    dic = dict()
    for n in tup:
        if n in dic:
            dic[n] += 1
       
        else:
            dic[n] = 1
    return tuple(dic.items())

# 2
def count_tuple(tup):
    dic = dict()
    for n in tup:
        dic[n] = dic.get(n,0)+1
    return tuple(dic.items())


# question 10
def rotate(tup,k):
    if not tup:
        return tup
    k = k % len(tup)
    
    part1 = tup[-k:]
    part2 = tup[:-k]

    return part1 + part2









