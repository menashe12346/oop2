from postFactory import postFactory


class User:
    users = []

    def __init__(self, user_name, user_password):
        self.factory = postFactory()
        self.user_name = user_name
        self.user_password = user_password
        self.followers = []
        self.users_who_follow_me = []
        self.notifications = []
        self.logged_in = False
        self.posts = []
        User.users.append(self.user_name)

    def follow(self, other_user):
        if other_user.user_name in User.users:
            if self.logged_in:
                if other_user not in self.followers:
                    self.followers.append(other_user)
                    other_user.users_who_follow_me.append(self)
                    print(self.user_name + " started following " + other_user.user_name)

    def unfollow(self, other_user):
        if other_user.user_name in User.users:
            if self.logged_in:
                if other_user in self.followers:
                    self.followers.remove(other_user)
                    other_user.users_who_follow_me.remove(self)
                    print(self.user_name + " unfollowed " + other_user.user_name)

    def NotifyAll(self, notification):
        for user_who_follow_me in self.users_who_follow_me:
            user_who_follow_me.add_notification(notification)

    def add_notification(self, notification):
        self.notifications.append(notification)

    def print_notifications(self):
        print(self.user_name + "'s notifications:")
        for notification in self.notifications:
            print(notification)

    def publish_post(self, type_of_post, *args):
        if self.logged_in:
            self.NotifyAll(f"{self.user_name} has a new post")
            return self.factory.create_post(type_of_post, self, *args)

    def __str__(self):
        return f"User name: {self.user_name}, Number of posts: {len(self.posts)}, Number of followers: {len(self.users_who_follow_me)}"
