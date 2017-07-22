import csv

products = []

csv_file_path = "data/products.csv"

def list_products():
    for product in products:
        print(product["id"], product['name'])
def show_product():
    print("SHOWING A PRODUCT")
def create_product():
    print("CREATING A PRODUCT")
    product_name = input("new product name:")
    product_id = input("new product id:")
    product_department = input("new product department:")
    product_aisle = input("new product aisle:")
    product_price = input("new product price:")
    new_product = {
        "id": product_id,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print(new_product)
    products.append(new_product)
#    print(products)
def update_product():
    print("UPDATING A PRODUCT")
def destroy_product():
    print("DESTROYING A PRODUCT")

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)
#        print(row["id"], row["name"])

print("-----------------------------------","\n","PRODUCTS APPLICATION", '\n'"-----------------------------------")
print("Welcome mrdamienb")

menu = """
    There are {0} products

    Please choose an operation:
    'List'    | Display a list of product identifiers
    'Show'    | Show information about a product
    'Create'  | Add a new product
    'Update'  | Edit an existing product
    'Destroy' | Delete an existing product

    Operation:""".format(len(products))

#new_products = "data/new_products.csv"
#with open(new_products, "w", newline='') as csv_file:
#    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
#    writer.writeheader()
#    for item in products:
#        writer.writerow(item)
#        print(item["id"], item["name"])

chosen_operation = input(menu)

if chosen_operation == "List":
    list_products()
elif chosen_operation == "Show":
    show_product()
elif chosen_operation == "Create":
    create_product()
elif chosen_operation == "Update":
    update_product()
elif chosen_operation == "Destroy":
    destroy_product()
else: print("Oops, that option is not available. Please verify your entry.")

with open(csv_file_path, "w", newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    writer.writeheader()
    for item in products:
        writer.writerow(item)
