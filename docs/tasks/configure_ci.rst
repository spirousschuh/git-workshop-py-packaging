Configure Continuous Integration
================================

Now we want to get deeper into the
`Continuous Intergration Setup <https://kiwi-python-package-template.readthedocs.io/en/latest/content/ci_setup.html>`_.


At first we want to create a small dummy test. We can just take
`this one <https://git.tu-berlin.de/bvt-htbd/kiwi/cookiecutter-python-package-template/-/blob/master/%7B%7Bcookiecutter.package_name%7D%7D/tests/test_numbers_magic.py>`_
from the template package.

Creating tests
______________

Please create the python package ``tests`` next to the ``plain_magic``
directory. The folder structure should look like this now.


.. code-block:: none

   some_directory/
      plain_magic/
         __init__.py
         cli.py
         number_magic.py
      tests/
         __init__.py
         test_number_magic.py
      setup.py


Install ``pytest`` via ``pip`` and try to execute the tests in the
home directory

.. code-block:: none

   pip install pytest

   cd some_directory
   pytest



Configure Tox
_____________


Now we are trying to automate the whole installation and testing proceduce
via `tox <https://kiwi-python-package-template.readthedocs.io/en/latest/content/ci_setup.html#tox>`_.
Therefore we need to put another configuration file in the main folder.

To check if you succeeded please install ``tox`` and execute it.

.. code-block:: none

   pip install tox

   cd some_directory
   tox

If all tests run through, you made it.


The folder structure shall look like this now:

.. code-block:: none

   some_directory/
      plain_magic/
         __init__.py
         cli.py
         number_magic.py
      tests/
         __init__.py
         test_number_magic.py
      setup.py
      tox.ini


Configure Gitlab to run the Tests
_________________________________

Now we want the current local repository to be on the Gitlab server. Therefore
please follow
`these instructions <https://kiwi-python-package-template.readthedocs.io/en/latest/content/create_repo.html>`_,
but keep in mind to skip the *Use Project Template*. We already created our
own little repository.


Now we want to tell Gitlab to run the tests for us, every time we push.
Therefore we need to add a file named ``.gitlab-ci.yml``
according to the
`instructions from the template documentation <https://kiwi-python-package-template.readthedocs.io/en/latest/content/ci_setup.html#gitlab-ci-yml>`_.