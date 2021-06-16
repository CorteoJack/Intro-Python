from tkinter import*
import random

main =Tk()
main.title("Guess the number!")
main.geometry("420x320")

guess = [0]

def generator():
    guess[0]=random.randint(1,1000)
    print(guess[0])

generator()
def game():
    guess_test=Label(main, text="Guess the number")
    guess_text.place(x=160, y=120)

user_guess_gui = Entry(main) 
user_guess_gui.place(x=150,y=150)


def user():
    root = Tk()         
    root.title("AGAIN?")
    root.geometry("320x240")

    user_guess = int(user_guess_gui.get())

    if user_guess==guess[0]:
        again = Label(root,text="\tYOU WON!!!!!",fg='light green')
        again.place(x=90,y=45)

        again = Label(root,text="Would you like to play again?")
        again.place(x=90,y=85)

        def greeting():
            greet = Label(root,text="Thank You for Playing.")
            greet.place(x=100,y=160)
            root.withdraw()
            main.withdraw()

        def yes():
            generator()
            yes_but = Button(root,text="YES?",command=game)
            yes_but.place(x=90,y=120)

        def no():
            no_but = Button(root,text="NO?",command=greeting)
            no_but.place(x=200,y=120)

        yes()
        no()

    elif user_guess<guess[0]:
        greet = Label(root,text="Too Low.Try again")
        greet.place(x=100,y=100)
        greet = Label(root,text="Would you like to play again?")
        greet.place(x=85,y=120)
        game()

        def yes():
            generator()
            yes_but = Button(root,text="YES?",command=game)
            yes_but.place(x=90,y=120)

        def no():
            no_but = Button(root,text="NO?",command=greeting)
            no_but.place(x=200,y=120)

            yes()
            no()

    elif user_guess>guess[0]:
        greet = Label(root,text="Too High.Try again")
        greet.place(x=100,y=100)
        game()


submit = Button(main,text="CHECK",command=user)
submit.place(x=180,y=175)
