# 1. Use the import statement to import a built-in package in Python. 2. Use the import statement to call a function present in another Python file.
import json
from Python.employee import details, employee_name, age, title

def create_dict(name, age, title):
    employee_dict = {
        "first_name": str(name),
        "age" : int(age),
        "title" : str(title)
    }
    json_obj = json.dumps(employee_dict)
    return employee_dict

def write_json_to_file(json_obj, output_file):
    newfile = open(output_file, 'w')
    newfile.write(str(json_obj))
    newfile.close()
    return