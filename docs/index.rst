
Git Workshop Part 4: Python Packaging
=====================================


Purpose
_______

In this documentation we just have some tasks that will help you understand
the features of the
`Kiwi Template for Python Packages <https://git.tu-berlin.de/bvt-htbd/kiwi/cookiecutter-python-package-template>`_.
For a description of the content that enables you to solve the tasks,
please take a look at the
`template's documentation <https://kiwi-python-package-template.readthedocs.io/en/latest/?badge=latest>`_.

Tasks
________

The idea of the tasks is that you create a python package arround this file:

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



Tasks 1: Basic Package
----------------------


.. toctree::
    :maxdepth: 2

    tasks/basic_packaging


Tasks 2: Configure Continuous Integration
-----------------------------------------


.. toctree::
    :maxdepth: 2

    tasks/configure_ci


Contribute
----------

- Issue Tracker: https://github.com/spirousschuh/git-workshop-py-packaging/-/issues
- Source Code: https://github.com/spirousschuh/git-workshop-py-packaging

Support
-------

If you encounter issues, please let us know.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
