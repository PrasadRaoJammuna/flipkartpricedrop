# flipkartpricedrop


 ## It is Amazing website Its working fine , can you make it pretty for me.pullrequest
 
 ## we can do pretty damn functionalities in future,Lets make it now.

Steps:

1)- Install Virtualenv

--> pip install virtualenv

2)- Create Virtualenv

--> virtualenv venv

3)- Activate virtual env

--> source venv/bin/activate

4)- Instal Git

--> pip install git

5)- Clone the code from the repo:

--> git clone https://github.com/PrasadRaoJammuna/flipkartpricedrop.git

6)- Install requirements

--> cd  pricedrop
--> pip install -r requirements

Note: Above lines are required for first time installation

7)- Execute below commands

--> python manage.py makemigrations
--> python manage.py migrate
Note: Above commands should be executed if there is any db level changes

8)- Create superuser for admin access and follow instruction, if not created one

--> python manage.py createsuperuser

9)- Runserver and open your browser: 

--> python manage.py runserver
For webapp: localhost:8000

For admin access: localhost:8000/admin

