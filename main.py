import random

print('''

█▀▄▀█ █▀█ █░█ █ █▀▀   █▀▀ █░█ █▀▀ █▀ █▀ █ █▄░█ █▀▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀
█░▀░█ █▄█ ▀▄▀ █ ██▄   █▄█ █▄█ ██▄ ▄█ ▄█ █ █░▀█ █▄█   █▄█ █▀█ █░▀░█ ██▄

''')

Movies=["Dune","Eternals","Venom","spider-man no way home","No time to die","Black panther","Free guy","Jungle cruise","Old","Cruella","Nobody","The suicde squad","The resident evil","Dolittle","The batman","Tenet","The tomorrow war","Mortal kombat","Cinderella","Men in black","Wonder woman","Oblivion","Red notice","The lion king","Blood shot"]


movie_chosen=random.choice(Movies).lower()
ch=''
for i in movie_chosen:
    if i.isalpha():
        ch+='_'
    else:
        ch+=' '
ch=movie_chosen[0]+ch[1:-1]+movie_chosen[-1]

print(" ".join(ch))
print()

#This function is used if the user wants to guess the entire movie name
def direct(movie_chosen):
    user_guess=input('Enter movie name : ')
    if movie_chosen==user_guess.lower():
        print('yay!, You got it right 🎉')
    else:
        print('Sorry, you got it wrong 😢')

#This function is used if the user wants to guess the movie name letter by letter
def letters(ch):
    while movie_chosen!= ch:
        user_guess=input('Enter your guess : ').lower()
        if user_guess in movie_chosen:
            for i in range(len(movie_chosen)):
                if movie_chosen[i]==user_guess:
                    ch=ch[0:i]+movie_chosen[i]+ch[i+1:]
            print(' '.join(ch))
            print('You got it right ,Keep going! 🔥')
        else:
            print(f"'{user_guess}' is not in the movie name 😢")

#This is the main function
def main():
    option='y'
    while option=='y':
        movie_chosen=random.choice(Movies)
        print('1. Guess the entire movie name')
        print('2. Guess the movie name letter by letter')
        print('3. Exit')
        print()
        e=int(input('Choose your option : '))
        print()
        if e==1:
            direct(movie_chosen)
        elif e==2:
            letters(ch)
        elif e==3:
            print('Have a nice day! 😄')
            break
        else:
            print('Invalid choice ❌')
        option=input('again? 🤔 (y/n) : ')
main()

            
        
    

