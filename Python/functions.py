#Calculate total tax without function
bill = 175.00
tax_rate = 15
total_tax = (bill * tax_rate) / 100.00 
print('Total tax', total_tax)

#Create function to find total tax
def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2)

print(calculate_tax(150.00, 20)) #function can be passed any random values to parameters and return tax.

