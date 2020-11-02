import sys
import subprocess

class admin:
	"""This is a class manages the users who use the system  and also allows user to be created, check if the user exists, check the users password

    """

	
	def createUser(name,password):
		"""[Writes the name and password of the user in a textfile in a newline]

		:param name: [This is the name the user will use to login.]
		:type name: [string]
		:param password: [This is the password the user uses to sign in]
		:type password: [string]
		"""
		file1 = open(r"/home/pi/Design/users.txt","a")
		line = name+" "+password + "\n"
		file1.writelines(line)
	
	
	def check(self,name,password):
		"""[checks if the user is registered user, does this by checking if they're name and password is in the textfile.The name should also match the corresponding password.]

		:param name: [This is the name the user uses to login]
		:type name: [string]
		:param password: [This is the password the user will uses to login.]
		:type password: [string]
		:return: [Returns True if the user was successfuly validated and False if the user was not successfuly validated.]
		:rtype: [bool]
		"""
		file1 = open(r"/home/pi/Design/users.txt","r")
		lines = file1.readlines()

		for line in lines:
			splitList = line.split()

			if(name == splitList[0] and password == splitList[1]):
				return True
		return False

	def checkPassword(self,name):
		"""[Takes in a username and returns the corresponding password to the username]

		:param name: [This is the name the user uses to login.]
		:type name: [string]
		:return: [plitList[0] which is the password of the user or Not found (str): Returns a ``Not found`` string if the corresponding username is not registered]
		:rtype: [string]
		"""
		file1 = open(r"/home/pi/Design/users.txt","r")
		lines = file1.readlines()

		for line in lines:
			splitList = line.split()

			if(name == splitList[0] ):
				return splitList[1]

		return "Not found"

