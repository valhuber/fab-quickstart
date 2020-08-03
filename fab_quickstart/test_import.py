import importlib
import sys
import slugify

# https://programtalk.com/python-examples/importlib.util.spec_from_file_location/

def _import_system_file(filename):
    module_name = slugify(filename[:-3], '.')
    spec = importlib.util.spec_from_file_location(module_name, filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


# ex 3
def import_python_modules_by_path(path):
    for filename in list_files(path, "py"):
        name = extract_filename(filename)
        spec = importlib.util.spec_from_file_location(name, os.path.join(path, filename))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

# ex 5
def load_numpy_tests():
    # load numpy arraysetops testing module from the installed numpy distro
    numpy_path = os.path.split(numpy.__file__)[0]
    module_source = os.path.join(numpy_path, 'lib', 'tests', 'test_arraysetops.py')
    module_name = 'numpy_indexed.tests.numpy_tests'
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(module_name, module_source)
        numpy_tests = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(numpy_tests)
    except:
        import imp
        numpy_tests = imp.load_source(module_name, module_source)
    return numpy_tests

# https://stackoverflow.com/questions/8790003/dynamically-import-a-method-in-a-file-from-a-string
def load_class(full_class_string):
    """
    dynamically load a class from a string
    """

    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]

    module = importlib.import_module(module_path, "views")  # Exception has occurred: ValueError Empty module name
    # Finally, we retrieve the Class
    return getattr(module, class_str)

test = load_class("Users/val/python/vscode/fab-quickstart/nw/app/models")


load_numpy_test("Users/val/python/vscode/fab-quickstart/nw/app")

import_python_modules_by_path("Users/val/python/vscode/fab-quickstart/nw/app")

_import_system_file("Users/val/python/vscode/fab-quickstart/nw/app")
_import_system_file("Users/val/python/vscode/fab-quickstart/nw/app/models.py")