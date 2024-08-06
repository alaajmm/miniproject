#Mini project
import csv

# Function to load products from a CSV file
def load_products_csv(products):
    product_list = []
    with open(products, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            product_list.append(row)
    return product_list

# Function to load orders from a CSV file
def load_orders_csv(orders):
    orders_list = []
    with open(orders, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            orders_list.append(row)
    return orders_list

# Function to load couriers from a CSV file
def load_couriers_csv(couriers):
    couriers_list = []
    with open(couriers, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            couriers_list.append(row)
    return couriers_list

# Data from CSV files assigned to variables
products_data = load_products_csv('products.csv')
orders = load_orders_csv('orders.csv')
couriers_data = load_couriers_csv('couriers.csv')

# Print main menu options
def print_main_menu():
    print("Main Menu:")
    print("0 - Orders")
    print("1 - Couriers")
    print("2 - View product menu")
    print("3 - Add product")
    print("4 - Delete product")
    print("5 - Update product")
    print("6 - Exit")
    print()

# Initialize order status list
order_status_list = ['PREPARING', 'READY', 'DELIVERED']

# Function to print orders menu
def print_orders_menu():
    print("\nOrders Menu:")
    print("0 - Return to Main Menu")
    print("1 - Print Orders")
    print("2 - Add New Order")
    print("3 - Update Order Status")
    print("4 - Update Existing Order ")
    print("5 - Delete Order ")
    print()

# Function to handle orders menu
def handle_orders_menu():
    while True:
        print_orders_menu()
        user_input = input("Select your option: ") #Asking user to input option.

        if user_input == '0':
            print('Returning to main menu.') #Returns the user to main menu.
            break
        elif user_input == '1':  #Print out all orders
            print('Orders List:')
            for i, order in enumerate(orders, start=1):
                print(f'{i}. Customer: {order["customer_name"]}, Status: {order["status"]}')
        elif user_input == '2': #Add a new order
            customer_name = input('Enter customer name: ')
            customer_address = input('Enter customer address: ')
            customer_phone = input('Enter customer phone number: ')
            order = {
                "customer_name": customer_name,
                "customer_address": customer_address,
                "customer_phone": customer_phone,
                "status": "PREPARING"
            }
            orders.append(order) #Appending csv file orders to make the change
            print('Order added successfully.')
        elif user_input == '3': #Update the order status
            print('Orders List:')
            for i, order in enumerate(orders, start=1):
                print(f'{i}. Customer: {order["customer_name"]}, Status: {order["status"]}')
            order_index = int(input('Enter the order index: '))
            if 1 <= order_index <= len(orders):
                print('Order Status List:')
                for i, status in enumerate(order_status_list, start=1):
                    print(f'{i}. {status}')
                status_index = int(input('Enter the status index: '))
                if 1 <= status_index <= len(order_status_list):
                    orders[order_index - 1]["status"] = order_status_list[status_index - 1]
                    print('Order status updated successfully.')
                else:
                    print('Invalid status index.')
            else:
                print('Invalid order index.')
        elif user_input == '4':  #Using indexes to update existing orders.
            print('Existing orders:')
            for i, order in enumerate(orders, start=1):
                print(f'{i}. Customer: {order["customer_name"]}, Status: {order["status"]}')
            order_index = int(input('Enter the order index to update: '))
            if 1 <= order_index <= len(orders):
                customer_name = input('Enter new customer name: ')
                customer_address = input('Enter new customer address: ')
                customer_phone = input('Enter new customer phone number: ')
                orders[order_index - 1].update({
                    "customer_name": customer_name,
                    "customer_address": customer_address,
                    "customer_phone": customer_phone
                })
                print('Order updated successfully.')
            else:
                print('Invalid order index.')
        elif user_input == '5': #Using indexes to remove order.
            print('Orders List:')
            for i, order in enumerate(orders, start=1):
                print(f'{i}. Customer: {order["customer_name"]}, Status: {order["status"]}')
            order_index = int(input('Enter the order index to delete: '))
            if 1 <= order_index <= len(orders):
                deleted_order = orders.pop(order_index - 1)
                print(f'Deleted order for {deleted_order["customer_name"]}.')
            else:
                print('Invalid order index.')
        else:
            print('Invalid option. Please try again.')

# Print courier menu
def print_courier_menu():
    print("\nCourier Menu:")
    print("0 - Exit to Main Menu")
    print("1 - Print Courier List")
    print("2 - Create New Courier")
    print("3 - Update Existing Courier")
    print("4 - Delete Courier")
    print()

# Handle courier menu
def handle_courier_menu():
    while True:
        print_courier_menu()
        user_input = input("Select your option: ") #Asking user to input option.
        if user_input == '0':
            print("Returning to main menu")
            break
        elif user_input == '1': #Printing courier list.
            print('Courier List:')
            for i, courier in enumerate(couriers_data, start=1):
                print(f'{i}. {courier}')
        elif user_input == '2': #User can input additional courier.
            courier_name = input('Enter courier name: ')
            couriers_data.append([courier_name])
            print(f'Courier {courier_name} added successfully.')
        elif user_input == '3': #Using indexes to allow user to update their courier list.
            print('Couriers List:')
            for i, courier in enumerate(couriers_data, start=1):
                print(f'{i}. {courier}')
            courier_index = int(input('Enter the courier index to update: '))
            if 1 <= courier_index <= len(couriers_data):
                new_name = input('Enter new courier name: ')
                couriers_data[courier_index - 1] = [new_name]
                print('Courier updated successfully.')
            else:
                print('Invalid courier index.')
        elif user_input == '4': #Allowing user to remove courier from list.
            print('Couriers List:')
            for i, courier in enumerate(couriers_data, start=1):
                print(f'{i}. {courier}')
            courier_index = int(input('Enter the courier index to delete: '))
            if 1 <= courier_index <= len(couriers_data):
                deleted_courier = couriers_data.pop(courier_index - 1)
                print(f'Deleted courier {deleted_courier}.')
            else:
                print('Invalid courier index.')
        else:
            print('Invalid option. Please try again.') 

# Main function (Main menu)
def main():
    while True:
        print_main_menu()
        user_input = input("Select your option: ") #This is where the user begins and each option will take the user to a different function.

        if user_input == '0': #  This will take user to orders menu.
            handle_orders_menu() 
        elif user_input == '1':# This will take user to products menu.
            handle_courier_menu()
        elif user_input == '2': # This will allow user to view product menu.
            print('Products Menu:')
            for product in products_data:
                print(f'- {product}')
        elif user_input == '3': # This will allow user to add a new product to menu.
            new_product = input('Enter the name of the new product: ')
            products_data.append([new_product])
            print(f'{new_product} has been added to the product list.')
        elif user_input == '4':
            print('Products List:')
            for i, product in enumerate(products_data, start=1):
                print(f'{i}. {product}')
            delete_index = int(input('Enter the product index to delete: '))
            if 1 <= delete_index <= len(products_data):
                deleted_product = products_data.pop(delete_index - 1)
                print(f'{deleted_product} has been removed from the list.')
            else:
                print('Invalid product index.')
        elif user_input == '5':
            print('Products List:')
            for i, product in enumerate(products_data, start=1):
                print(f'{i}. {product}')
            update_index = int(input('Enter the number of the product you would like to update: '))
            if update_index.isdigit() and 1 <= int(update_index) <= len(products_data):
                updated_product = input(f'What would you like to change "{products_data[int(update_index) - 1]}" to? ')
                products_data[int(update_index) - 1] = [updated_product]
                print(f'Product updated. New list: {products_data}')
            else:
                print('Error: Invalid selection. Please try again.')
        elif user_input == '6':
            print('Exiting app')
            break
        else:
            print('Invalid option. Please try again.')

# Run the program
if __name__ == "__main__":
    main()