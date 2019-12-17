# stephen gaydash
# do not change unless you know what you are doing!
import time
print('WARNING: this program makes use of the "time" library to make reading the content easier. Expect small delays in text output.')
time.sleep(3)
print('loading...')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('Hello! Welcome to my database of python basics!')
time.sleep(3)
print('This database will be updated and expanded in the future!')
time.sleep(3)
print('You will be able to pick a topic to review from a list!')
time.sleep(1)
def start():
    begin = input('Would you like to begin? (Yes or No)')
    if begin == 'Yes' or begin == "yes":
        print('Here is your list of topics to choose from:')
        time.sleep(2)
        print('.')
        time.sleep(2)
        print('.')
        time.sleep(2)
        print('////////////////')
        print('1 = Getting Started (Hello World!)')
        print('2 = Math Operators')
        print('3 = Variables')
        print('4 = If/Else')
        print('////////////////')
        time.sleep(3)
        choose = input('Which topic would you like to learn about? (Type the number of a topic)')
        if choose == "1":
            print('Good choice! Always start at the basics.')
            time.sleep(2)
            print('When you think about it, programming is actually easy to start learning. The only goal should be to get output from your program.')
            print('One of the easiest ways to do this is with the Hello World approach.')
            print('The goal of this exercise is to get your computer to output the statement "Hello World!"')
            time.sleep(2)
            print('The easiest way to do this is using pythons built in "print" command')
            print('typing this into IDLE - print("Hello World!"), will yeild this result:')
            time.sleep(3)
            print()
            print()
            print('Hello World!')
            print()
            print()
            time.sleep(2)
            print('See,')
            time.sleep(2)
            print('Easy peasy.')

            def tryworld():

                print('Now it is your turn! try typing the command to yield the previous output!')
                testworld = input('Type the command now:')
                if testworld == ('print("Hello World!")'):
                    print('SUCCESS')
                    print('You have learned this topic!')
                    print('You will now return to the topic selection.')
                    print('.')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print('.')
                    start()
                elif testworld != ('print("Hello World")'):
                    print('Sorry, try again!')
                    tryworld()
            tryworld()
        if choose == "2":
            print('Welcome! This is the Math Operators section.')
            time.sleep(3)
            print('There are several math operators built right into python.')
            time.sleep(2)
            print("First, let's dive into the four main ones.")
            print('+ is Addition')
            print("- is Subtraction")
            print("/ is Division")
            print("* is Multiplication")
            time.sleep(2)
            print("These operators can be used in the print statements you learned in the first module!")
            time.sleep(2)
            print("For example,")
            print("Typing 'print(2 + 2)' will yield:")
            time.sleep(2)
            print('4')
            time.sleep(3)
            print('You can also just type the operator right into the python console!')
            time.sleep(2)
            print('Now it is your turn!')
            time.sleep(2)
            print('Try dividing 21 by 3:')

            def trymultiply():
                answer = input()
                if answer == ('print(21 / 3)') or answer == '21 / 3':
                    print("Correct!")
                    time.sleep(2)
                    print('You have completed the Math Operators section of the course!')
                    start()
                else:
                    print('Sorry, this is incorrect. Try again!')
                    trymultiply()
            trymultiply()

        if choose == "3":
            print('Welcome to the Variables section of this course!')
            time.sleep(2)
            print("Variables are 'containers' that store information, such as input from a user and an integer.")
            time.sleep(2)
            print('For example, if we wanted the word "usefulNumber" to be assigned the value "3",')
            time.sleep(1)
            print("We would type:")
            print("usefulNumber = 3")
            time.sleep(3)
            print("The '=' symbol assigns the word we choose with the value we give.")
            time.sleep(2)
            print("If we were to type the variable name, it would then print us the data stored inside!")
            time.sleep(2)
            print("You try!")
            time.sleep(3)
            print("First, assign the word 'test' with the value '50':")
            def variable():
                testvar = input()
                if testvar == "test = 50":
                    print('Wow! That was perfect.')
                    time.sleep(2)
                    print("Now type your variable into the prompt to see its value:")
                    def variable2():
                        testvar2 = input()
                        if testvar2 == 'test':
                            print('50')
                            time.sleep(3)
                            print("Perfect!")
                            time.sleep(3)
                            print('You have completed the Variables section of this course!')
                            start()
                        else:
                            print('Not quite! Try again:')
                            variable2()
                    variable2()
                else:
                    print('Not quite! Try again:')
                    variable()
            variable()
        if choose == '4':
            def elsetest():
                elsevar = input()
                if elsevar == 'else':
                    print('Correct!')
                    time.sleep(2)
                    print('Congratulations! You have completed this section of the course.')
                    time.sleep(1)
                    print('You will now return to the selection page.')
                    start()
                else:
                    print('Incorrect. Try again:')
                    elsetest()
            print("Hello! This section of the course is all about If/Else operators.")
            time.sleep(2)
            print("If/Else statements are great for accepting data input from the user and running certain code depending")
            time.sleep(0.5)
            print('on that input!')
            time.sleep(2)
            print("For example: You ask (with a print statement) 'print('What is 2 + 2' ")
            time.sleep(2)
            print('Use your knowledge of variables to assign this input to a "testvar" variable:')
            time.sleep(1)
            print('Use: "testvar = inout()"')
            time.sleep(1)
            print('This will assign whatever the user types as the data for the variable "testvar"')
            time.sleep(1)
            print('We can then use the If/Else operators to decide what to do with the users input:')
            time.sleep(2)
            print()
            print()
            print('''
                  'if testvar == "4":
                        print('Correct!')
                  else:
                        print('Wrong')
        
                        ''')
            print()
            print()
            time.sleep(2)
            print(".")
            time.sleep(2)
            print('The two "==" are necessary to the If statement. This allows the statement to compare the expected value with the')
            time.sleep(1)
            print('users input.')
            time.sleep(2)
            print('Now, lets test your knowledge!')
            time.sleep(2)
            print("What sign do you use to compare input to an expected value ( == or * ):")
            def iftest():
                ifvar = input()
                if ifvar == '==':
                    print('Correct!')
                    time.sleep(2)
                    print('Next question,')
                    time.sleep(1)
                    print("What word is used to run code if a value other than the expected value is input by the user:")
                    elsetest()
                else:
                    print('Incorrect. Try again!')
                    iftest()
            iftest()
                         
start()



