import io
import os
import re
import setuptools


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(
            text_type(r':[a-z]+:`~?(.*?)`'),
            text_type(r'``\1``'),
            fd.read()
        )


setuptools.setup(
    name="git_workshop_py_packaging",
    version="0.0.1",
    url="https://github.com/spirousschuh/git-workshop-py-packaging",
    license='MIT',

    author="Christoph Lange",
    author_email="christoph.lange@tu-berlin.de",

    description="Some tasks to practise python packaging",
    long_description=read("README.rst"),
    long_description_content_type='test/x-rst',
    packages=setuptools.find_packages(exclude=('tests')),
    install_requires=['click', 'tox'],
    entry_points={
        'console_scripts': [
            'do-nothing=git_workshop_py_packaging.cli:cli_group'
        ],
    },
)
