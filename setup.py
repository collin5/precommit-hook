#@Author: Collins Abitekaniza
#@Email: abtcolns@gmail.com


from distutils import setup
from app.scripts import *

setup(

        #Application name
        name = "precommit-hook",
        
        version = "0.1",
        author = "Collins Abitekaniza",
        author_email = "abtcolns@gmail.com",
        packages = ['app'],
        include_package_data = True,
        license = 'MIT',
        url = "https://github.com/collin5/precommit-hook",
        description = "Enforce code quality in python projects",
        install_requires = ["flake8"],
        cmdclass = {
            "install":Post_install
        }
    )
