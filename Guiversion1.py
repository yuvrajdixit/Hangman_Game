from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random


window = Tk()
window.title('Hangman-GUESS CITIES NAME')
word_list= ['MUMBAI','DELHI','BANGLORE','HYDRABAD','AHMEDABAD','CHENNAI','KOLKATA','SURAT','PUNE','JAIPUR','AMRITSAR','ALLAHABAD','RANCHI',
            'LUCKNOW','KANPUR','NAGPUR','INDORE','THANE','BHOPAL','PATNA','GHAZIABAD','AGRA','FARIDABAD','MEERUT','RAJKOT','VARANASI','SRINAGAR',
            'RAIPUR','KOTA','JHANSI']
            
photos = [PhotoImage(file="C:\hangman game\hang0.png"), PhotoImage(file="C:\hangman game\hang1.png"), PhotoImage(file="C:\hangman game\hang2.png"),
PhotoImage(file="C:\hangman game\hang3.png"), PhotoImage(file="C:\hangman game\hang4.png"), PhotoImage(file="C:\hangman game\hang5.png"),
PhotoImage(file="C:\hangman game\hang6.png"), PhotoImage(file="C:\hangman game\hang7.png"), PhotoImage(file="C:\hangman game\hang8.png"),
PhotoImage(file="C:\hangman game\hang9.png"), PhotoImage(file="C:\hangman game\hang10.png"), PhotoImage(file="C:\hangman game\hang11.png")]






def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses =0
    
    the_word=random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(' '.join("_"*len(the_word)))

def guess(letter):
	global numberOfGuesses
	if numberOfGuesses<11:	
		txt = list(the_word_withSpaces)
		guessed = list(lblWord.get())
		if the_word_withSpaces.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]==letter:
					guessed[c]=letter
				lblWord.set("".join(guessed))
				if lblWord.get()==the_word_withSpaces:
					messagebox.showinfo("Hangman","You guessed it!")
		else:
			numberOfGuesses += 1
			imgLabel.config(image=photos[numberOfGuesses])
			if numberOfGuesses==11:
					messagebox.showwarning("Hangman","Game Over")


imgLabel=Label(window) 
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)



lblWord = StringVar()
Label(window, textvariable  =lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=('Helvetica 18'), width=4).grid(row=1+n//9,column=n%9)
    n+=1

Button(window, text="New\nGame", command=lambda:newGame(), font=("Helvetica 10 bold")).grid(row=3, column=8)

newGame()
window.mainloop()
