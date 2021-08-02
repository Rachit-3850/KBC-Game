from questions import QUESTIONS
import sys


def isanswercorrect(question,answer):
    return True if question["answer"]==answer else False

def lifeLine(ques):
    correctoption=ques["answer"]
    optiontodelete1=0
    optiontodelete2=0
    if correctoption==1:
        optiontodelete1="option3"
        optiontodelete2="option4"

    elif (correctoption==2):
        optiontodelete1="option4"
        optiontodelete2="option3"
    elif (correctoption==3):
        optiontodelete1="option1"
        optiontodelete2="option2"
    elif correctoption==4:
        optiontodelete1="option1"
        optiontodelete2="option2"
    del ques[optiontodelete1]
    del ques[optiontodelete2]

    return ques


def kbc():


    prizewon=0
    roundno=0
    lifeline=1
    wronganswer=False
    print("welcome to kbc...")
    print("choose any option given below ")
    print("1 : start game")
    print("2: quit game")

    userchoice=int(input().strip())

    if userchoice==2:
        sys.exit(0)

    while (roundno<=14):
        print("\n\t\t lifeline remains {}\n".format(lifeline))
        print(f'\t\tQuestions {roundno +1}: {QUESTIONS[roundno]["name"]}')
        print(f'\t\t\t\toption 1:{QUESTIONS[roundno]["option1"]}')
        print(f'\t\t\t\toption 2:{QUESTIONS[roundno]["option2"]}')
        print(f'\t\t\t\toption 3:{QUESTIONS[roundno]["option3"]}')
        print(f'\t\t\t\toption 4:{QUESTIONS[roundno]["option4"]}')

        ans=input("\n\nYour choice ( 1-4 ) or Enter lifeline to use lifeline or Enter quit to Quit the game:")
        if ans.lower()=="quit":
            break
        elif (ans.lower=="lifeline" and roundno==14):
            print(" u cannot use lifeline on last question")
            ans=input("\n\n Your choice ( 1-4 ) or Enter lifeline to use lifeline or Enter quit to Quit the game:")
        elif (ans.lower=="lifeline" and lifeline==0):
            print("you do not have any lifeline ")
        elif (ans.lower=="lifeline" and lifeline==1):
            q=lifeLine(QUESTIONS[roundno])
            print(f'\tQuestion {roundno + 1}: {q["name"]}')
            print(f'\t\tOptions:')

            if (q["answer"]==1 or q["answer"]==2):
                print(f'\t\t\t option1 :{q["option1"]}')
                print(f'\t\t\t option2 :{q["option2"]}')
            elif (q["answer"]==3 or q["answer"]==4):
                print(f'\t\t\t option1 :{q["option3"]}')
                print(f'\t\t\t option2 :{q["option4"]}')

            lifeline-=1
            ans=input("your choice (1 or 2)")

        elif (ans not in ["1","2","3","4"]):
            print("please choose a correct option")
            ans=input("your choice (1-4)")




        if isanswercorrect(QUESTIONS[roundno],int(ans)):
            print("\n\t\t\tcorrect answer")
            prizewon=QUESTIONS[roundno]["money"]
            print("\t\t\t money win till now : {}".format(prizewon))
        else :
            print('\n\nIncorrect !')
            print("THe Right Answer Was {}".format(QUESTIONS[roundno]["answer"]))
            wronganswer = True
            break
        roundno+=1
    if (not wronganswer):
        print("you won total amount:{}".format(prizewon))

    else :
        if roundno +1<5:
            print("you won : {}".format("0 rs"))
        elif (roundno +1 >=5) and (roundno+1<11):
            print("you won : {}".format("10,000 rs"))
        elif (roundno+1>=11):
            print("you won:{}".format("3,20,000 rs"))
kbc()