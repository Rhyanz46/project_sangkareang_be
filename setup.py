from setuptools import find_packages, setup

setup(
    name='apps',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_cors',
        'flask_sqlalchemy'
    ],
)

# pip install -e .
