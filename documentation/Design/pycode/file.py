
class file:
    """
    This is a class that represents a file object

    Attributes:
        id (String): The real part of complex number.
        name (String): The imaginary part of complex number.
        date (String): The date of the file was created
        size(String): The size of the file
        url(String): The url in which the file was downloaded from
    """

    Id = ""
    name = ""
    date = ""
    size = ""
    url = ""

#https://homes.cs.washington.edu/~djg/teachingMaterials/spac/sophomoricParallelismAndConcurrency.pdf

    def __init__(self,ID,Name,Url):
        """
        Constructor that initializes the Id, name and url
        """
        self.Id = ID
        self.name = Name
        self.url = Url

    def getName(self):
        """
        get the name of the file
        """
        return  name

    def getSize(self):
        """
        get the size of the file
        """
        return size

    def getDate(self):
        """
        get the date of the file
        """
        return date

    def getUrl(self):
        """
        get the url from which the file was downloaded from
        """
        return url

    def setName(self,Name):
        """
        set the name of the file
        """
        self.name = Name

    def setSize(self,Size):
        """
        set the size of the file
        """
        self.size = Size

    def setDate(self,Date):
        """
        set the date of the file
        """
        self.date = Date

    def setUrl(self,Url):
        """
        set the url which the file can be downloaded from
        """
        self.url = Url