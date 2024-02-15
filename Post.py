from abc import ABC

from Comment import Comment


class Post(ABC):

    def __init__(self, owner):
        owner.posts.append(self)
        self.owner = owner
        self.likes = []
        self.comments = []

    def like(self, user):
        if self.owner is not user:
            self.likes.append(user)
            notify = f"{user.user_name} liked your post"
            self.owner.add_notification(notify)
            self.send_notification(notify)

    def comment(self, user, text):
        if self.owner is not user:
            self.comments.append(Comment(user, text))
            self.owner.add_notification(f"{user.user_name} commented on your post")
            self.send_notification(f"{user.user_name} commented on your post: {text}")

    def send_notification(self, notification):
        print(f"notification to {self.owner.user_name}: {notification}")
