# FAB Quick Start - build views.py
__fab_quickstart__ generates Flask Application Builder `views.py` files, to create instant multi-page, multi-table apps.

## Features
Generated fab pages look like as shown below:
1. __multi-page__ apps (1 page per table)
1. __multi-table__ pages (includes `related_views` for related child data)
1. __favorite field first__ first field is "name", or contains "name" (configurable)
1. __predictive joins__ favorite field of each parent is shown (product _name_ - not product _id_)
1. __ids last__ such boring fields are not shown on lists, last on view pages

![generated page](https://drive.google.com/uc?export=view&id=1Q3cG-4rQ6Q6RdZppvkrQzCDhDYHnk-F6)
See the wiki for a [Quick Start for using FAB](https://github.com/valhuber/fab-quickstart/wiki).


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


## Install
```diff
- Planned

```
```
cd <project>  # fab directory containing `config.py` file
pip install fab-quickstart
fab-quickstart
# copy generated output over your views.py file
```
Automated pip install is under construction.  Until complete, please follow the __Explore__ instructions, below.


## Explore

This project contains 2 main folders:
1. `nw`: is a fab project for a sqlite version northwind (nw), for illustration and testing.
It was built using the ([QuickStart procedure.](https://sites.google.com/view/app-logic-server/python-fab))
1. `fab_quickstart` code (work in progress - see Explore, below).
   1. The main code is `fab_quickstart/fab_quickstart_base.py`.   This is what you run, as described below.
   1. For customizations, it is extended by its runnable subclass `fab_quickstart/fab_quickstart.py`


### Pre Reqs

To get started, you will need:

* Python3: run the windows installer; on mac/Unix, consider [using brew](https://opensource.com/article/19/5/python-3-default-mac#what-to-do)
* virtualenv - see [here](https://www.google.com/url?q=https%3A%2F%2Fpackaging.python.org%2Fguides%2Finstalling-using-pip-and-virtual-environments%2F%23creating-a-virtual-environment&sa=D&sntz=1&usg=AFQjCNEu-ZbYfqRMjNQ0D0DqU1mhFpDYmw)  (e.g.,  `pip install virtualenv`)
* [VSCode](https://code.visualstudio.com) - any ide will do, though different install / generate / run instructions apply


### Project Installation
Open VSCode, and clone this repo.

In VSCode Python Debug Console:

```
virtualenv venv
# windows: .\venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
```

You must also choose your Python Interpreter (e.g., `.\venv\bin\python`).

Note: Windows Powershell requires privileges as described [here](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershel)


### Generate

Then, in VSCode, select Launch Config: `Python: Run Current File`,
and run any of:
* `fab_quickstart/fab_quickstart_ext.py`
* `fab_quickstart/cli.py`
* `fab_quickstart/fab_quickstart.py`

Or, in a terminal window:
```
cd nw
    
```

This provides optional overrides for extension, and calls `fab_quickstart/fab_quickstart_ext.py`.

Copy the console output over the `nw/app/views.py` file.


### Run generated fab app

Run the launch config `NW APP (Flask)'.

This is equivalent to:
```
cd nw
export FLASK_APP=app
flask run
```
