# stephen gaydash
# do not change unless you know what you are doing!
import time
print('Hello! Welcome to my database of python basics!')
time.sleep(3)
print('You will be a ble to pick a topic to review from a list!')
time.sleep(1)
def start():
    begin = input('Would you like to begin? (Yes or No)')
    if begin == 'Yes' or begin == "yes":
        print('Here is your list of topics to choose from:')
        print('////////////////')
        print('1 = Getting Started (Hello World!)')
        print('2 = Math Operators')
        print('3 = Variables')
        print('4 = Loops!')
        print('5 = Logic')
        print('////////////////')
        choose = input('Which topic would you like to learn about? (Type the number of a topic)')
        if choose == 1:
            print('Good choice! Always start at the basics.')
            time.sleep(2)
            print('When you think about it, programming is actually easy to start learning. The only goal should be to get output from your program.')
            print('One of the easiest ways to do this is with the Hello World approach.')
            print('The goal of this exercise is to get your computer to output the statement "Hello World!"')
            time.sleep(2)
            print('The easiest way to do this is using pythons built in "print" command')
            print('typing this into IDLE - print("Hello World!", will yeild this result:')
            time.sleep(3)
            print()
            print()
            print('Hello World!')
            print()
            print()
            print('See,')
            time.sleep(2)
            print('Easy peasy.')

            def tryworld():

                print('Now it is your turn! try typing the command to yield the previous output!')
                testworld = input('Type the command now:')
                if testworld == ('print("Hello World")'):
                    print('SUCCESS')
                    print('You have learned this topic!')
                    print('You will now return to the topic selection.')
                    print('.')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print('.')
                    return begin()
                elif testworld != ('print("Hello World")'):
                    print('Sorry, try again!')
                    tryworld()



