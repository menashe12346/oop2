from User import User


class SocialNetwork:
    _SocialNetwork_instance = None

    def __new__(cls, *args, **kwargs):
        if cls._SocialNetwork_instance is None:
            cls._SocialNetwork_instance = super().__new__(cls)
        return cls._SocialNetwork_instance

    def __init__(self, name):
        self.name = name
        self.users = []
        print("The social network " + name + " was created!")

    def search_for_user(self, username):
        for user in self.users:
            if username == user:
                return True
        return False

    def sign_up(self, username, password):
        if self.search_for_user(username):
            return None
        if len(password) > 8 or len(password) < 4:
            return None
        new_user = User(username, password)
        new_user.logged_in = True
        self.users.append(new_user)
        return new_user

    def log_in(self, username, password):
        for user in self.users:
            if user.user_name == username and user.user_password == password:
                user.logged_in = True
                print(f"{username} connected")

    def log_out(self, username):
        for user in self.users:
            if user.user_name == username:
                user.logged_in = False
                print(f"{username} disconnected")

    def __str__(self):
        info = f"{self.name} social network:"
        for user in self.users:
            info += "\n"+user.__str__()
        return info
