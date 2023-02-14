# This Project is used [ChatGPT] to create a Login API Service

## Step to [Create]

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

> Done , easy right ?

## Step to [Test]

> Give GPT Cmd to execute
```
Thanks , so how do I test /register when i use PostMan tool
```
![Image](https://github.com/jony371400/Learn-ChatGPT/blob/main/Pic/testcmd.png)

> Get the response
```
To test the /register route using Postman, you can follow these steps:

1. Open Postman and create a new POST request.
2. Enter the URL of your Flask application followed by /register. For example, http://localhost:5000/register.
3. Select the "Basic Auth" tab and enter the username and password you want to use for registration in the "Username" and "Password" fields.
4. Click the "Send" button to send the request.

If the registration is successful, you should receive a JSON response with the message "Registration successful" and a status code of 201. If the registration fails, you will receive an error message and a different status code.
```
![Image](https://github.com/jony371400/Learn-ChatGPT/blob/main/Pic/testresponse.png)

> Done , easy right ?

> So , the /login & /users/<username> also the same way to [Test]

## Epilogue
> [ChatGPT] is a good tools to used to help anyone , you can use this tool to help you have many idea to reference .