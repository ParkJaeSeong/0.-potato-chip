# pip install setuptools

from setuptools import setup, find_packages


setup(
    name='python_programming_demo_app',
    version='0.0.2',
    packages=find_packages(),
    package_data={ 'roboter': ['templates/*.txt'] },
    url='http://sakaijunsoccer.appspot.com',
    license='MIT',
    author='jsakai',
    author_email='example@example.com',
    install_requires=['termcolor==1.1.0'],
    long_description=open('README.txt').read(),
    test_suits='tests',
    #tests_require=['pytest'],
)
