from setuptools import setup, find_packages

setup(
    name='my_package_1',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        "requests",
        "scikit-learn",
    ],
    author='Amit Ravi',
    author_email='amit.ravi@uk.qbe.com',
    description='A test of external package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hiamitravi/pypi',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)