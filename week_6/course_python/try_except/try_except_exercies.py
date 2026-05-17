# question 1
def safe_int(s):
    try:
        return int(s)
    except ValueError,TypeError:
        return None
    

# question 2
def  safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "undefined"
    except TypeError:
        return None
    

# question 3
def read_first_line(path):
    try:
        with open(path, "r") as file:
            return file.readline()     
    except (FileNotFoundError,TypeError,ValueError):
        return None




# question 4
def get_value(d, key):
    try:
        return d[key]
    except KeyError,TypeError,ValueError:
        return "missing"
    

# question 5
def  parse_ints(values):
    new = []
    for i in values:
        try:
            new.append(int(i))
        except TypeError,ValueError:
            continue
    return new



# question 6
def set_age(age):
    try:
        if 0 > age or age > 150:
            raise ValueError
        return age
    except TypeError:
        None


# question 7
class InsufficientFundsError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw {amount}. Available balance is {balance}.")
    
    return balance - amount



# question 8
def retry(func, n):
    for i in range(n):
        try:
            return func()
        except Exception:
            if i == n - 1:
                raise


# question 9
def count_errors_short(funcs):
    def check_error(f):
        try:
            f()
            return 0  
        except Exception:
            return 1  

    return sum(check_error(func) for func in funcs)


# question 10
def load(path):
    try:
        with open(path, "r") as file:
            return int(file.readline())
            
    except Exception as original_error:
        raise RuntimeError("failed") from original_error