# MUSF

## Introduction
Our project is titled MUSF and it is a music recommendations website. The purpose of this software is to allow users to find new music based on their taste by providing related songs curated by a specific genre or keyword. It is meant to help users expand their music libraries by finding new genres, songs, or artists similar to the ones they listen to.

## Technologies Used
This application was made using Python, Flask, HTML, CSS, JavaScript, and SQL. The IDEs used for this project are Visual Studio, MySQL Workbench, and GitHub. 

## How to run this project:
Make you have install the following modules: pymysql, flask, flask-sqlalchemy, cryptography, and flask-login

if you do not have these modules use the commands below to install:

-- pip install flask

-- pip install flask-sqlalchemy

-- pip install cryptography

-- pip install flask-login

-- pip install pymysql

### Specifications
Users must create a new MySQL connection if they do not have one already. After creating it make sure that the MySQL server is activated. This can be seen by going into the Administration window and choosing ‘Server Status’. If the server is not running, run the MySQL server. Once the server is running, test the connection and then begin setting up the user access. To do so, access the Administration window, go to ‘Users and Privileges’ and in the ‘User Accounts’ section select User ‘root’ from host ‘localhost’. Here make sure that the Login Name is ‘root’, Limit to Hosts Matching is ‘localhost’, and the password is ‘password1234’. This is crucial for the application to be able to access the server dataset. After setting this up, one can begin to run the application.

To run this application download the GitHub Repository and open MySQL Workbench and run the MusicDB.sql file. This should generate a new schema in MySQL Workbench called MusicDB. Additionally, 52 entries will be inserted into the Songs table. Now, users can begin to run the application by opening the main.py file and running it on Visual Studio Code. If the terminal is causing some issues, try debugging the main.py file. Additional assitance is to select the Visual Studio Python environment to be an anaconda gloabl environment.

Open the http location stated in the terminal. The navigational instrucitons are located in the About Page.

If accessing the profile edit page gives users an error, simply refresh the page and it should work accordingly.
