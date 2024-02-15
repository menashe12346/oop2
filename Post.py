from abc import ABC  # Importing the ABC class from the abc module
from Comment import Comment  # Importing the Comment class from the Comment module


class Post(ABC):
    # Abstract base class for posts

    def __init__(self, owner):
        # Initializing the Post object with an owner and initializing attributes
        owner.posts.append(self)  # Adding the post to the owner's list of posts
        self.owner = owner  # Setting the owner of the post
        self.likes = []  # List to hold users who liked the post
        self.comments = []  # List to hold comments on the post

    def like(self, user):
        # Method to like the post
        if self.owner is not user:  # Checking if the owner is not the user
            self.likes.append(user)  # Adding the user to the list of likes
            notify = f"{user.user_name} liked your post"  # Creating a notification message
            self.owner.add_notification(notify)  # Adding the notification to the owner's notifications
            self.send_notification(notify)  # Sending the notification

    def comment(self, user, text):
        # Method to add a comment to the post
        if self.owner is not user:  # Checking if the owner is not the user
            self.comments.append(Comment(user, text))  # Creating a new comment and adding it to the post
            self.owner.add_notification(f"{user.user_name} commented on your post")  # Adding a notification about the comment to the owner's notifications
            self.send_notification(f"{user.user_name} commented on your post: {text}")  # Sending a notification about the comment

    def send_notification(self, notification):
        # Method to send a notification to the post owner
        print(f"notification to {self.owner.user_name}: {notification}")  # Printing the notification message
