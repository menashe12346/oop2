from Post import Post


class TextPost(Post):

    def __init__(self, owner, content):
        super().__init__(owner)
        self.content = content
        print(self.__str__())

    def __str__(self):
        return f"{self.owner.user_name} published a post:\n\"{self.content}\"\n"

