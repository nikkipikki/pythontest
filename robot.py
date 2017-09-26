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
		total = self.price * self.tax
		if total > 500:
			return 0.9 * total
		else:
			return total	

products = [Product(price=900 * 2, tax=1.25), Product(price=100, tax=1.06)]
total_price = 0
for product in products:
	total_price = total_price + product.final_price()
	print(total_price)
