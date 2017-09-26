robot_price = 900
robot_tax = 1.25

book_price = 100
book_tax = 1.06

class Product:
	price = 0
	tax = 1.25

	def __init__(self, price, tax):
		self.price = price
		self.tax = tax

	def final_price(self):
		return self.price * self.tax

robot = Product(price=900, tax=1.25)
book = Product (price=100, tax=1.06)


print(robot.final_price() * 2 + book.final_price())
