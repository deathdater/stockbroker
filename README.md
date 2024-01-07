## STOCKBROKER - Inspiration to learn trading programitically.
### A Django application For Market Data Collection, Analysis, Strategy also Trading in Indian Markets.

## Running Locally

### 1. Install virtualenv
- `pip3 install virtualenv`   
### 2. Create a virtual Env using below command //helps keep the python dependencies intact:
- `mkdir ~/.stockenv`
- `virtualenv -p python3 ~/.stockbroker/stockenv`

### 3. cd into virtualenv directory & activate the virtualenv using below command 
- `source ~/.stockbroker/stockenv/bin/activate`

### 4. pip install following perquisites:
- `pip3 install requirments.txt`

### 5. Enter the below command to intialise your db. // make sure you  have cd into git repo
- `python manage.py makemigrations`
- `python manage.py migrate`
	
### 7. now run the server using below command
- `python manage.py runserver`

### 8. visit `http://127.0.0.1:8000`

VOILA you are On !!


# How does this work

Kautilya uses NSE BHAVCOPY for static Data Analysis.


Step 1 : Create a Django superuser/admin account.
Step 2 : Start the APP to get yourself.
Step 3 : Add the PR folder till date this will create the folders with respective URLS.
Step 4 : Download the PR Zip file for the folders Data Generated.
Step 5 : GOTO Stockmaster App to load the last ten ,you can clear the data beore loading new Data add a dummy record to perform the admin function.
Step 6 : GOTO stockanalysis App to Load all the stocks for Buy signal validations.
Step 7 : GOTO PR master table to update filter stock


Data Prep Work:
Creation of PR Folder Links
Downloading PR folders from Official NSE Website and extracting Bhav copy Data
Now most of the swing based approach to take Buy signals are based on 10 Days Data.

In this App we have two approaches implemented for analysis of 2 Days Data  and store the signal info.
1. PD Data loaded
2. Investpy realtime validation.


Qualittative Analysis for Investment is based on a degreet of research on the filtered stocks.
This is seek the user to input the details of the filtered stock from the PR Master to be loaded and then confirmed over quality parameters.

Output Actions:

1. Get Trendy Stocks: This provides the prints list of Stocks in the terminal with BUY signal for swing trade based on chart data.