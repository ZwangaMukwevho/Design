import pytest
import fileManager

FM = fileManager.fileManager()

def test_splitUrl_correctFormatting():
    """Tests if splitUrl returns the correct list when tested on valid list
    """
    FM = fileManager.fileManager()
    testList = FM.splitUrl('https://homes.cs.washington.edu/~djg/teachingMaterials/older/sophomoricParallelismAndConcurrency092710.pdf')
    assert testList ==  ['https:', '', 'homes.cs.washington.edu', '~djg', 'teachingMaterials', 'older', 'sophomoricParallelismAndConcurrency092710.pdf']

def test_splitUrl_incorrectUrl():
    """Tests if split url handles incorrect list being supplied to it
    """
    FM = fileManager.fileManager()
    testList = FM.splitUrl('httpshomes.cs.washington.edu~djgteachingMaterialsoldersophomoricParallelismAndConcurrency092710.pdf')
    assert testList ==  "invalid URL given"

def test_splitUrl_incorrectParameter():
    """Tests the behaviour of splitUrl if it is given an int as a parameter
    """
    FM = fileManager.fileManager()
    testList = FM.splitUrl(22)
    assert testList ==  "invalid URL given"

def test_obtainName_correctFormatting():
    """Tests behaviour of obtainName() if it is given a correct nameList
    """
    FM = fileManager.fileManager()
    testList = ['https:', '', 'homes.cs.washington.edu', '~djg', 'teachingMaterials', 'older', 'sophomoricParallelismAndConcurrency092710.pdf']
    testName = FM.obtainName(testList)
    assert testName == "sophomoricParallelismAndConcurrency092710"

def test_obtainName_incorrectList():
    """ Checks how obtainName behaves if it is given a list with wrong content
    """
    testList = ["one","two","three"]
    testName = FM.obtainName(testList)
    assert testName == ""

def test_obtainName_incorrectparameter():
    """ Checks how obtainName behaves if it is given a list with wrong content
    """
    testName = FM.obtainName(22)
    assert testName == ""

def test_obtaintType_correctFormatting():
    """Tests behaviour of obtainType() if it is given a correct nameList
    """
    FM = fileManager.fileManager()
    testList = ['teachingMaterials', 'older', 'sophomoricParallelismAndConcurrency09271.docx']
    testName = FM.obtainType(testList)
    assert testName == "docx"

def test_obtainType_incorrectList():
    """ Checks how obtainType behaves if it is given a list with wrong content
    """
    testList = [0,11,22]
    testName = FM.obtainType(testList)
    assert testName == ""

def test_obtainType_incorrectparameter():
    """ Checks how obtainType behaves a string as a parameter as opposed to a list
    """
    testName = FM.obtainType("hello")
    assert testName == ""

def test_searchFile():
    """Tests behaviour the searchFile function it is given parameters that are not strings"""
    output = FM.searchFile(98)
    assert output == ""

def test_deleteFile():
    """Tests behaviour of deleteFile function if it is given parameters that not strings"""
    mylist = ["one","two"]
    output = FM.deleteFile(mylist)
