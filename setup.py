from setuptools import setup, find_packages

setup(
    name='my_external_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "requests==2.32.3",
        "scikit-learn==1.6.0",
        "SQLAlchemy==2.0.36",
        "sqlalchemy-bigquery==1.12.0",
        "xmltodict==0.14.2",
        "pyparsing==3.2.1",
        "tqdm==4.67.1"
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