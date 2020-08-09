Flask App Builder - Quick Start
===============================

Create `Flask App Builder <www.github.com/dpgaspar/Flask-AppBuilder>`_ `view` file,
directly from model, for an instant multi-page, multi-table app.

Use this `Quick Start <www.github.com/valhuber/fab-quickstart/wiki>`_ to create the app shown below in 10 minutes.


Change Log
----------

Initial Version

Usage:
------
Presuming you have a project and model.py file as shown in quick start,
generate the view.py file like this::

    pip install -i https://test.pypi.org/simple/ FAB-Quickstart==0.9.0
    fabqs


Features:
---------

Generated fab pages look like as shown below:

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
