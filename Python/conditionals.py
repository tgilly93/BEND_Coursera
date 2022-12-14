current = False

if current:
    current = False
    print('Turning light off') 

if not current:
    current = True
    print('Turning light on') # IF statement.
    
    current = False

if current:
    current = False
    print('Turning light off')
else: 
    current = True
    print('Turning light on') # More efficient statement using "If/Else".
    
    loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill)) # Elif multiple condition statement,

http_status = 501

match http_status:
    case 200 | 201:
        print('Success')
    case 400:
        print('Bad Request')
    case 500 | 501:
        print('Server Error')
    case _:
        print('Unknown') # Example elif conditional using Match/case.