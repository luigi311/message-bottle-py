# message-bottle-py

The message bottle project is for educational purposes to familiarize the contributors with github collaboration and working with django

Message bottle is a django application that will act as a message board allowing users to interact with eachother. The message board will give the users the ability to create a thread about a specific topic that they will to talk about with other users and allow others to create responses to said thread. The application will also allow the users to interact with eachother in real time via a live chat that is handled by a plugin called FireChat. 

# Configuration
1. Create Virtual Enviornment 
```
makevirtualenv message-bottle
```
2. Activate Virtual Enviornment
```
workon message-botte
```
3. Clone the repository to your computer
```
git clone https://github.com/rmedinahu/message-bottle-py.git
```
4. Install the required python packages inside the virtual enviornment
```
pip install -r requirements/requirements.txt
```
5. Create sql database
```
python manage.py migrate
```
6. Create Superuser so you can mess around with the admin page
```
python manage.py createsuperuser
```
7. Run the server to make sure everything works
```
python manage.py runserver
```
If you want to access the server from a device other than your computer such as a mobile device
```
python manage.py runserver 0.0.0.0:8000
```
To access the server on another device you need to know the ip address of your computer that is running the server, you can get it by running 
```
ip addr show
```
