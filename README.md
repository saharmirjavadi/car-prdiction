# Project Setup

*car-prdiction*
Forecasting car price according to its model and year of production based on fetching other cars information and performing machine learning operations on them



## Step 1 – Installing the Components from the Ubuntu Repositories

First you will install the essential components. This includes pip, the Python package manager for installing and managing Python components, and also the database software with its associated libraries.

You will be using Python 3, which ships with Ubuntu 20.04. Start the installation by typing:

    ➜ ~ sudo apt update
    ➜ ~ sudo apt install python3-venv python3-pip python3-dev 

With the installation out of the way, you can move on to the database.

## Step 2 – Creating a Database and Database User
....

## Step 3 - Install project requirements and running project

The virtualenv package allows you to create these environments easily.

Clone and move into project directory :

    ➜ ~ git clone https://github.com/saharmirjavadi/car-prdiction.git
    ➜ ~ cd car-prdiction

You can create a virtual environment to store the project’s Python requirements by typing:

    ➜ car-prdiction python3 -m venv venv

This will install a local copy of Python and a local pip command into a directory called myprojectenv within your project directory.

Before you install applications within the virtual environment, you need to activate it. You can do so by typing:

    ➜ car-prdiction source venv/bin/activate

Your prompt will change to indicate that you are now operating within the virtual environment. It will look something like this 

    (venv) ➜ car-prdiction


Note: Regardless of which version of Python you are using, when the virtual environment is activated, you should use the pip command (not pip3).

    (venv) ➜ car-prdiction pip install -r requirements.txt


Configure environment variables:

    (venv) ➜ car-prdiction cp .env-sample car-prdiction/.env


When you are done, you're ready test the project.


to run the project:
    (venv) ➜ car-prdiction python3 ./fetch_data.py