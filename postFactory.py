from ImagePost import ImagePost  # Importing the ImagePost class from the ImagePost module
from SalePost import SalePost  # Importing the SalePost class from the SalePost module
from TextPost import TextPost  # Importing the TextPost class from the TextPost module


class postFactory:
    # Factory class to create different types of posts

    def create_post(self, type_of_post, owner, *args):
        # Method to create a post of the specified type
        if type_of_post == "Text":  # Checking if the type of post is Text
            return TextPost(owner, *args)  # Creating and returning a TextPost object
        elif type_of_post == "Image":  # Checking if the type of post is Image
            return ImagePost(owner, *args)  # Creating and returning an ImagePost object
        elif type_of_post == "Sale":  # Checking if the type of post is Sale
            return SalePost(owner, *args)  # Creating and returning a SalePost object
        else:
            return None  # Returning None if the type of post is unknown or unsupported
