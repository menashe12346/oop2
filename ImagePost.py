from Post import Post  # Importing the Post class from the Post module
import matplotlib.pyplot as plt  # Importing the pyplot module from matplotlib
import matplotlib.image as mpimg  # Importing the image module from matplotlib


class ImagePost(Post):
    # Subclass of Post for image posts

    def __init__(self, owner, path):
        # Initializing the ImagePost object with an owner and path to the image
        super().__init__(owner)  # Calling the superclass's __init__() method
        self.path = path  # Setting the path to the image file
        print(self.__str__())  # Printing a message indicating the creation of the image post

    def display(self):
        # Method to display the image
        image_data = mpimg.imread(self.path)  # Load the image data from the file path
        imgplot=plt.imshow(image_data)
        plt.axis('off')
        plt.show()  # Display the image using imshow()
        print("Shows picture")  # Printing a message indicating the image is displayed

    def __str__(self):
        # Method to return a string representation of the ImagePost object
        return f"{self.owner.user_name} posted a picture\n"  # Returning a string indicating that the owner posted a picture
