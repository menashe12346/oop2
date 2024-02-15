from Post import Post
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImagePost(Post):

    def __init__(self, owner, path):
        super().__init__(owner)
        self.path = path
        print(self.__str__())

    def display(self):
        image_data = mpimg.imread(self.path) # Load the image data from the file path
        plt.imshow(image_data) # Display the image using imshow()
        print("Shows picture")

    def __str__(self):
        return f"{self.owner.user_name} posted a picture\n"
