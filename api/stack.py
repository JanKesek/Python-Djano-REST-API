import json


class Car:
	def __init__ (self, registration_number,passangers_number,production_year,producer,model,type_of_car): 
		self.registration_number = registration_number
		self.passangers_number = passangers_number
		self.production_year = production_year
		self.producer = producer
		self.model = model
		self.type_of_car = type_of_car


class Fleet:
	def __init__(self):
		self.items = []

	def push(self, new_car):
                self.items.append(new_car)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]	
	def print_last(self):
		print json.dumps(self.items[len(self.items)-1])

	def print_all(self):
		for i in range(0, len(self.items)):
			print json.dumps(self.items[i])
	def change_key(self,car, key, value):
		car[key] = value

fleet = Fleet()

car1 = { 
"registration_number": 12345, 
"passangers_number": 3, 
"production_year":1990,
"producer": "Mazda",
"model": 2,
"type_of_car": "Sedan" }


car2 = {
"registration_number":44662,
"passangers_number":6,
"production_year":1990,
"producer" : "Toyota",
"model" : 5,
"type_of_car" :"Sedan"
}
toyota = Car(12345,3,1945,"Toyota", 14, "Kombii")
fleet.push(car1)
fleet.push(car2)
fleet.change_key(car2, "producer", "Mercedes")
print(fleet.print_last())
print(fleet.print_all())
