# this is the list of customer orders, each order is represented as a tuple containing the customer name, product name, price, and category
customer_orders = [
    ("John Smith", "Laptop", 1249.99, "Electronics"),
    ("Jane Doe", "T-shirt", 9.99, "Clothing"),
    ("Michael Johnson", "Coffee Maker", 89.50, "Home & Kitchen"),
    ("Emily Davis", "Mystery Novel", 9.99, "Books"),
    ("James Wilson", "Smartphone", 1099.00, "Electronics"),
    ("Sarah Brown", "Jeans", 64.99, "Clothing"),
    ("David Miller", "Cookware Set", 179.99, "Home & Kitchen"),
    ("Jessica Taylor", "Fantasy Novel", 18.50, "Books"),
    ("Robert Anderson", "Headphones", 249.99, "Electronics"),
    ("Ashley Thomas", "Sneakers", 89.99, "Clothing"),
    ("William Jackson", "Vacuum Cleaner", 329.00, "Home & Kitchen"),
    ("Amanda White", "Cookbook", 9.99, "Books"),
    ("Richard Harris", "Camera", 1399.00, "Electronics"),
    ("Jennifer Martin", "Sweater", 59.99, "Clothing"),
    ("Joseph Thompson", "Table Lamp", 74.50, "Home & Kitchen"),
    ("Elizabeth Garcia", "Biography", 22.99, "Books"),
    ("Thomas Martinez", "Tablet", 549.99, "Electronics"),
    ("Stephanie Robinson", "Jacket", 149.00, "Clothing"),
    ("Charles Clark", "Bed Sheets", 89.99, "Home & Kitchen"),
    ("Nicole Rodriguez", "Science Textbook", 119.50, "Books"),
    ("Christopher Lewis", "Laptop", 1899.00, "Electronics"),
    ("Melissa Lee", "T-shirt", 9.99, "Clothing"),
    ("Daniel Walker", "Coffee Maker", 129.99, "Home & Kitchen"),
    ("Rebecca Hall", "Mystery Novel", 12.50, "Books"),
    ("Matthew Allen", "Smartphone", 799.99, "Electronics"),
    ("Laura Young", "Jeans", 79.50, "Clothing"),
    ("Anthony Hernandez", "Cookware Set", 249.99, "Home & Kitchen"),
    ("Michelle King", "Fantasy Novel", 16.99, "Books"),
    ("Mark Wright", "Headphones", 179.00, "Electronics"),
    ("Kimberly Lopez", "Sneakers", 119.99, "Clothing"),
    ("John Smith", "Coffee Maker", 59.99, "Home & Kitchen"),
    ("Jane Doe", "Cookbook", 10.50, "Books"),
    ("Michael Johnson", "Camera", 1049.99, "Electronics"),
    ("Emily Davis", "Sweater", 15.99, "Clothing"),
    ("James Wilson", "Table Lamp", 45.00, "Home & Kitchen"),
    ("Sarah Brown", "Biography", 18.99, "Books"),
    ("David Miller", "Tablet", 699.00, "Electronics"),
    ("Jessica Taylor", "Jacket", 189.99, "Clothing"),
    ("Robert Anderson", "Bed Sheets", 129.50, "Home & Kitchen"),
    ("Ashley Thomas", "Science Textbook", 89.99, "Books"),
    ("William Jackson", "Laptop", 1499.99, "Electronics"),
    ("Amanda White", "T-shirt", 14.99, "Clothing"),
    ("Richard Harris", "Vacuum Cleaner", 449.99, "Home & Kitchen"),
    ("Jennifer Martin", "Mystery Novel", 9.99, "Books"),
    ("Joseph Thompson", "Smartphone", 1299.00, "Electronics"),
    ("Elizabeth Garcia", "Jeans", 54.99, "Clothing"),
    ("Thomas Martinez", "Coffee Maker", 99.00, "Home & Kitchen"),
    ("Stephanie Robinson", "Fantasy Novel", 21.50, "Books"),
    ("Charles Clark", "Headphones", 329.99, "Electronics"),
    ("Nicole Rodriguez", "Sneakers", 74.50, "Clothing"),
    ("Christopher Lewis", "Cookware Set", 199.00, "Home & Kitchen"),
    ("Melissa Lee", "Cookbook", 19.99, "Books"),
    ("Daniel Walker", "Camera", 1799.00, "Electronics"),
    ("Rebecca Hall", "Sweater", 49.99, "Clothing"),
    ("Matthew Allen", "Table Lamp", 89.99, "Home & Kitchen"),
    ("Laura Young", "Biography", 31.00, "Books"),
    ("Anthony Hernandez", "Tablet", 399.99, "Electronics"),
    ("Michelle King", "Jacket", 129.50, "Clothing"),
    ("Mark Wright", "Bed Sheets", 69.99, "Home & Kitchen"),
    ("Kimberly Lopez", "Science Textbook", 139.99, "Books"),
    ("John Smith", "Laptop", 1249.99, "Electronics"),
    ("Jane Doe", "T-shirt", 24.99, "Clothing"),
    ("Michael Johnson", "Coffee Maker", 89.50, "Home & Kitchen"),
    ("Emily Davis", "Mystery Novel", 14.99, "Books"),
    ("James Wilson", "Smartphone", 1099.00, "Electronics"),
    ("Sarah Brown", "Jeans", 64.99, "Clothing"),
    ("David Miller", "Cookware Set", 179.99, "Home & Kitchen"),
    ("Jessica Taylor", "Fantasy Novel", 18.50, "Books"),
    ("Robert Anderson", "Laptop", 1699.99, "Electronics"),
    ("Ashley Thomas", "Sneakers", 89.99, "Clothing"),
    ("William Jackson", "Vacuum Cleaner", 329.00, "Home & Kitchen"),
    ("Amanda White", "Cookbook", 27.99, "Books"),
    ("Richard Harris", "Camera", 1399.00, "Electronics"),
    ("Jennifer Martin", "Sweater", 59.99, "Clothing"),
    ("Joseph Thompson", "Table Lamp", 74.50, "Home & Kitchen"),
    ("Elizabeth Garcia", "Biography", 22.99, "Books"),
    ("Thomas Martinez", "Tablet", 549.99, "Electronics"),
    ("Stephanie Robinson", "Jacket", 149.00, "Clothing"),
    ("Charles Clark", "Bed Sheets", 89.99, "Home & Kitchen"),
    ("Nicole Rodriguez", "Science Textbook", 119.50, "Books"),
    ("Christopher Lewis", "Headphones", 289.99, "Electronics"),
    ("Melissa Lee", "T-shirt", 19.99, "Clothing"),
    ("Daniel Walker", "Coffee Maker", 129.99, "Home & Kitchen"),
    ("Rebecca Hall", "Mystery Novel", 12.50, "Books"),
    ("Matthew Allen", "Smartphone", 1199.00, "Electronics"),
    ("Laura Young", "Jeans", 79.50, "Clothing"),
    ("Anthony Hernandez", "Cookware Set", 249.99, "Home & Kitchen"),
    ("Michelle King", "Fantasy Novel", 16.99, "Books"),
    ("Mark Wright", "Laptop", 1399.00, "Electronics"),
    ("Kimberly Lopez", "Sneakers", 119.99, "Clothing"),
    ("John Smith", "Coffee Maker", 59.99, "Home & Kitchen"),
    ("Jane Doe", "Cookbook", 32.50, "Books"),
    ("Michael Johnson", "Camera", 1049.99, "Electronics"),
    ("Emily Davis", "Sweater", 74.99, "Clothing"),
    ("James Wilson", "Table Lamp", 45.00, "Home & Kitchen"),
    ("Sarah Brown", "Biography", 18.99, "Books"),
    ("David Miller", "Tablet", 699.00, "Electronics"),
    ("Jessica Taylor", "Jacket", 189.99, "Clothing"),
    ("Robert Anderson", "Bed Sheets", 129.50, "Home & Kitchen"),
    ("John Smith", "Sweater", 24.99, "Clothing"),
]

