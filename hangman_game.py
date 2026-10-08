import random
import hangman_stages
import word_list1
#word_list=["apple","mango","banana"]
lives=6
print("Welcome to the Hangman Game!")
print("you have only 6 lives 🤯🤯🤯 Good luck👍 ")
chosen_word=random.choice(word_list1.words)
#print(chosen_word)
display=[]
for i in range(len(chosen_word)): #apple len=5
    display+='_'    #'_','_','_','_','_'
print(display)
game_over=False     #game khatam nhi hua
while not game_over:
    guessed_letter=input("Guess a letter: ").lower()  #user guess kare
    for position in range(len(chosen_word)):   #apple len=5 range(5)
        letter=chosen_word[position]    # apple->> position[0,1,2,3,4]
        if letter==guessed_letter:      #a==a (true) or a==y (false)
            display[position]=guessed_letter #display['_','_','_','_','_']=guess later
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            print("you lose")
    if '_' not in display:
        game_over=True
        print("you win")
    print(hangman_stages.stages[lives])




