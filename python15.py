# All-in-One Exception Handling Example

try:
    # ValueError
    num = int("abc")  
    
    # ZeroDivisionError
    div = 10 / 0  
    
    # IndexError
    lst = [1, 2, 3]
    print(lst[5])  
    
    # KeyError
    d = {"a": 1}
    print(d["b"])  
    
    # TypeError
    result = "5" + 5  
    
    # FileNotFoundError
    f = open("nofile.txt")  
    
except ValueError:
    print("Error: Invalid value type!")
except ZeroDivisionError:
    print("Error: Division by zero!")
except IndexError:
    print("Error: List index out of range!")
except KeyError:
    print("Error: Key not found in dictionary!")
except TypeError:
    print("Error: Wrong type operation!")
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print("Unexpected Error:", e)
finally:
    print("Program execution finished.")
