#List Comprehension syntax
#[ <expression> for x in <sequence> if <condition>] 
data = [2,3,5,7,11,13,17,19,23,29,31]
data = [x+3 for x in data]
print("Updating the list: ", data)# update list

new_data = [x*2 for x in data]
print("Creating new list: ", new_data)#new list

fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)# list with If condition

nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)# using range function


#Dictionary Comprehension syntax
#dict = { key:value for key, value in <sequence> if <condition> } 
#new_dict ={key:value for (key, value) in zip(list1, list2)} (two lists)
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)#dictionary using one list

months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)#dictionary using two lists


#Set Comprehension
#similar to list comprehension but use curly braces instead of brackets.
set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)


#Generator Comprehension
#similar to lists, uses parentheses, and object is produced to iterate over.
data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")
    

employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

#using the map() function to apply mod() to all elements within employee_list. Assign the result of it to a new variable called map_emp. Convert map_emp to a list and return it.
def to_mod_list(employee_list):
    map_emp = map(mod, employee_list)
    end_list = [x for x in map_emp]
    return end_list

#using list comprehension and the replace() over mod_list to replace all spaces (" ") with underscores ("_"). Return the resulting list.
def generate_usernames(mod_list):
    new_list = [x.replace(" ", "_") for x in mod_list]
    return new_list

#using dictionary comprehension over the employee_list to create a dictionary where each key is the first letter of an employee's name and the value is the employee's ID.
def map_id_to_initial(employee_list):
    new_dict = {}
    for x in employee_list:
      new_dict = {x['name'][0] : x['id'] for x in employee_list}
      return new_dict 