# function to create a list of unique customer names from the customer_orders list
def get_unique_customers(orders):
    return list(set(order[0] for order in orders))  

# function to create a dictionaary where keys are customer names and values are lists of order details in tuples
def get_customer_orders(orders):
    customer_orders_dict = {}
    for order in orders:
        customer_name = order[0]
        if customer_name not in customer_orders_dict:
            customer_orders_dict[customer_name] = []
        customer_orders_dict[customer_name].append(order)
    return customer_orders_dict

# function to create a dictionary to map each product to its category
def get_product_categories(orders):
    product_categories = {}
    for order in orders:
        product_name = order[1]
        category = order[3]
        product_categories[product_name] = category
    return product_categories

# function to create a set of unique product categories from the customer_orders list
def get_unique_categories(orders):
    return set(order[3] for order in orders)    


# function to display all available product categories using the get_unique_categories function
def display_product_categories(orders):
    categories = get_unique_categories(orders)
    print("Available Product Categories:")
    for category in categories:
        print(f"- {category}")
    print()

# function to calculate the total amount each customer has spent on their orders
def calculate_total_spent(orders):
    total_spent = {}
    for order in orders:
        customer_name = order[0]
        price = order[2]
        if customer_name not in total_spent:
            total_spent[customer_name] = 0
        total_spent[customer_name] += price
    return total_spent

