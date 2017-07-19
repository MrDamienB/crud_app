import csv

products = []

csv_file_path = "data/products.csv"

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

chosen_operation = input(menu)

#def list_products():
#    print("Product list")
#def show_product():
#    print("SHOWING A PRODUCT")
#def create_product():
#    print("CREATING A PRODUCT")
#def update_product():
#    print("UPDATING A PRODUCT")
#def destroy_product():
#    print("DESTROYING A PRODUCT")
#
#if chosen_operation == "List":
#    list_products()
#elif chosen_operation == "Show":
#    show_product()
#elif chosen_operation == "Create":
#    create_product()
#elif chosen_operation == "Update":
#    update_product()
#elif chosen_operation == "Destroy":
#    destroy_product()
#else: print("Oops, that option is not available. Please verify your entry.")
