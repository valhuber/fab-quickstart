Flask App Builder - Quick Start
===============================

Create `Flask App Builder <www.github.com/dpgaspar/Flask-AppBuilder>`_ ``views.py`` file,
directly from ``models.py``, for an instant multi-page, multi-table app.

Use this `Quick Start <www.github.com/valhuber/fab-quickstart/wiki>`_ to create the app shown below in 10 minutes.


Change Log
----------

Initial Version

Usage:
------
First, create a fab project (e.g., see the `Quick Start <www.github.com/valhuber/fab-quickstart/wiki>`_).

Then, generate the ``views.py`` file like this::

    pip install -i https://test.pypi.org/simple/ FAB-Quickstart==0.9.0
    fabqs

Copy the console output to your `views.py` file, and run fab / flask app.

Features:
---------

Normally, you hand-code segments like this in the ``views.py`` file for each page,
like this: ::

    class OrderModelView(ModelView):
        datamodel = SQLAInterface(Order)
        list_columns = ["ShipName", "Customer.CompanyName", ... "EmployeeId", "CustomerId"]
        show_columns = ["ShipName", "Customer.CompanyName", "OrderDate", ... "ShipCountry", "Id", "EmployeeId", "CustomerId"]
        edit_columns = ["ShipName", "OrderDate",... "ShipCountry", "Id", "EmployeeId", "CustomerId"]
        add_columns = ["ShipName", "OrderDate", ... "ShipCountry", "Id", "EmployeeId", "CustomerId"]
        related_views = [OrderDetailModelView]

        appbuilder.add_view(OrderModelView, "Order List", icon="fa-folder-open-o", category="Menu")

Instead, fab-quickstart generates this file with such segments for each page,
resulting in apps like shown below:

#. **Multi-page:** apps incude 1 page per table

#. **Multi-table:** pages include `related_views` for each related child table, and join in parent data

#. **Favorite field first:** first-displayed field is "name", or _contains_ "name" (configurable)

#. **Predictive joins:** favorite field of each parent is shown (product _name_ - not product _id_)

#. **Ids last:** such boring fields are not shown on lists, and at the end on other pages


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://drive.google.com/uc?export=view&id=1Q3cG-4rQ6Q6RdZppvkrQzCDhDYHnk-F6



Depends on:
-----------
- Flask-AppBuilder