# function to display the total amount spent by each customer using the calculate_total_spent function
def display_total_spent(orders):
    total_spent = calculate_total_spent(orders)
    print("Total Amount Spent by Each Customer:")
    for customer, amount in total_spent.items():
        print(f"{customer}: ${amount:.2f}")
    print()


# function to classify customers based on their total spending into categories: "Low Spender", "Medium Spender", and "High Spender"
def classify_customers_by_spending(orders):
    total_spent = calculate_total_spent(orders)
    customer_classification = {}
    for customer, amount in total_spent.items():
        if amount < 100:
            customer_classification[customer] = "Low Spender"
        elif 100 <= amount < 500:
            customer_classification[customer] = "Medium Spender"
        else:
            customer_classification[customer] = "High Spender"
    return customer_classification  

# function to display the classification of each customer based on their total spending using the classify_customers_by_spending function
def display_customer_classification(orders):
    customer_classification = classify_customers_by_spending(orders)
    print("Customer Classification Based on Spending:")
    for customer, classification in customer_classification.items():
        print(f"{customer}: {classification}")
    print()

# function to calculate total spent by category stored in a dictionary where keys are categories and values are total amounts spent in those categories
def calculate_total_spent_by_category(orders):
    total_spent_by_category = {}
    for order in orders:
        category = order[3]
        price = order[2]
        if category not in total_spent_by_category:
            total_spent_by_category[category] = 0
        total_spent_by_category[category] += price
    return total_spent_by_category

# function to display the total amount spent in each product category using the calculate_total_spent_by_category function
def display_total_spent_by_category(orders):
    total_spent_by_category = calculate_total_spent_by_category(orders)
    print("Total Amount Spent by Category:")
    for category, amount in total_spent_by_category.items():
        print(f"{category}: ${amount:.2f}")
    print()


# function to extract the unique products from all orders and return them as a set
def get_unique_products(orders):
    return set(order[1] for order in orders)    

# function takes a categoary as input and uses list comprehension to return a list of customers who have purchased products in that category
def get_customers_by_category(orders, category):
    return list(set(order[0] for order in orders if order[3] == category))

def get_electronics_customers():
    return get_customers_by_category(customer_orders, "Electronics")

# function to display the unique list of customers who have purchased products in the "Electronics" category using the get_electronics_customers function
def display_electronics_customers():
    electronics_customers = get_electronics_customers()
    print("Customers who purchased Electronics:")
    for customer in electronics_customers:
        print(f"- {customer}")
    print()
# function to find the top three spending customers using sorting
def get_top_spending_customers(orders):
    total_spent = calculate_total_spent(orders)
    sorted_customers = sorted(total_spent.items(), key=lambda x: x[1], reverse=True)
    return sorted_customers[:3]

# function to display the top three spending customers using the get_top_spending_customers function
def display_top_spending_customers():
    top_customers = get_top_spending_customers(customer_orders)
    print("Top 3 Spending Customers:")
    for customer, amount in top_customers:
        print(f"{customer}: ${amount:.2f}")
    print()


# function to display a summary of each customer including their total spending and classification based on spending
def display_customer_summary(orders):
    total_spent = calculate_total_spent(orders)
    customer_classification = classify_customers_by_spending(orders)
    print("Customer Summary:")
    for customer in total_spent:
        amount = total_spent[customer]
        classification = customer_classification[customer]
        print(f"{customer}: Total Spent: ${amount:.2f}, Classification: {classification}")
    print()


# function to find customers who have purchased products in multiple categories using set operations
def get_customers_with_multiple_categories(orders):
    customer_categories = {}
    for order in orders:
        customer_name = order[0]
        category = order[3]
        if customer_name not in customer_categories:
            customer_categories[customer_name] = set()
        customer_categories[customer_name].add(category)
    
    return [customer for customer, categories in customer_categories.items() if len(categories) > 1]        


