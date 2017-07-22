import csv

products = []
headers = ["id", "name", "aisle", "department", "price"]
user_input_headers = [header for header in headers if header != "id"] #using from professor's code.  I'm beginning to understand list comprehension, but still shaky.

def get_product_id(product): return int(product["id"])

def creat_new_pid():
    last_pid = map(get_product_id, products)
    return max(last_pid) + 1

csv_file_path = "data/products.csv"

def list_products():
    for product in products:
        print(product["id"], product['name'])
def show_product():
    while True:
        show_request = input("WOULD YOU LIKE TO LOOK UP AN ITEM (Y/N)?: ")
        if show_request == "N": break
        elif show_request == "Y":
            lookup = input("ENTER ID: ")
            product = [p for p in products if p["id"] == lookup][0]
            if product:
                print("READING PRODUCT HERE:",
                "\n", "        ID #: ",product["id"],
                "\n", "NAME @ PRICE: ",product["name"].title(), "@" ,'${0:.2f}'.format(float(product["price"])),
                "\n", "       AISLE: ", product["aisle"].title(),
                "\n", "  DEPARTMENT: ",product["department"].title())
            else:
                print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product)
        else: print("Please enter 'Y' for 'yes' or 'N' or 'no'")
def create_product():
    print("PLEASE PROVIDE THE NEW PRODUCT INFORMATION")
    new_product = {"id": creat_new_pid() }
    for header in user_input_headers:
        new_product[header] = input("The '{0}' is: ".format(header))
#    product_name = input("new product name:")
#    product_department = input("new product department:")
#    product_aisle = input("new product aisle:")
#    product_price = input("new product price:")
#    new_product = {
#        "id": product_id,
#        "name": product_name,
#        "aisle": product_aisle,
#        "department": product_department,
#        "price": product_price
#    }
    print("Review the new product you added:","\n",new_product)
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
    There are {0} products (Exit and reopen app to refresh product count)

    Please choose an operation:
    'List'    | Display a list of product identifiers
    'Show'    | Show information about a product
    'Create'  | Add a new product
    'Update'  | Edit an existing product
    'Destroy' | Delete an existing product

    Operation:""".format(len(products))

search = """
You can search via the following search keys:
{0}
Please enter your search key:
""".format(headers)

#new_products = "data/new_products.csv"
#with open(new_products, "w", newline='') as csv_file:
#    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
#    writer.writeheader()
#    for item in products:
#        writer.writerow(item)
#        print(item["id"], item["name"])

while True:
    chosen_operation = input(menu)
    if chosen_operation == "DONE":
        print("YOU HAVE EXITED THE APPLICATION")
        break
    elif chosen_operation == "List": list_products()
    elif chosen_operation == "Show": show_product()
    elif chosen_operation == "Create": create_product()
    elif chosen_operation == "Update": update_product()
    elif chosen_operation == "Destroy": destroy_product()
    else: print("Oops, that option is not available. Please verify your entry.")

with open(csv_file_path, "w", newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    writer.writeheader()
    for item in products:
        writer.writerow(item)
