"""

Fab QuickStart 0.1 running

Current Working Directory: /Users/val/python/vscode/fab-quickstart/nw

From: /Users/val/python/vscode/fab-quickstart/fab_quickstart/cli.py

Using Python: 3.8.3 (default, Jul 15 2020, 16:38:07) 
[Clang 11.0.3 (clang-1103.0.32.62)]

 Generated at: 2020-08-04 09:03:45.653400

"""
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder, db
from .models import *




class CategoryModelView(ModelView):
   datamodel = SQLAInterface(Category)
   list_columns = ["Id", "CategoryName", "Description"]
   show_columns = ["Id", "CategoryName", "Description"]
   edit_columns = ["Id", "CategoryName", "Description"]
   add_columns = ["Id", "CategoryName", "Description"]
   related_views = []

appbuilder.add_view(
      CategoryModelView, "Category List", icon="fa-folder-open-o", category="Menu")





class CustomerCustomerDemoModelView(ModelView):
   datamodel = SQLAInterface(CustomerCustomerDemo)
   list_columns = ["Id", "Customer.Id"]
   show_columns = ["Id", "Customer.Id", "CustomerTypeId"]
   edit_columns = ["Id", "CustomerTypeId"]
   add_columns = ["Id", "CustomerTypeId"]
   related_views = []

appbuilder.add_view(
      CustomerCustomerDemoModelView, "CustomerCustomerDemo List", icon="fa-folder-open-o", category="Menu")





class OrderDetailModelView(ModelView):
   datamodel = SQLAInterface(OrderDetail)
   list_columns = ["Id", "Product.Id", "Order.Id", "UnitPrice", "Quantity"]
   show_columns = ["Id", "Product.Id", "Order.Id", "UnitPrice", "Quantity", "Discount", "ProductId", "OrderId"]
   edit_columns = ["Id", "UnitPrice", "Quantity", "Discount", "ProductId", "OrderId"]
   add_columns = ["Id", "UnitPrice", "Quantity", "Discount", "ProductId", "OrderId"]
   related_views = []

appbuilder.add_view(
      OrderDetailModelView, "OrderDetail List", icon="fa-folder-open-o", category="Menu")





