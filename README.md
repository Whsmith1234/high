# high
## Site available at
https://trusting-kalam-e9434a.netlify.app/
## Project setup
### For just the front end
```
cd into the high directory and run
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```
## Custom Backend
The file for the flask api is in the python scripts folder under flask.py
Make sure to pip install all of the dependencies at the top of the file.
Connect this file to your own remote mySQL database by replacing the 
```py
mydb = mysql.connector.connect(
      host="wpra.mysql.pythonanywhere-services.com",
      user="wpra",
      password="#######",
      database="wpra$default"
    )
```
With your own host username password and database
Then in said my sql database run the database.sql file to have the same database as mine.
## Connect front end to back
replace the base url in HelloWorld.vue with the one your flask api is running on.
```js
fetch('https://wpra.pythonanywhere.com/')
```
