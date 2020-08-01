# FAB Quick Start - build views.py
__fab_quickstart__ generates Flask Application Builder `views.py` files, to create instant __multi-page__ apps (1 page per table) of __multi-table__ pages (includes `related_views` for related child data). 

The wiki is a [Quick Start for using FAB](https://github.com/valhuber/fab-quickstart/wiki).

This project contains 2 main folders:
1. `nw`: is a fab project for a sqlite version northwind (nw), for illustration and testing
1. `fab_quickstart` code (work in progress - see Explore, below).


## Background
[Flask Application Builder (FAB)](https://github.com/dpgaspar/Flask-AppBuilder) provides a rapid means for building web pages for database apps, based on Python and Flask ([QuickStart here](https://sites.google.com/view/app-logic-server/python-fab)).

FAB inputs are:

1. `models.py` file - describes your database tables.  You can build models with tools like [sqlacodegen](https://www.google.com/url?q=https%3A%2F%2Fpypi.org%2Fproject%2Fsqlacodegen%2F&sa=D&sntz=1&usg=AFQjCNHZ3ERjfnSO8MA8V20gzLjfeBaIxw).

1. `views.py` file - used by fab to generate pages.  It consists of segments like this, one for each page:

```
class OrderModelView(ModelView):
   datamodel = SQLAInterface(Order)
   list_columns = ["ShipName", "Customer.CompanyName", ... "EmployeeId", "CustomerId"]
   show_columns = ["ShipName", "Customer.CompanyName", "OrderDate", ... "ShipCountry", "Id", "EmployeeId", "CustomerId"]
   edit_columns = ["ShipName", "OrderDate",... "ShipCountry", "Id", "EmployeeId", "CustomerId"]
   add_columns = ["ShipName", "OrderDate", ... "ShipCountry", "Id", "EmployeeId", "CustomerId"]
   related_views = [OrderDetailModelView]

appbuilder.add_view(
      OrderModelView, "Order List", icon="fa-folder-open-o", category="Menu")
```


This project generates the `views.py` file from the `models.py` file, to save time and reduce learning curve.

## Key Features

1. Generate `views.py` with 1 class per (not ab_) table

    a. "Favorite" field (called "name", or contains "name") first
          
          Eg, List of Products - ProductName is more interesting than ProductId, so show it first
    
    b. Join Fields (join in parents' favorite field)
          
          Eg, List of Order + OrderDetails: show ProductName (not id)

    b. Numeric keyfields last

2. With Referenced for master/detail (e.g., Order before Customer)

    a. Generated child views first

3. Predictive Joins (e.g, ProductName on Order+OrderDetail

    a. Note - *not* generated for edit/show, else you get fab "key errors"



## Install

### Pre Reqs

To get started, you will need:

* Python3: run the windows installer; on mac/Unix, consider [using brew](https://opensource.com/article/19/5/python-3-default-mac#what-to-do)
* virtualenv - see [here](https://www.google.com/url?q=https%3A%2F%2Fpackaging.python.org%2Fguides%2Finstalling-using-pip-and-virtual-environments%2F%23creating-a-virtual-environment&sa=D&sntz=1&usg=AFQjCNEu-ZbYfqRMjNQ0D0DqU1mhFpDYmw)  (e.g.,  `pip install virtualenv`)


### Project Installation
open VSCode, and clone this repo.

In VSCode Python Debug Console:

```
virtualenv venv
# windows: .\venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
```

You must also choose your Python Interpreter (e.g., `.\venv\bin\python`).

Note: Windows Powershell requires privileges as described [here](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershel)


## Generate

Then, in VSCode, open the file `fab_quickstart/fab_quickstart.py`, and run it (e.g, under the debugger) using the launch config `FAB QuickStart Run`.

Copy the console output over the `nw/app/views.py` file.


## Run
```
cd nw
export FLASK_APP=app
flask run
```



## Explore

The main code is `fab_quickstart/fab_quickstart_base.py`.

For customizations, it is extended by its runnable subclass `fab_quickstart/fab_quickstart.py`

## Screenshot
    
![image](https://drive.google.com/uc?export=view&id=1Q3cG-4rQ6Q6RdZppvkrQzCDhDYHnk-F6)
