from Post import Post  # Importing the Post class from the Post module


class TextPost(Post):
    # Subclass of Post for text-based posts

    def __init__(self, owner, content):
        # Initializing the TextPost object with an owner and content
        super().__init__(owner)  # Calling the superclass's __init__() method
        self.content = content  # Setting the content of the text post
        print(self.__str__())  # Printing a message indicating the creation of the text post

    def __str__(self):
        # Method to return a string representation of the TextPost object
        return f"{self.owner.user_name} published a post:\n\"{self.content}\"\n"  # Returning a string indicating that the owner published a post with the specified content
