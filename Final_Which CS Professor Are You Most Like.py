#Vivien Chen and Audrey Fok
#CS 111 Final Project
#Due Dec 9 2014

from Tkinter import *
import random
from Functions import *
#from Animations import *

class QuestionsAndAnswers: #Creates questions and answers
    def __init__(self, filename):
        lines = open(filename).readlines()
        self.QandA_list = []     # A list of question/answer tuples read in from file
        for line in lines:  # Populate list of questions/answers with data from file
            splitLine = line.strip().split(';')  # Assumes tab-delimited file
            self.QandA_list.append(splitLine)

    def get_random_QandA_number(self):
        '''Every question/answer has a number associated with it, i.e., the index
        it occurs in the list. Return the number associated with a randomly
        chosen question/answer.'''
        return random.randint(0, len(self.QandA_list)-1)

    def getQuestion(self, number):
        '''Returns the question associated with the given number.'''
        return self.QandA_list[number][0] 

    def getAnswer(self, number):
        '''Returns the answer associated with the given number.'''
        return self.QandA_list[number][1:]


class CSProfApp(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.QA = QuestionsAndAnswers('REALinfo.txt')
        self.title('Which CS Professor Are You Most Like?')
        self.grid()
        self.totalNumberOfQuestions = 5  # Total number of questions
        self.currentQuestionNumber = 1    # Current question number (increments with after each question)
        self.indexOfCurrentQuestion = self.QA.get_random_QandA_number()  # Number/index of current question
        self.awaitingUserToSubmitAnswer = True  # Are we waiting for the user to submit an answer to a question (True)? Or if user has already submitted an answer and we are waiting for the user to press the "Next" button (False)?
        self.createWidgets()

    def createWidgets(self):

        # Image and Title
        pic = PhotoImage(file='background.gif')
        imageLabel = Label(self, image=pic,borderwidth=0)
        imageLabel.pic = pic
        imageLabel.grid(row=0,column=0)
        titleLabel = Label(self, text='Which CS Professor Are You Most Like?', bg='white', font='Century 26 bold')
        titleLabel.grid(row=0,column =1, sticky=N+E+W+S)

        # Question
        self.question = StringVar()
        questionLabel = Label(self, fg='hotpink', font='Century 14', textvariable=self.question)
        questionLabel.grid(rowspan=4,column=0,sticky=E)
        self.setQuestion()  # Set text of question

        # Answers
        self.answerIndex = IntVar()  # Index of selected radiobutton
        self.answerTexts = []  # List of StringVars, one for each radiobutton. Each list element allows getting/setting the text of a radiobutton.
        for i in range(0, 4):
            self.answerTexts.append(StringVar())
        for i in range(0, 4):  # Create radiobuttons
            rb = Radiobutton(self, fg='red', font='Century 14', textvariable=self.answerTexts[i], variable=self.answerIndex, value=i)
            rb.grid(row=1+i, column=1, sticky=W)
        self.setAnswers()  # Set text of radiobuttons

        # Status Label
        self.results = StringVar()
        self.resultsLabel = Label(self, fg='brown', font='Times 14 italic', textvariable=self.results)
        self.resultsLabel.grid(row=5,column=0)

        # Submit Button
        self.submitButton = Button(self, text='Submit', command=self.onSubmitButtonClick)
        self.submitButton.grid(row=6,column=1)

        # Quit Button        
        quitButton = Button(self, text='Quit', command=self.onQuitButtonClick)
        quitButton.grid(row=6,column=0,sticky=W)

    def setQuestion(self):
        freckle = captions[self.currentQuestionNumber]
        self.question.set('Question ' + str(self.currentQuestionNumber) + ' out of ' + str(self.totalNumberOfQuestions) + '.\n' + freckle)
            
    def setAnswers(self):
        '''Populates the answer radiobuttons in a random order 
        with the correct answer as well as random answers.'''
        yo = self.currentQuestionNumber-1
        answers = returnanswers(listofdicts[yo])
        self.answers = answers
        for i in range(0, len(answers)):  # Populate text of radiobuttons
            self.answerTexts[i].set(answers[i])
    global storedanswers
    storedanswers=[] #Creates list of user's stored answers
    def onSubmitButtonClick(self):
        if self.awaitingUserToSubmitAnswer:  # "Submit" button was just pressed.
            self.awaitingUserToSubmitAnswer = not self.awaitingUserToSubmitAnswer  # Toggle value of "Submit"/"Next" button.
            self.submitButton.config(text='Next')  # Change "Submit" button to "Next"
            hawaii = int(self.answerIndex.get()) #hawaii = index of answers
            crayon = self.answers[hawaii] #Searching for corresponding answer
            storedanswers.append(crayon) #Add chosen answer to storedanswers
        else:  # "Next" button was just pressed.
            if self.currentQuestionNumber == self.totalNumberOfQuestions:  # End of game. All questions answered.
                pen = storedanswers #calling storedanswers again
                water = storage(storedanswers,listofdicts) #creates dictionary of prof name with corresponding count
                oracle = findingthetruth(water) #Returns prof name with max count
                self.results.set('Congratulations!  You are most like ' + oracle + '!')             
                self.submitButton.config(text='Replay', command=self.replay) #Offers opportunity to replay
                #if oracle == 'Rhys': #gui with picture of corresponding professor pops up
                #    runAnswer('rhys.gif')
                #elif oracle == 'Sohie':
                #    runAnswer('sohie.gif')
                #elif oracle == 'Jean':
                #    runAnswer('jean.gif')
                #elif oracle == 'Brian':
                #    runAnswer('Brian.gif')
                
            else:  # Move to next question
                self.awaitingUserToSubmitAnswer = not self.awaitingUserToSubmitAnswer  # Toggle value of "Submit"/"Next" button.
                self.submitButton.config(text='Submit')  # Change "Next" button to "Submit"
                self.currentQuestionNumber += 1
                self.indexOfCurrentQuestion +=1
                self.setQuestion()  # Populate text of question
                self.setAnswers()  # Populate text of answer radiobuttons
                
   

    def onQuitButtonClick(self):
        self.destroy()
      

    def replay(self):
        self.currentQuestionNumber = 1
        self.indexOfCurrentQuestion = 1
        self.setQuestion()  # Populate text of question
        self.setAnswers()  # Populate text of answer radiobuttons
        self.results.set('')
        storedanswers = []
        self.submitButton.config(text='Submit', command=self.onSubmitButtonClick)

class Professor(Tk):
    def __init__ (self,image):
        Tk.__init__(self,image)
        self.title('Congratulations! Here is your CS professor buddy!')
        pic = PhotoImage(file=image)
        imageLabel = Label(self, image=pic,borderwidth=0)
        imageLabel.pic = pic
        imageLabel.grid(row=0,column=0)

def runAnswer(picture): 
    app = Professor(picture)
    app.mainloop()
        
        
app = CSProfApp()
app.mainloop()

