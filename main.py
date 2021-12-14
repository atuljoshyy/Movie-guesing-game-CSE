import random

movie_list = ["Dune","Eternals","Venom","spider-man no way home","No time to die","Black panther","Free guy","Jungle cruise","Old","Cruella","Nobody","The suicde squad","The resident evil","Dolittle","The batman","Tenet","The tomorrow war","Mortal kombat","Cinderella","Men in black","Wonder woman 1984","Oblivion","Red notice","The lion king","Blood shot"]


movie_chosen = random.choice(movie_list).lower()
used = []


display = movie_chosen
for i in range (len(display)):

  display = display[0:i]  + "_" + display[i+1:]

  


movie_display = " ".join(display)

print (movie_chosen[0]+movie_display[1:-1]+movie_chosen[-1])


attempts = 0


while display != movie_chosen:
  guess = input("Please enter a letter: ")
  guess = guess.lower()
  used.extend(guess)
  print ("Attempts: ")
  print (attempts)
  

  for i in range(len(movie_chosen)):
    if movie_chosen[i] == guess:
      display = display[0:i] + guess + display[i+1:]

  print("Used letters: ")
  print(used)
      


  movie_display = " ".join(display)
  print (movie_chosen[0]+movie_display[1:-1]+movie_chosen[-1])
  attempts = attempts + 1
  
print("Well done, you guessed the correct movie " + str(attempts) + " attempts")
