import getpass, sys #importing libraries

def question_with_response(prompt): #defining the function 'question_with_response'
    print("Question: " + prompt) #prints "Question:" + prompt as defined by each question in 'rsp ='
    msg = input() #user input is being defined as the string 'msg'
    return msg

questions = 6 #assigning a value of 3 to the 'questions' variable
correct = 0 #assigning a value of 0 to the 'questions' variable

print('Hello, ' + getpass.getuser() + " running " + sys.executable) #printing the appropriate text before the quiz starts
print("You will be asked " + str(questions) + " questions.")
print("Are you ready to take a test?")

rsp = question_with_response("What command is used to include other functions that were previously developed?") #calling the 'question_with_response' function
if rsp == "import": #if the input from the user is 'import'
    print(rsp + " is correct!")
    correct += 1 #increases variable 'correct' by 1 (useful for calculating final score)
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What command is used to evaluate correct or incorrect response in this example?") #question 2
if rsp == "if":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("Each 'if' command contains an '_________' to determine a true or false condition?") #question 3
if rsp == "expression":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")
    
rsp = question_with_response("What command/statement is used to print text in Python?")
if rsp == "print":
    print(rsp + "is correct!")
    correct += 1
else:
    print(rsp + "is incorrect!")

rsp = question_with_response("What is it called when a program enables the user to change the input, thus changing the output on every attempt?")
if rsp == "dynamic":
    print(rsp + "is correct!")
    correct += 1
else:
    print(rsp + "is incorrect!")
    
rsp = question_with_response("What is text that does does not change called?")
if rsp == "static":
    print(rsp + "is correct!")
    correct += 1
else: 
    print(rsp + "is incorrect!")

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))
