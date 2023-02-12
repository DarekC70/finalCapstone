
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost=cost
        self.quantity=quantity
        '''
        In this function, you must initialise the following attributes:
            selcountry,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity
        '''
        Add the code to return the quantity of the shoes.
        '''


    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f'''Shoe (The item {self.product} has code {self.code}, country of manufacture is {self.country},
                it's worth is {self.cost} and current stock is {self.quantity})'''
        


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []  # Create dictionary username: password
with open("inventory.txt", "r", encoding="utf-8-sig") as file:
# Assigning to variable 'lines' lines from file 'user.txt'
    for lines in file:
        temp = lines.strip()
        temp=temp.split(", ")
        print('***', temp)
        shoe_list.append(Shoe(temp[0],temp[1],temp[2],temp[3],temp[4]))
del shoe_list[0] # Remove the header from the loaded inventory.txt file
for shoe in shoe_list:
    print(shoe) 


#==========Functions outside the class==============
def read_shoes_data():
    try: 
        shoe_list = []  # Create dictionary username: password
        with open("inventory.txt", "r", encoding="utf-8-sig") as file:
        #shoe = open("inventory.txt", "r", encoding="utf-8-sig")
        # Assigning to variable 'lines' lines from file 'user.txt'

            for lines in file:
                temp = lines.strip()
                temp=temp.split(", ")
                print('***', temp)
                shoe_list.append(Shoe(temp[0],temp[1],temp[2],temp[3],temp[4]))
        del shoe_list[0] # Remove the header from the loaded inventory.txt file
        for shoe in shoe_list:
            print(shoe) 
    except:
        print('something went wrong!')
        return[]
        '''
        This function will open the file inventory.txt
        and read the data from this file, then create a shoes object with this data
        and append this object into the shoes list. One line in this file represents
        data to create one object of shoes. You must use the try-except in this function
        for error handling. Remember to skip the first line using your code.
        '''


def capture_shoes():
    country=input("Country: ")
    code=input("Code: ")
    product=input('Product: ')
    cost=input('Cost: ')
    quantity=input('Quantity: ')
    shoe_list.append(Shoe(country,code,product, cost, quantity))
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''


def view_all():
    for idx in range(len(shoe_list)):
        print(shoe_list[idx]) 
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python's tabulate module.
    '''


def re_stock():
    lowest_qty = 0
    for idx in range(len(shoe_list)):        
        if (int(shoe_list[idx].quantity) < int(shoe_list[lowest_qty].quantity)):            
            lowest_qty = idx
    
    print(shoe_list[lowest_qty])
    choice = input('Do you want to increase the stock value: Y - Yes or N - No ')
    if choice=='Y':
        shoe_list[lowest_qty].quantity=(input('Enter new stock: '))
        print('Incres stock: \n',shoe_list[lowest_qty])
        # new object add to file inventory
        with open("inventory.txt", "w", encoding="utf-8-sig") as file:
            file.write('Country, Code, Product, Cost, Quantity\n')
            for shoe in shoe_list:
                record=str(shoe.country +', '+ shoe.code +', '+ shoe.product +', '+ shoe.cost +', '+  shoe.quantity )
                file.write(record+'\n')
    else:
        print(shoe_list[lowest_qty])
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''


def search_shoe():
    shoe_code=input('Please enter the shoe code: ')
    for idx in range(len(shoe_list)): 
        if shoe_list[idx].code == shoe_code:             
            print(shoe_list[idx])
    else:
        print('Wrong code. Please try again!')
        shoe_code=input('Please enter the shoe code: ')
        for idx in range(len(shoe_list)): 
            if shoe_list[idx].code == shoe_code:
                print(shoe_list[idx])          
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''


def value_per_item():
    total_value=0
    for idx in range(len(shoe_list)):        
        total_value=(int(shoe_list[idx].cost) * int(shoe_list[idx].quantity))
        print(f'The total value for product: "{shoe_list[idx].product}" is: {total_value}')
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''


def highest_qty():
    highest_qty = 0
    for idx in range(len(shoe_list)):        
        if (int(shoe_list[idx].quantity) > int(shoe_list[highest_qty].quantity)):            
            highest_qty = idx
    
    print('The product with the highest quantity and recommended for sale is:\n', shoe_list[highest_qty])
               
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    menu = input('''Select one of the following Options below:
        so - Read shoe data/create shoe object;
        cds - Capture data shoe;
        va - Print the detailes of the shoe;
        lst - Shoe with the lowest stocke ==> to be re-stored;
        sc - Search shoe by the code;
        tvd - Display the total value for each item;
        hq - Shoe with the highest quantity ==> it has to sell
        e - Exit
            : ''').lower()

    if menu == 'so': # Read shoe data/create shoe object
        read_shoes_data()

    elif menu == 'cds': # Capture data of the shoe
        capture_shoes()

    elif menu == 'va': # Print the detailes of the shoe
        view_all()

    elif menu == 'lst': # Shows shoes with the lowest stock, recommendation for stock increase
        re_stock()
        
    elif menu == 'sc': # Search shoe by the code
        search_shoe()

    elif menu == 'tvd': # Display the total value for each item
        value_per_item()

    elif menu == 'hq':  # Shows shoes with the highest stock, recommendation for sale
        highest_qty()

    elif menu == 'e':  # Exit the program
        print('Goodbye!!!')
        exit()

    else:  # Display of a message about the wrong choice of menu option
        print("You have made a wrong choice, Please Try again")