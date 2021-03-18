Conventions
===========


Use Flake8
----------

Now we try to check if our code matches the PEP 8 coding conventions.

Consequently we install the checking tool ``flake8`` and check it.

.. code-block:: none

   pip install flake8
   cd some_directory
   flake8
   # take a look at the output


In case flake8 does not complain, just do nothing. In case it does
follow the `liniting instructions <https://git.tu-berlin.de/bvt-htbd/kiwi/cookiecutter-python-package-template/-/blob/master/%7B%7Bcookiecutter.package_name%7D%7D/tox.ini>`_
make your code more conventional.

If you want to automate a ``flake8`` check you can modify your ``tox.ini``
file according to the
`template tox.ini <https://git.tu-berlin.de/bvt-htbd/kiwi/cookiecutter-python-package-template/-/blob/master/%7B%7Bcookiecutter.package_name%7D%7D/tox.ini>`_.



Add .gitignore
--------------


Last but not least, let us add a ``.gitignore`` file to the directory root.
For an example take at that `simple example <https://kiwi-python-package-template.readthedocs.io/en/latest/content/conventions.html#gitignore>`_.

