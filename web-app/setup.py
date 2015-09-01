from distutils.core import setup



setup(

    # Application name:

    name="MyFirstWebApp",

    # Version number (initial):

    version="0.1",

    # Application author details:

    author="Mohammad Syed",
    author_email="Mohammed_Syed01@infosys.com",

    # Packages
    
    packages=["."],



    # Include additional files into the package

    include_package_data=True,



    # Details

    url="https://github.com/testwlmorg/testdock/MyFirstWebApp_0.1",


    # license="LICENSE.txt",

    description="There is nothing much in this except a simple home page.",


    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)

    install_requires=[

        "flask",

    ],

)
