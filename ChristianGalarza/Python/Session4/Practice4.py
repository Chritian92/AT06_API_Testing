import re


def valid_email_entered(email):
    expression = re.compile('^[\w]+@[\w-]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,2})?$')
    email = str(expression.match(email))
    print("The email is valid: {}".format(email) if email != 'None' else "The email is Invalid: {}".format(email))


def valid_username_entered(username):
    expression = re.compile("[a-z0-9-_]*$")
    user = str(expression.match(username))
    if user != 'None':
        print("The username is valid: {}".format(username))
    else:
        print("The username is Invalid: {}".format(username))


def valid_password_entered(password):
    expression = re.compile("[a-zA-Z0-9]{8,16}$")
    password = str(expression.match(password))
    if password != 'None':
        print("The password is valid: {}".format(password))
    else:
        print("The password is Invalid: {}".format(password))


valid_username_entered("RABBIT")
valid_username_entered("user1234")

valid_password_entered("Pass123")
valid_password_entered("eisnuodr452862lk")

valid_email_entered("helloworld@gmail.com")
valid_email_entered("helloworld@gmail.com.bol")
valid_email_entered("helloworld@gmail.com.bo")
