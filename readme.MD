## 1. Before you start... 

You should have:
- Python 3.8.x installed on your computer 
- Visual Studio Code (or another IDE of your choosing) installed on your computer 
- A GitHub account
- requierments.txt contains all packages you need (except virtualenv)-> `pip install -r requirements.txt`

## 2. Setup virtual enviorment and flask

## Initial setup
- Check to see if your Python installation has pip:

    `pip -h`

- Install the virtualenv package:

    `pip install virtualenv`

- To create a virtual environment, you must specify a path. For example to create one in the local directory called ‘mypython’:

    `virtualenv mypython`


## IMPORTANT! Every time you restart your computer or reopen VSCode, you'll have to do a few things. 
These instructions are for a Bash shell on windows. For other shells can be found online. 

- Activate your virtual environment for this project: 
   
    `source venv/Scripts/activate`

- Point Flask to your application: 

    `export FLASK_APP=main.py`
    
- Enable hot reloading, debug mode, and other useful features for local development:  

    `export FLASK_ENV=development`
     
- run your flask application: 

    `flask run`

## 3. While You're Developing... 

Whenever you deploy your code, it will be automatically testing and linted by the GitHub Action. To have a quicker feedback loop and to make sure there are as few surprises as possible, run the same commands locally, too:

To test your app: 

> pytest --doctest-modules

To Lint your app: 
> flake8 --exclude venv 

#### Environment Variables 
This setup is designed to allow you to use environment variables if you need them. There are many ways to set this up with Python, and for this repository, I chose a method which allows for relatively simple integration with our GitHub Actions and Google App Engine workflow, but it does not scale very well. A more scalable system using the library `python-dotenv`. If you start working with many secrets, for example, many API keys, it makes sense to switch to that instead. The current system as implemented in this repository is described below.  

Environment Variables can be found in the file `config.py`, as can more explanation. In order to use an environment variable - a value which you expect to be different in local development from our production system - it should be added to that file. In the cases of the Python variable `DATABASE_PASSWORD`, Python will look for an environment variable (on the computer running your website) called `DB_PASSWORD`, and assign its value to the Python variable. This is then usable by the Flask app. It is essential that anything which should remain a secret, like a database password, is never added to your GitHub repository. This makes your password public - giving anyone access to your database. Instead, we can use GitHub Secrets to securely add a password to the production environment. In other words: we can create a database password, add it to GitHub Secrets, and then GitHub can pass it on to App Engine. The last step requires one more trick, though. The App Engine environment is configured by the file `app.yaml`, which does not support reading in environment variables dynamically. Instead, the GitHub Action has a step in it called `Prepare Deployment`, which can add a GitHub Secret to the `app.yaml` file. In this case, the code expects GitHub to have a variable called `PRODUCTION_DATABASE_PASSWORD`. A line of code in `.github/workflows/main.yaml` then adds this password to the file `app.yaml` dynamically, setting to have the name `DB_PASSWORD`. This, in turn, is read in by the flask app. Note that the environment variables can all have the same name, but I have made them different to make it clearer what is what. 