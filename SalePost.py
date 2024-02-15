from Post import Post  # Importing the Post class from the Post module


class SalePost(Post):
    # Subclass of Post for sale posts

    def __init__(self, owner, content, price, place):
        # Initializing the SalePost object with an owner, content, price, and place
        super().__init__(owner)  # Calling the superclass's __init__() method
        self.content = content  # Setting the content of the sale post
        self.price = price  # Setting the price of the sale post
        self.place = place  # Setting the pickup location of the sale post
        self.isSold = False  # Boolean to track whether the product is sold
        print(self.__str__())  # Printing a message indicating the creation of the sale post

    def discount(self, percentage, password):
        # Method to apply a discount to the sale post
        if not self.isSold and self.owner.user_password == password:  # Checking if the product is not sold and the password is correct
            self.price -= self.price * percentage / 100  # Calculating the discounted price
            print(f"Discount on {self.owner.user_name}'s product! The new price is: {self.price}")  # Printing a message indicating the discounted price

    def sold(self, password):
        # Method to mark the product as sold
        if self.owner.user_password == password:  # Checking if the password is correct
            self.isSold = True  # Marking the product as sold
            print(f"{self.owner.user_name}'s product is sold")  # Printing a message indicating that the product is sold

    def __str__(self):
        # Method to return a string representation of the SalePost object
        return f"{self.owner.user_name} posted a product for sale:\n{'Sold!' if self.isSold else 'For sale!'} {self.content}, price: {self.price}, pickup from: {self.place}\n"  # Returning a string indicating the owner posted a product for sale with the specified details
