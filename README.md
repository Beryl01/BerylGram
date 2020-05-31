# Pics Art
#### By:
Beryl Negesa Otieno

<img src="./p.png">

### Description  
The app is a photo sharing app which allows users to share, like, comment, follow and have followers in sharing daily activities.

## User story
As a user of the web application you will be able to:
1. Sign up and log in
2. View photos posted by other users
3. Follow other users
4. Comment on photos
5. Edit your profile

### Deployed link


### BDD
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the app and gets redirected to the register page  | User register | Directed to the login page | 
If user has an account, they click on `login` | User logs in | User is redirected to the home page where can view their pictures or others photos |
|  Home page loads | Add comment  | Comment posted appears |
|  Homepage loads | Click `user name` | User's profile appears | 
| Homepage loads | Click `plus sign` icon | User's redirected to a modal where they can upload an image | 
| Profile page loads | Click `settings` icon | A modal appears where one can change their delete account or logout | 
| Homepage loads | User inputs in the search form and presses enter | Searched results show |
| A list of users displays | Click `follow` button to follow | Reloaded to the homepage

### Setup and Installation  
To get the project .......    
##### Cloning the repository:  
 ```bash 
git clone https://github.com/Beryl01/BerylGram.git
```
##### Navigate into the folder 
 ```bash 
cd BerylGram
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
pip install -r requirements.txt 
```  
##### Setup Database  
SetUp your database User,Password, Host then make migrations
 ```bash 
python manage.py makemigrations
 ``` 
 Now Migrate  
 ```bash 
python3.6 manage.py migrate 
```
##### Run the application  
 ```bash 
python3.6 manage.py runserver 
```  
##### Testing the application  
 ```bash 
python3.6 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
## Technologies Used
* Python3.6
* Django 3.0
* HTML5
* CSS3
* Bootstrap4
  
## Known Bugs
None known for now.

## Support and contact details
* Email-berylnegesa@gmail.com

## License
[MIT License](License.md)
Copyright (c) [2020] [Beryl Negesa Otieno]
</a>