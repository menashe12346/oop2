from Post import Post


class SalePost(Post):

    def __init__(self, owner, content, price, place):
        super().__init__(owner)
        self.content = content
        self.price = price
        self.place = place
        self.isSold = False
        print(self.__str__())

    def discount(self, percentage, password):
        if not self.isSold and self.owner.user_password == password:
            self.price -= self.price * percentage / 100
            print(f"Discount on Charlie product! the new price is: {self.price}")

    def sold(self, password):
        if self.owner.user_password == password:
            self.isSold = True
            print(f"{self.owner.user_name}'s product is sold")

    def __str__(self):
        return f"{self.owner.user_name} posted a product for sale:\n{'Sold!' if self.isSold else 'For sale!'} {self.content}, price: {self.price}, pickup from: {self.place}\n"
