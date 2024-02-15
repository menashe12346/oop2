from User import User  # Importing the User class from the User module


class SocialNetwork:
    _SocialNetwork_instance = None  # Class variable to hold the single instance of the SocialNetwork class

    def __new__(cls, *args, **kwargs):
        # Implementing Singleton design pattern to ensure only one instance of SocialNetwork class is created
        if cls._SocialNetwork_instance is None:
            cls._SocialNetwork_instance = super().__new__(cls)
        return cls._SocialNetwork_instance

    def __init__(self, name):
        # Initializing the SocialNetwork object with a name
        self.name = name
        self.users = []  # List to hold user objects
        print("The social network " + name + " was created!")  # Printing a message indicating the creation of the social network

    def search_for_user(self, username):
        # Method to search for a user by username
        for user in self.users:
            if username == user:
                return True  # Return True if user is found
        return False  # Return False if user is not found

    def sign_up(self, username, password):
        # Method to sign up a new user
        if self.search_for_user(username):  # Check if the username already exists
            return None  # Return None if the username already exists
        if len(password) > 8 or len(password) < 4:  # Checking password length
            return None  # Return None if password length is invalid
        new_user = User(username, password)  # Creating a new User object
        new_user.logged_in = True  # Setting the new user's login status to True
        self.users.append(new_user)  # Adding the new user to the list of users
        return new_user  # Returning the new user object

    def log_in(self, username, password):
        # Method to log in a user
        for user in self.users:
            if user.user_name == username and user.user_password == password:  # Checking username and password
                user.logged_in = True  # Setting the user's login status to True
                print(f"{username} connected")  # Printing a message indicating the user has connected

    def log_out(self, username):
        # Method to log out a user
        for user in self.users:
            if user.user_name == username:
                user.logged_in = False  # Setting the user's login status to False
                print(f"{username} disconnected")  # Printing a message indicating the user has disconnected

    def __str__(self):
        # Method to return a string representation of the SocialNetwork object
        info = f"{self.name} social network:"  # Initializing the info string
        for user in self.users:
            info += "\n"+user.__str__()  # Adding each user's string representation to the info string
        return info  # Returning the info string
