#========The beginning of the class==========
# shoe class with attributes: country, code, product, cost and quantity
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    # function to return cost of a shoe
    def get_cost(self):
        return self.cost


    # function to return shoes quantity
    def get_quantity(self):
        return self.quantity


    # function to return a string representing a shoe product
    def __str__(self):
        return self.product


#=============Shoe list===========

# create an ampty shoe_list arrey to store a list of objects of shoes.
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    shoe_list = []
    # open the file inventory.txt
    try:
        inventory_file = open("inventory.txt", "r")
        inventory_data = inventory_file.readlines()
        # create a shoes object with this data and append this object into the shoes list
        for line in inventory_data[1:]:
            line_list = line.split(",")
            shoe_list.append(Shoe(line_list[0], line_list[1], line_list[2], line_list[3], int(line_list[4])))
        return shoe_list
    # avoid file not found error
    except FileNotFoundError:
        print("This file doesn't exists")


def capture_shoes(shoe_list):
    input_country = input("Shoe country: ")
    input_code = input('Shoe code: ')
    input_name = input("Shoe product name: ")
    input_price = int(input("Shoe Price: "))
    input_quantity = int(input("Shoe quantity in storage: "))
    shoe_list.append(Shoe(input_country,input_name,input_code,input_price,input_quantity))
    return shoe_list


# iterate over the shoes list and  print the details
def view_all(shoes):
    for shoe in shoes:
        print(shoe)


# identify shoe object with the lowest quantity
# ask the user if they want to add and update it
def re_stock(shoes):
    min_shoe = shoes[0]
    for item in shoes:
        if item.quantity < min_shoe.quantity:
            min_shoe = item
    print(f'{min_shoe} in stock: {min_shoe.quantity}')

    add_stock = int(input("Number of shoes to add in stock: "))
    new_quantity = str(min_shoe.quantity + add_stock)
    print(f'New stock quantity: {new_quantity}')

    # write on the inventiry txt file ne updated quantity
    inventory_file = open("inventory.txt", "w+")
    inventory_file.write("Country,Code,Product,Cost,Quantity\n")

    for item in shoe_list:
        if item.code == min_shoe.code:
            item.quantity = new_quantity
        inventory_file.write(f"{item.country},{item.code},{item.product},{item.cost},{item.quantity}\n")
    inventory_file.close()


# search for a shoe from the list using the shoe code
# return and print the shoe
def search_shoe(shoes):
    shoe_code = input('Shoe code to search: ')
    for item in shoes:
        if item.code == shoe_code:
            return item


# function to calculate total value of each shoe
# print total value for each shoe
def value_per_item(shoes):
    item_value = shoes[0]
    for item in shoes:
        item_value = int(item.cost) * int(item.quantity)
        print(f'{item} value: {item_value}\n')


# function to find the shoes with the highest quantity in stock
# print this shoe as on SALE
def highest_qty(shoes):
    heighst_quantity = shoes[0]
    for item in shoes:
        if item.quantity > heighst_quantity.quantity:
            heighst_quantity = item
    print(f'\n{heighst_quantity} now on SALE!')


#==========Main Menu=============
# Create a menu that executes each function above.
while True:
    # presenting the menu to the user
    # making sure that the user input is coneverted to lower case.
    menu = int(input('''\nSelect one of the following Options below:
1 - Read shoes inventory
2 - Capture shoe
3 - View all shoes
4 - Restock
5 - Search shoe
6 - Total value per shoe
7 - Highest shoe stock 
8 - Exit
Selected option: '''))

    if menu == 1:
        shoe_list = read_shoes_data()
    elif menu == 2:
        shoe_list = capture_shoes(shoe_list)
    elif menu == 3:
        view_all(shoe_list)
    elif menu == 4:
        re_stock(shoe_list)
    elif menu == 5:
        item = search_shoe(shoe_list)
        print(f"\nCountry: {item.country}\nCode: {item.code}\nProduct name: {item.product}\nPrice: {item.cost}\nQuantity in Stock: {item.quantity}")
    elif menu == 6:
        value_per_item(shoe_list)
    elif menu == 7:
        highest_qty(shoe_list)
    elif menu == 8:
        print("Thank you bye!!!")
        exit()
    else:
        print("This is not an option!")