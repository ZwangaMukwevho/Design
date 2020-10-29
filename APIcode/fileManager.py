# Imported files
import sys
import subprocess

class fileManager:
	"""
    This is a class that manages files.
	Allows the downloading, seaching and deleting of files 

    Attributes:
        command (String): Name of command [e.d download, delete, search]
        url(String): Url to download the file
    """


	def splitUrl(self,url):
		"""
		Takes a url, splites it to and splits it to get the file type
		"""
		
		urlList = url.split("/")
		if len(urlList) == 1:
			return "invalid URL given"
		else:
			return urlList
		


	def obtainName(self,nameList):
		"""
        Obtains the name of the file from the url
        """

		# Obtaining the name of file with type
		length = len(nameList) -1
		nameWithtype = nameList[length]

		#Obtaining the name of the file
		typeList = nameWithtype.split(".")
		name = typeList[0]
		return name

	def obtainType(self,nameList):
		"""
        Obtains the type of the file from the url
        """

		# Obtaining the name of file with type
		length = len(nameList) -1
		nameWithtype = nameList[length]

		#Obtaining type of the file
		typeList = nameWithtype.split(".")
		fileType = typeList[1]
		return fileType

	
	def donwloadFile(self,URL,fName,fType):
		"""
		downloads the file from the url given
        """		
		
		outName = fName + "." + fType
		subprocess.run(["curl","-O",URL])
		#subprocess.run(["mv",outName,"/media/usb/files"])
		subprocess.run(["mv",outName,"/home/pi/files"])
	
	def authDownload(self,URL,username,password,outName):
		"""	
		Downloads the file from a website that requires authentication
		"""
		authToken = username+":"+password
		
		subprocess.run(["curl","-u",authToken,"-O",URL])
		print(outName)
		subprocess.run(["mv",outName,"/home/pi/files"])
		

	def searchFile(self,fName):
		"""
		searches for the fileName in the usb module
		returns the name of the file if successful and returns an empty string if no match is found
        """
		searchName = fName + "*"
		#out = subprocess.Popen(["find","/media/usb/files","-name", searchName],stdout=subprocess.PIPE)
		out = subprocess.Popen(["find","/home/pi/files","-name", searchName],stdout=subprocess.PIPE)

		#Removing the "\n" at the end of the line
		output = out.stdout.read()[:-1:]
		return output

	def deleteFile(self,fName):
		"""
		deletes the file given as the usb
        """
		
		#searchName = fName + "*"
		searchName = fName
		#out = subprocess.Popen(["find","/media/usb/files","-name", searchName,"-delete"],stdout=subprocess.PIPE)
		out = subprocess.Popen(["find","/home/pi/files","-name", searchName,"-delete"],stdout=subprocess.PIPE)
		return out
	
		


	
	


	
	
	
	
	
	
	

