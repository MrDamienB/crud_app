# THE SIMPLE PRODUCT INVENTORY MANAGER

This application will help you manage simple inventories and allow you the ability to update
current and new products.  You can also look up products by their id number to ensure no two products are created with the same product id number.

## Installation

Download the source code to a local directory on the machine where you want to run the app:

```shell
git clone https://github.com/MrDamienB/crud_app
cd some/path/to/repo/
```

Finally, download the [example `products.csv` file] (https://raw.githubusercontent.com/MrDamienB/crud_app/master/data/products.csv) and save it as `data/products.csv`.

Once familiar with the app and how to add/edit/delete products, you can use this file
as a template to begin logging all of your products.

## Usage
To run the app, navigate to the directory where you saved the app file during "Installation".
In this early version of the app, you will notice a product count on  the main menu.  This
product count is dynamic and will report how many products you have saved in your data file, or
product log.  However, it only updates each time you begin the app.  So if you are making
multiple changes, please sign out of the app via the "DONE" command and restart the app.  The
count will update.  We look forward to releasing a patch soon that will update the count without
having to restart the program.

```shell
python app/products_app.py
```
All options in the app have a menu.  If at anytime you make an entry that the app does not
recognize, you will be prompted to re-enter your desire command.  Both the "Create" and "Destroy"
commands will ask you to verify or confirm before completing the action.  It is important to
complete the confirmation or the change will not be saved.
