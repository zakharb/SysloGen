from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='syslogen',
    version='1.2',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=required,
)