class OrderModelView(ModelView):
   datamodel = SQLAInterface(Order)
   list_columns = ["Id", "Customer.Id", "OrderDate", "RequiredDate", "ShippedDate"]
   show_columns = ["Id", "Customer.Id", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipName", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "EmployeeId", "CustomerId"]
   edit_columns = ["Id", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipName", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "EmployeeId", "CustomerId"]
   add_columns = ["Id", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipName", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "EmployeeId", "CustomerId"]
   related_views = [OrderDetailModelView]

appbuilder.add_view(
      OrderModelView, "Order List", icon="fa-folder-open-o", category="Menu")





class CustomerModelView(ModelView):
   datamodel = SQLAInterface(Customer)
   list_columns = ["Id", "CompanyName", "ContactName", "ContactTitle", "Address"]
   show_columns = ["Id", "CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax"]
   edit_columns = ["Id", "CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax"]
   add_columns = ["Id", "CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax"]
   related_views = [CustomerCustomerDemoModelView, OrderModelView]

appbuilder.add_view(
      CustomerModelView, "Customer List", icon="fa-folder-open-o", category="Menu")


# table already generated per recursion: CustomerCustomerDemo


class CustomerDemographicModelView(ModelView):
   datamodel = SQLAInterface(CustomerDemographic)
   list_columns = ["Id", "CustomerDesc"]
   show_columns = ["Id", "CustomerDesc"]
   edit_columns = ["Id", "CustomerDesc"]
   add_columns = ["Id", "CustomerDesc"]
   related_views = []

appbuilder.add_view(
      CustomerDemographicModelView, "CustomerDemographic List", icon="fa-folder-open-o", category="Menu")





class EmployeeTerritoryModelView(ModelView):
   datamodel = SQLAInterface(EmployeeTerritory)
   list_columns = ["Id", "Employee.Id", "Territory.Id"]
   show_columns = ["Id", "Employee.Id", "Territory.Id", "EmployeeId", "TerritoryId"]
   edit_columns = ["Id", "EmployeeId", "TerritoryId"]
   add_columns = ["Id", "EmployeeId", "TerritoryId"]
   related_views = []

appbuilder.add_view(
      EmployeeTerritoryModelView, "EmployeeTerritory List", icon="fa-folder-open-o", category="Menu")





class EmployeeModelView(ModelView):
   datamodel = SQLAInterface(Employee)
   list_columns = ["Id", "LastName", "FirstName", "Title", "TitleOfCourtesy"]
   show_columns = ["Id", "LastName", "FirstName", "Title", "TitleOfCourtesy", "BirthDate", "HireDate", "Address", "City", "Region", "PostalCode", "Country", "HomePhone", "Extension", "Photo", "Notes", "ReportsTo", "PhotoPath"]
   edit_columns = ["Id", "LastName", "FirstName", "Title", "TitleOfCourtesy", "BirthDate", "HireDate", "Address", "City", "Region", "PostalCode", "Country", "HomePhone", "Extension", "Photo", "Notes", "ReportsTo", "PhotoPath"]
   add_columns = ["Id", "LastName", "FirstName", "Title", "TitleOfCourtesy", "BirthDate", "HireDate", "Address", "City", "Region", "PostalCode", "Country", "HomePhone", "Extension", "Photo", "Notes", "ReportsTo", "PhotoPath"]
   related_views = [EmployeeTerritoryModelView]

appbuilder.add_view(
      EmployeeModelView, "Employee List", icon="fa-folder-open-o", category="Menu")


# table already generated per recursion: EmployeeTerritory# table already generated per recursion: Order# table already generated per recursion: OrderDetail# table already generated per recursion: OrderDetail


class ProductModelView(ModelView):
   datamodel = SQLAInterface(Product)
   list_columns = ["Id", "ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock"]
   show_columns = ["Id", "ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "SupplierId", "CategoryId"]
   edit_columns = ["Id", "ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "SupplierId", "CategoryId"]
   add_columns = ["Id", "ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "SupplierId", "CategoryId"]
   related_views = [OrderDetailModelView]

appbuilder.add_view(
      ProductModelView, "Product List", icon="fa-folder-open-o", category="Menu")





class RegionModelView(ModelView):
   datamodel = SQLAInterface(Region)
   list_columns = ["Id", "RegionDescription"]
   show_columns = ["Id", "RegionDescription"]
   edit_columns = ["Id", "RegionDescription"]
   add_columns = ["Id", "RegionDescription"]
   related_views = []

appbuilder.add_view(
      RegionModelView, "Region List", icon="fa-folder-open-o", category="Menu")





class ShipperModelView(ModelView):
   datamodel = SQLAInterface(Shipper)
   list_columns = ["Id", "CompanyName", "Phone"]
   show_columns = ["Id", "CompanyName", "Phone"]
   edit_columns = ["Id", "CompanyName", "Phone"]
   add_columns = ["Id", "CompanyName", "Phone"]
   related_views = []

appbuilder.add_view(
      ShipperModelView, "Shipper List", icon="fa-folder-open-o", category="Menu")





class SupplierModelView(ModelView):
   datamodel = SQLAInterface(Supplier)
   list_columns = ["Id", "CompanyName", "ContactName", "ContactTitle", "Address"]
   show_columns = ["Id", "CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "HomePage"]
   edit_columns = ["Id", "CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "HomePage"]
   add_columns = ["Id", "CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "HomePage"]
   related_views = []

appbuilder.add_view(
      SupplierModelView, "Supplier List", icon="fa-folder-open-o", category="Menu")


# table already generated per recursion: EmployeeTerritory


class TerritoryModelView(ModelView):
   datamodel = SQLAInterface(Territory)
   list_columns = ["Id", "TerritoryDescription"]
   show_columns = ["Id", "TerritoryDescription", "RegionId"]
   edit_columns = ["Id", "TerritoryDescription", "RegionId"]
   add_columns = ["Id", "TerritoryDescription", "RegionId"]
   related_views = [EmployeeTerritoryModelView]

appbuilder.add_view(
      TerritoryModelView, "Territory List", icon="fa-folder-open-o", category="Menu")


# skip admin table: ab_permission
# skip admin table: ab_permission_view
# skip admin table: ab_view_menu
# skip admin table: ab_permission_view_role
# skip admin table: ab_role
# skip admin table: ab_register_user
# skip admin table: ab_user
# skip admin table: ab_user_role
#  21 table(s) in model; generated 13 page(s), including 5 related_view(s).

