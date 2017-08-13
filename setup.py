from setuptools import find_packages, setup

setup(
    name='xdao'
    , version='0.1'
    , author='sebastian'
    , author_email='oxsoftdev@gmail.com'
    , packages=find_packages()
    , url='https://github.com/oxsoftdev/xdao'
    , license='LICENSE.txt'
    , install_requires=[
        'pyodbc'
    ]
)

