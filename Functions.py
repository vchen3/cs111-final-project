# Vivien Chen and Audrey Fok
# CS111 Final Project
# Functions File

captions = ['Welcome!','You put your iPod on shuffle- what"s the first song that pops up?','You"ve had a long day of coding.  What TV show do you tune into?','What candy do you secretly steal from the Halloween basket?','How do you prefer to spend a Saturday afternoon?',"Throwback to high school! Which line do you use to ask someone to prom?"]

def createListOfAnswers(fileName):    
    '''Creates a list with one dictionary per question (5 dictionaries total).  
    Each dictionary's key is the question number, and the value is a subdictionary.  
    The subdictionary key is the shown answer, and the value is the corresponding professor's name.'''
    mainlist = []
    lines = open(fileName).readlines() #opening our file of information
    for line in lines:
        d = {}
        subdictionary = {}
        splitLine = line.split(';') #split each line on the semicolon
        d[splitLine[0].strip()] = subdictionary #adds question number to main dictionary, sets subdict as value
        for i in range(1, len(splitLine)):
            subdictionary[getKey(splitLine[i])] = getValue(splitLine[i]) #creates subdictionary
        mainlist.append(d)
    return mainlist

def getKey(s): 
    '''Returns that portion of string s to the left 
    of the first equal sign, with flanking white space
    removed.'''
    return s[0:s.find('=')].strip()

def getValue(s):
    '''Returns that portion of string s to the right 
    of the first equal sign, with flanking white space
    removed.'''
    return s[(s.find('=')+1):].strip()
    
def returnanswers(dictionary): 
    '''Takes a dictionary and returns list of shown answers '''
    listofvalues = dictionary.values() #list with the subdictionary within
    for subdictionary in listofvalues: #looking within this one subdict
        subkeys = subdictionary.keys() #this is a list of all of the answers
        return subkeys


listofdicts = createListOfAnswers('REALinfo.txt') #MAJOR list of dictionaries (includes subdicts) #whole shebang

#possibleanswers = ['Gimme Shelter - The Rolling Stones','Finding Your Roots with Henry Louis Gates Jr.', 'Wilko Mints','Boating along the gorgeous Charles River', 'Kickbox into their classroom and drop a sick Game of Thrones pickup line!']

def storage(listofanswers,masterlist):  #takes stored answers and masterlist and creates dictionary with keys = professor names, and values = count
    testdict = {}  
    for answer in listofanswers: #considers each stored value
        for dictionary in masterlist: #considers each question number
            printer = dictionary.values() #List with one subdictionary in it
            for item in printer: #item is a dictionary
                if answer in item: #if the stored value is in that subdictionary
                    profname= item[answer] 
                    if profname not in testdict: #add professor to dictionary of stored answers
                        testdict[profname] = 1
                    else:
                        testdict[profname]+=1 #increase count of professor
    return testdict

#hello = {'cat':5,'middle':4, 'bottle':3, 'test': 2}
#^Example of storage in action

def findingthetruth(dictionary): 
    '''Returns which CS prof you are'''
    list = []
    for name in dictionary:
        number = dictionary[name]
        list.append(number)
    highestnum= max(list)
    for item in dictionary:
        if dictionary[item] == highestnum:
            yourinnerprof = item  #Returns name of professor with highest count
            return yourinnerprof
        #if tie- inherently chooses randomly
    
     
    