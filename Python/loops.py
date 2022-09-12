favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    print('One of my favorite desserts is', dessert) # Example For loop.

    
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

count = 0 # Counter like variable necessary for termination of loop.

while count < len(favorites):
    print('One of my favorite desserts is', favorites[count]);
    count += 1 # Example While loop.


favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break 
else:
    print('No sorry, not a dessert on my list') #Controlling loops with If statement and break.
    
    favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']


for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert) #Controlling loops with "continue" (skip) and If statement.
    
    
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) #Controlling loops with "pass" and If statement.
