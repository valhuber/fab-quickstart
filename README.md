# FAB Quick Start - build views.py
__fab_quickstart__ is a command line utility to generate Flask Application Builder `views.py` files, to create instant multi-page, multi-table apps.

## Features
Generated fab pages look as shown below:
1. __Multi-page:__ apps incude 1 page per table
1. __Multi-table:__ pages include `related_views` for each related child table, and join in parent data
1. __Favorite field first:__ first-displayed field is "name", or _contains_ "name" (configurable)
1. __Predictive joins:__ favorite field of each parent is shown (product _name_ - not product _id_)
1. __Ids last:__ such boring fields are not shown on lists, and at the end on other pages

![generated page](https://drive.google.com/uc?export=view&id=1Q3cG-4rQ6Q6RdZppvkrQzCDhDYHnk-F6)


## Background
[Flask Application Builder (FAB)](https://github.com/dpgaspar/Flask-AppBuilder) provides a rapid means for building web pages for database apps, based on Python, Flask and sqlalchemy.  Here is a [Quick Start for using FAB](https://github.com/valhuber/fab-quickstart/wiki).

Recall that creating the `views.py` file can be [tedious](https://github.com/valhuber/fab-quickstart/wiki#key-fab-inputs-modelspy-and-viewspy).  This utility generates the `views.py` file from the `models.py` file, to save time and reduce learning curve.


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
