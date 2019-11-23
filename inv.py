class Product:
	def __init__(self, id ,name, quantity=0):
		self.id = id
		self.name = name 
		self.quantity = quantity

class Inventory:
	def __init__(self):
		self.products=[]

	'''Adds a new product to products list'''
	def add_products(self, id, name, quantity):
		self.products.append(Product(id, name, quantity))
		return self.products

	'''Displays product quantity by looking
	for product name in the list of products'''
	def product_quantity(self, product_name):
		for product in self.products:
			if product.name==product_name:
				print(product.quantity)
			else:
				print("That product does not exist")
	
	'''change product name by looking for all
	 product name and replacing it with new name'''
	def modify_product_name(self,old_name, new_name):
		for product in self.products:
			if product.name == old_name:
				product.name = new_name #Set product name to the new name
				print('Name successfully change')
			else:
				print('That product does not exist')

	'''Looks for given product name in products
	and deduct a particular quantity of that 
	product as demanded by the user '''
	def take_product(self, product_name, quantity):
		for product in self.products:
			if product_name == product_name:
				if product.quantity<=0:
					print('{} product is finish'.format(product.name.capitalize()))
				elif quantity > product.quantity:
					print('Your demand is more than available products.Available Product {}'.format(product.quantity))
				else:
					product.quantity -= quantity
					print('product successfully taken new quantity is {}'.format(product.quantity))
			else:				
				print('That product does not exist')



	def add_existing_product(self, product_name, product_quantity):
		for product in self.products:
			if product.name==product_name:
				product.quantity+=product_quantity
				print('Added successfully')
			else:
				print('Product [{}] does not exist.Enter [2] to add new product or [7] to view available products'.format(product_name))


	def list_all_products(self):
		new_products=[]
		for product in self.products:
			if product.quantity>0:
				new_products.append(product)
			else:
				print('{} is finish.'.format(product.name))

			total_products=len(new_products)
			print('''
			Total products is {}
			=================
			'''.format(total_products))
			for product in new_products:
				print(product.name, ' --->  {}'.format(product.quantity))



class Menu:
	def __init__(self):
		self.inventory = Inventory()

	def add_product(self):
		id = int(input('Enter product id'))
		product_name = input('Enter product name')
		product_quantity = int(input('Enter product quantity'))
		self.inventory.add_products(id, product_name, product_quantity)
		print('Sucessfully added')


	def adding_existing_product(self):
		try:
			product_name = input('Enter the product name')
			product_quantity = int(input('Enter quantity you wish to add'))
			self.inventory.add_existing_product(product_name, product_quantity)

		except Exception as e:
			print('Enter product name and product quatity')



	def check_product_quantity(self):
		try:
			product_name = input('enter a product name')
			self.inventory.product_quantity(product_name)

		except Exception as e:
			print('please make sure to enter product name'.capitalize())



	def change_product_name(self):
		try:
			old_name = input('Enter old product name')
			new_name = input('Enter new name')
			self.inventory.modify_product_name(old_name, new_name)

		except Exception as e:
			print('please make sure to enter old name and the new name you want'.capitalize())




	def send_out_some_products(self):
		try:
			product_name = input('Enter product name')
			product_quantity = int(input('Enter product quantity'))
			self.inventory.take_product(product_name, product_quantity)

		except Exception as e:
			print('please make sure to enter product name and product quantity'.capitalize())


	def show_all_products(self):
		self.inventory.list_all_products()




	def  display(self):

		print('''
			Welcome to Inventory Manager
			============================
			          Chioces 
			          -------
			     Enter    Function
			     -----    --------    
			     2 -------- Add new product
			     3 -------- Check product quantity
			     4 -------- Change product name
			     6 -------- Get some products
			     7 -------- See all products 
			     8 -------- Increase existing product quantity                
			''')

	def run(self):
		
		self.display()

		while True:
			try:

				choice = int(input('Enter your choice'))

				if choice == 2:
					self.add_product()
				elif choice == 3:
					self.check_product_quantity()
				elif choice == 4:
					self.change_product_name()
				elif choice == 6:
					self.send_out_some_products()
				elif choice == 7:
					self.show_all_products()
				elif choice == 8:
					self.adding_existing_product()
			except Exception as e:
				print('Please you must enter a choice')

if __name__ == '__main__':
	Menu().run()


