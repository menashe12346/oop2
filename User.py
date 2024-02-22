from postFactory import postFactory  # Importing the postFactory class from the postFactory module


class User:
    users = []  # Class variable to hold the list of usernames

    def __init__(self, user_name, user_password):
        # Initializing the User object with a username, password, and other attributes
        self.factory = postFactory()  # Creating an instance of the postFactory class
        self.user_name = user_name  # Setting the username
        self.user_password = user_password  # Setting the password
        self.followers = []  # List to hold followers
        self.users_who_follow_me = []  # List to hold users who follow the current user
        self.notifications = []  # List to hold notifications
        self.logged_in = False  # Boolean to track login status
        self.posts = []  # List to hold user's posts
        User.users.append(self.user_name)  # Adding the username to the list of usernames

    def follow(self, other_user):  # here I used the observer pattern to add new observer
        # Method to follow another user
        if other_user.user_name in User.users:  # Checking if the other user exists
            if self.logged_in:  # Checking if the current user is logged in
                if other_user not in self.followers:  # Checking if the current user is not already following the other user
                    self.followers.append(other_user)  # Adding the other user to the followers list
                    other_user.users_who_follow_me.append(
                        self)  # Adding the current user to the other user's followers list
                    print(
                        self.user_name + " started following " + other_user.user_name)  # Printing a message indicating the follow action
                    return
        raise Exception("action not allowed.")

    def unfollow(self, other_user):  # here i used the observer pattern to remove observer
        # Method to unfollow another user
        if other_user.user_name in User.users:  # Checking if the other user exists
            if self.logged_in:  # Checking if the current user is logged in
                if other_user in self.followers:  # Checking if the current user is following the other user
                    self.followers.remove(other_user)  # Removing the other user from the followers list
                    other_user.users_who_follow_me.remove(
                        self)  # Removing the current user from the other user's followers list
                    print(
                        self.user_name + " unfollowed " + other_user.user_name)  # Printing a message indicating the unfollow action
                    return
        raise Exception("action not allowed.")

    def NotifyAll(self, notification):  # here i used the observer pattern to notify all the observers
        # Method to notify all users who follow the current user
        for user_who_follow_me in self.users_who_follow_me:
            user_who_follow_me.add_notification(notification)

    def add_notification(self, notification):
        # Method to add a notification to the current user's notification list
        self.notifications.append(notification)

    def print_notifications(self):
        # Method to print all notifications for the current user
        print(self.user_name + "'s notifications:")
        for notification in self.notifications:
            print(notification)

    def publish_post(self, type_of_post, *args):
        # Method to publish a new post
        if self.logged_in:  # Checking if the current user is logged in
            self.NotifyAll(f"{self.user_name} has a new post")  # Notifying all users who follow the current user about the new post
            return self.factory.create_post(type_of_post, self, *args)  # Creating and returning a new post using the postFactory
        raise Exception("action not allowed.")

    def __str__(self):
        # Method to return a string representation of the User object
        return f"User name: {self.user_name}, Number of posts: {len(self.posts)}, Number of followers: {len(self.users_who_follow_me)}"
