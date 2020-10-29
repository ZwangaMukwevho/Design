import sys
import subprocess

class admin:

	
	def createUser(self,name,password):
		"""
		Creates a user with the given name and password
		"""
		file1 = open(r"/home/pi/Design/users.txt","a")
		line = name+" "+password + "\n"
		file1.writelines(line)
	
	
	def check(self,name,password):
		"""
		checks if the user exists
		"""
		file1 = open(r"/home/pi/Design/users.txt","r")
		lines = file1.readlines()

		for line in lines:
			splitList = line.split()

			if(name == splitList[0] and password == splitList[1]):
				return True
		return False

	def checkPassword(name):
		"""
		Returns users password if they have forgotten it
		"""
		file1 = open(r"/home/pi/Design/users.txt","r")
		lines = file1.readlines()

		for line in lines:
			splitList = line.split()

			if(name == splitList[0] ):
				return splitList[1]

		return "Not found"
	
	"""def deleteUser(name):
	def makeAdmin(name):"""

	string = checkPassword("sadiki")
	print(string)