# function that takes the orders list and two categories as input and returns the list of customers who have purchased products in both categories using set operations
def get_customers_in_both_categories(orders, category1, category2):
    customers_category1 = set(get_customers_by_category(orders, category1))
    customers_category2 = set(get_customers_by_category(orders, category2))
    return list(customers_category1.intersection(customers_category2))  

# function to return the list of customers who have purchased products in both "Electronics" and "Clothing" categories using the get_customers_in_both_categories function
def get_customers_in_electronics_and_clothing():
    return get_customers_in_both_categories(customer_orders, "Electronics", "Clothing")

# function to display the list of customers who have purchased products in both "Electronics" and "Clothing" categories using the get_customers_in_electronics_and_clothing function
def display_customers_in_electronics_and_clothing():
    customers = get_customers_in_electronics_and_clothing()
    print("Customers who purchased both Electronics and Clothing:")
    for customer in customers:
        print(f"- {customer}")
    print()


        


# function to add a new order for a specific customer to the customer_orders list
def add_order(orders, customer_name, order):
    if order[0] != customer_name:
        raise ValueError("The order's customer name must match customer_name.")

    orders.append(order)    


# function to show all orders for a specific customer using the get_customer_orders function
def show_customer_orders(customer_name):
    customer_orders_dict = get_customer_orders(customer_orders)
    if customer_name in customer_orders_dict:
        orders = customer_orders_dict[customer_name]
        print(f"Orders for {customer_name}:")
        for order in orders:
            print(f"- Product: {order[1]}, Price: ${order[2]:.2f}, Category: {order[3]}")
    else:
        print(f"No orders found for {customer_name}.")
    print()

# create a function to print to console a short paragraph describing the customer orders data and the functionality of the program
def describe_program():
    print("This program manages customer orders for various products across different categories.")
    print("It allows you to view unique customers, their orders, total spending, and classifications based on spending.")
    print("You can also see the total amount spent by category, customers who purchased specific categories, and top spending customers.")
    print("Additionally, you can add new orders and view summaries of customer activity.")
    print()


# function to display customers who ordered more than $1000 in total using the calculate_total_spent function
def display_high_spending_customers():
    total_spent = calculate_total_spent(customer_orders)
    high_spenders = {customer: amount for customer, amount in total_spent.items() if amount > 1000}
    
    print("Customers who spent more than $1000:")
    for customer, amount in high_spenders.items():
        print(f"{customer}: ${amount:.2f}")
    # add a blank line for better readability
    print()





# Main function to demonstrate the functionality of the above functions
def main():

    # describe the program
    describe_program()

    # show adding a customer order to the list
    # add and order for customer "John Smith" for a new product "Smartwatch" in the "Electronics" category with a price of $199.99
    add_order( customer_orders,"John Smith",("John Smith", "Smartwatch", 199.99, "Electronics"),)
    
    # show all orders for a specific customer should show the smartwatch order added above
    #show_customer_orders("John Smith")  
    # will show with entire list of orders later.

    # Display customer classification based on spending
    display_customer_classification(customer_orders)

    # Display total amount spent by category
    display_total_spent_by_category(customer_orders)


    # Display unique customers
    unique_customers = get_unique_customers(customer_orders)
    print("Unique Customers:")
    for customer in unique_customers:
        print(f"- {customer}")
    print()

    # Display customer orders
    customer_orders_dict = get_customer_orders(customer_orders)
    print("Customer Orders:")
    for customer, orders in customer_orders_dict.items():
        print(f"{customer}:")
        for order in orders:
            print(f"  - Product: {order[1]}, Price: ${order[2]:.2f}, Category: {order[3]}")
    print()

    # Display product categories
    display_product_categories(customer_orders)
    print()

    # Display total amount spent by each customer
    display_total_spent(customer_orders)
    print()

    # Display customers who purchased Electronics
    display_electronics_customers()

    # Display top three spending customers
    display_top_spending_customers()

    # Display customer summary
    display_customer_summary(customer_orders)

    # Display customers who purchased both Electronics and Clothing
    display_customers_in_electronics_and_clothing()

    # Display customers who spent more than $1000
    display_high_spending_customers()
    print()






# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()  

