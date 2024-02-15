from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class postFactory:

    def create_post(self, type_of_post, owner, *args):
        if type_of_post == "Text":
            return TextPost(owner, *args)
        elif type_of_post == "Image":
            return ImagePost(owner, *args)
        elif type_of_post == "Sale":
            return SalePost(owner, *args)
        else:
            return None
