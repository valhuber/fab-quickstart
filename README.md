# FAB Quick Start - build views.py
__fab_quickstart__ generates Flask Application Builder `views.py` files, to create instant multi-page, multi-table apps.

## Features
Generated fab pages look as shown below:
1. __Multi-page:__ apps incude 1 page per table
1. __Multi-table:__ pages include `related_views` for each related child table, and join in parent data
1. __Favorite field first:__ first-displayed field is "name", or _contains_ "name" (configurable)
1. __Predictive joins:__ favorite field of each parent is shown (product _name_ - not product _id_)
1. __Ids last:__ such boring fields are not shown on lists, and at the end on other pages

![generated page](https://drive.google.com/uc?export=view&id=1Q3cG-4rQ6Q6RdZppvkrQzCDhDYHnk-F6)


## Background
[Flask Application Builder (FAB)](https://github.com/dpgaspar/Flask-AppBuilder) provides a rapid means for building web pages for database apps, based on Python and Flask.  Here is a [Quick Start for using FAB](https://github.com/valhuber/fab-quickstart/wiki).

Key FAB inputs are:

1. `models.py` file - describes your database tables.  You can build models with tools like [sqlacodegen](https://www.google.com/url?q=https%3A%2F%2Fpypi.org%2Fproject%2Fsqlacodegen%2F&sa=D&sntz=1&usg=AFQjCNHZ3ERjfnSO8MA8V20gzLjfeBaIxw).  The file contains segments like this for each table:
```
class OrderDetail(BaseMixin, Model):
    __tablename__ = 'OrderDetail'

    Id = Column(String(8000), primary_key=True)
    OrderId = Column(Integer, ForeignKey("Order.Id"), nullable=False)
    Order = relationship("Order")
    ProductId = Column(Integer, ForeignKey("Product.Id"), nullable=False)
    Product = relationship("Product")
    UnitPrice = Column(DECIMAL, nullable=False)
    Quantity = Column(Integer, nullable=False)
    Discount = Column(Float, nullable=False)
```

Note the ```ForeignKey / relationship``` code.  To get multi-table forms, either
add such code to the ```models.py``` file, or (better) add foreign keys to your database.

The ```Northwind_small.sqlite``` sample database contains no foreign keys.
The ```ForeignKey / relationship``` code was hand-added,
not generated by ```sqlacodegen```.

2. `views.py` file - used by fab to generate pages.  It consists of segments like this for each page:
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

## Usage
Follow the steps below to install, generate an app, and run it.

### Install fab_quickstart
```
cd <project>  # fab directory containing `config.py` file
pip install -i https://test.pypi.org/simple/ FAB-Quickstart==0.9.0
```

### Generate views.py
```
fab-qs
# copy generated output over your views.py file
```

### Run generated app
Run fab to run the app:
```
cd project
export FLASK_APP=app
flask run
```



***
## Explore fab_quickstart
Use this to [explore the FAB Quick Start Utility](https://github.com/valhuber/fab-quickstart/wiki/Explore-fab_quickstart).
