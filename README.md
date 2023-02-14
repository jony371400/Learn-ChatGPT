# This Project is used [ChatGPT] to create a Login API Service

## Step

> Give GPT Cmd to execute
```
Use Python Flask to create a login API Service with register account and delete account, also use SQLite database to storage user infomation
```
![Image](https://github.com/jony371400/Learn-ChatGPT/blob/main/Pic/cmd.png)

> Get the response
```
Here's an example code for creating a login API service using Flask in Python and a SQLite database to store user information, with support for registering and deleting user accounts:
```
![Image](https://github.com/jony371400/Learn-ChatGPT/blob/main/Pic/response.png)

> Finally , GPT will teach you how to use
```
In this example, we define a get_db_connection function that returns a connection to the SQLite database users.db. We also define a create_table function that creates a users table in the database if it does not exist.

The /register route is used to accept POST requests for user registration. The function checks if the request contains a username and password, and then queries the users table for an existing user with the same username. If the username already exists, an error message is returned, otherwise the user is added to the database.

The /login route is used to accept POST requests for user authentication. The function checks if the request contains a username and password, and then queries the users table for a matching username and password. If the credentials are correct, a success message is returned, otherwise an error message is returned.

The /users/<username> route is used to accept DELETE requests for deleting a user. The function queries the users table for the specified username and deletes the user if they exist, otherwise an error message is returned.

Note that this example uses a very simple table structure and basic authentication, which are not recommended for production environments
```
![Image](https://github.com/jony371400/Learn-ChatGPT/blob/main/Pic/infomation.png)

> Done , easy right?