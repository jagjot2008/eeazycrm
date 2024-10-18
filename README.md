# EeazyCRM

#### Python based open source CRM developed using Flask framework

##### It's still WORK IN PROGRESS (I'm still building the modules)
##### But I have a small DEMO image below
![alt text](https://i.ibb.co/BsWm9Kf/eeazycrm-demo1.gif)

Features List
============

EeazyCRM contains the following modules (along with the 
completion progress report):

   1. Leads (99% complete)
   2. Accounts (90% complete)
   3. Contacts (99% complete)
   4. Deals (with Pipeline view) (90% complete)
   5. Activities (still building) (Not started as yet)
   6. Reports (with charts and graph) - (60% complete)
   7. Settings (50% complete)
       1. Roles Management (100% complete)
       2. User Management (100% complete)
       3. Profile Management (100% complete)
       4. Company Management (Not started)
       5. Configuration Management (Not started)
            1. Deal Stage
            2. Lead Stage
            3. Lead Source
            4. Activity Types
            5. Email Templates
       6. Application Settings (100% complete)
   8. Invoice (Not started)
   9. Dashboard (10% complete)
   
Depending upon the demand of this application, I'm also planning the
following:

   * Integration with WordPress Contact Form 7 (Lead Capture).
   * Integration with Google Contacts.
   * Integration with DropBox or Google Drive for Automatic Backups.
   * Integration with Email Service such as MailChimp.
   
Installation Requirements
============

1. Python3
2. Postgresql (ver 11+ or greater)
2. pip3
3. virtualenv

Make sure that the postgresql instance is up and running.

Open the command prompt or terminal and 
create a new database with the following commands.
    .. code-block:: python
    
        psql
        create database eeazy_crm

Installation Steps
============

Step 1: Create and Navigate to the Project Directory
bash
mkdir eeazycrm
cd eeazycrm

Step 2: Initialize Git Repository and Pull Project Code
bash
git init
git remote add origin https://github.com/jagjot2008/EeazyCRM.git
git pull origin master

Step 3: Create and Activate a Virtual Environment
bash
virtualenv -p python3 eeazycrm_env
source eeazycrm_env/bin/activate

Step 4: Install the Dependencies
bash
pip3 install -r requirements.txt

Step 5: Set Up PostgreSQL
Ensure PostgreSQL is running, then open the terminal and execute the following commands:

bash
psql
CREATE DATABASE eeazy_crm;

Step 6: Create the Configuration File from Example
bash
cp config_vars.example config_vars.py
Open the config_vars.py file and add the PostgreSQL database connection credentials. For example:

python
PRODUCTION_DATABASE_URI = 'postgresql://username:password@localhost/eeazy_crm'
You can also set up development and testing configurations if needed.

Step 7: Set Environment Variables
Configure the environment variables needed for the application:

bash
export EMAIL_USER=<your email username>
export EMAIL_PASS=<your email password>
export FLASK_ENV=development  # or 'testing'
If you are using Windows, use set instead of export:

bash
set EMAIL_USER=<your email username>
set EMAIL_PASS=<your email password>
set FLASK_ENV=development

Step 8: Run the Application for the First Time (Installation Wizard)
bash
python3 run.py
This will run the installation wizard. Follow the on-screen instructions.

Step 9: Restart the Application After Installation
Once the installation is complete, stop the application and restart it:

bash
python3 run.py
       
   This will run the installation wizard. Follow the instructions
   in the wizard and after finishing installation, stop the 
   application and start again by running the command in step #6.
   
That's it folks. Your CRM is running.

Report a Bug or Request a New Feature
================================

For reporting bugs in the system, you can raise a github issue or even request
a new feature.



