Basic Packaging
===============

As mentioned we want to create a package out of this file:

.. code-block:: python
   :caption: number_magic.py

   def addition(arg1, arg2):
       """
       This functions adds the first and the second argument.

       :param arg1: the first summand
       :type arg1:  float
       :param arg2: the second and last summand
       :type arg2:  float
       :return:     the sum of both summands
       :rtype:      float
       """
       return arg1 + arg2

Make it a package
-----------------

Right now it is just a plain python file. To make it a package you need to
folder and add a ``__init.py`` file, that can be empty.
Now we created a python package that can be imported.

Try it. Open a terminal and do

.. code-block:: none

   cd /path/containing/folder
   python

We will assume you called the folder above ``plain_magic``. So try to import
the package.

.. code-block:: python

   import plain_magic

If that does not throw any import error we have a python package now.

The directory should look like this now:

.. code-block:: none

   some_directory/
      plain_magic/
         __init__.py
         number_magic.py


Enable Installations
--------------------

Check Package Import
____________________

Now we solve the problem that you cannot import your package everywhere. Try it
by doing:

.. code-block:: none

   # now switch directories
   cd /tmp
   python

So try to import
the package.

.. code-block:: python

   import plain_magic

It should complain and throw an ``ModuleNotFoundError``.

So lets solve the problem

Create a setup.py
_________________

Now create a ``setup.py`` according to the instructions of the
`Kiwi template documentation <https://kiwi-python-package-template.readthedocs.io/en/latest/content/packaging_features.html>`_.


How can you check if you succeded?
__________________________________

Try to install it and import the package from somewhere else.

So open a terminal

.. code-block:: none

   cd /parent/directory/of/plain_magic
   pip install -e .


Now you go back to `Check Package Import`_ and try to import it from
another directory.


The directory should look like this now:

   some_directory/
      plain_magic/
         __init__.py
         number_magic.py
      setup.py

Write a Command Line Interface
------------------------------

Now we want to be able to use our package from the command line:

.. code-block:: none

   some-magic-cmd adding-two-numbers --first-summand 1 --second-summand 2

Therefore you need to create command line interace similar to the one in the
template `here <https://kiwi-python-package-template.readthedocs.io/en/latest/content/packaging_features.html#command-line-interface>`_.
In particular you need to create a ``cli.py``.

To check if you succeeded you need to

- reinstall your package
- call the command from the command line

For solutions take a look `the template package <https://git.tu-berlin.de/bvt-htbd/kiwi/cookiecutter-python-package-template/-/tree/master/%7B%7Bcookiecutter.package_name%7D%7D>`_

The directory should look like this now:

   some_directory/
      plain_magic/
         __init__.py
         cli.py
         number_magic.py
      setup.py
