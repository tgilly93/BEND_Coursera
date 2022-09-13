items = [1,2,3,4,5]
item = items[6]
print(item)

items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except:
    print('Item does not exist in the list')
    
    
def divide_by(a, b):
    
    return a / b


ans = divide_by(40, 0)
print(ans)

def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0   
    except Exception as e:
        print(e, 'Cannot divide by zero')
        
ans = divide_by(40, 0)
print(ans)


with open('file_does_not_exist.txt', 'r') as file:
    print(file.read())

try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print('Unable to locate file')



    
