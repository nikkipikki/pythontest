robot_price = 900
robot_tax = 1.25

book_price = 100
book_tax = 1.06

class Product:
	price = 0
	tax = 1.25

robot = Product()
robot.price = 900

book = Product()
book.price = 100 
book.tax = 1.06

print(robot.price * 2 * robot.tax + book.price * book.tax)
