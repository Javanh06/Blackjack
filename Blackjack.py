from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Blackjack")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Font and color scheme
fonts = {
    'title': ('Arial Rounded MT Bold', 24),
    'header': ('Verdana', 14, 'bold'),
    'body': ('Segoe UI', 12),
    'button': ('Tahoma', 12, 'bold'),
    'result': ('Comic Sans MS', 36, 'bold'),
    'cards': ('Courier New', 12)
}

colors = {
    'green': '#50C878',
    'red': '#FF6B6B',
    'blue': '#6495ED',
    'white': '#FFFFFF',
    'black': '#000000'
}

# Load background image
image = Image.open("/Users/javanwizeye/Documents/Exceptional pictures/background.jpg")
resized_image = image.resize((screen_width, screen_height), Image.LANCZOS)
background_image = ImageTk.PhotoImage(resized_image)
bgLabel = Label(root, image=background_image)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

# Game setup
def newGame():
    for i in range(4):
        for j in range(1,14):
            cards.append((i,j))

suit = {0:"♣ Clubs", 1:"♦ Diamonds", 2:"♥ Hearts", 3:"♠ Spades"}
number = {1:"Ace", 11:"Jack", 12:"Queen", 13:"King"}

cards = []
newGame()
total = dTotal = previous = wins = draws = losses = hand2Total = count = 0
handString = dHandString = hand2String = ""
finalTotal = 0
canSplit = False

mainFrame = Frame(root, bg=colors['white'], width=min(screen_width-100, 1000), 
                 height=min(screen_height-100, 800))
mainFrame.place(relx=0.5, rely=0.5, anchor='center')
mainFrame.pack_propagate(False)

playerFrame = Frame(mainFrame, bg=colors['white'])
playerFrame.grid(row=0, column=0, padx=20, pady=10, sticky='nsew')

scoreLabel = Label(playerFrame, text="Score: 0", bg=colors['white'], font=fonts['header'])
scoreLabel.pack(anchor='w')

hand = Label(playerFrame, text="Your hand: ", bg=colors['white'], font=fonts['cards'],
            wraplength=300, justify='left', anchor='w')
hand.pack(anchor='w', fill='x')

score2Label = Label(playerFrame, text="", bg=colors['white'], font=fonts['body'])
score2Label.pack(anchor='w')

hand2 = Label(playerFrame, text="", bg=colors['white'], font=fonts['cards'],
             wraplength=300, justify='left', anchor='w')
hand2.pack(anchor='w', fill='x')

dealerFrame = Frame(mainFrame, bg=colors['white'])
dealerFrame.grid(row=0, column=2, padx=20, pady=10, sticky='nsew')

dealerScoreLabel = Label(dealerFrame, text="Dealer's score: 0", bg=colors['white'], font=fonts['header'])
dealerScoreLabel.pack(anchor='w')

dHand = Label(dealerFrame, text="Dealer's hand: ", bg=colors['white'], font=fonts['cards'],
             wraplength=300, justify='left', anchor='w')
dHand.pack(anchor='w', fill='x')

statusFrame = Frame(mainFrame, bg=colors['white'])
statusFrame.grid(row=0, column=1, padx=20, pady=10, sticky='nsew')

statsContainer = Frame(statusFrame, bg=colors['white'])
statsContainer.pack()

winLabel = Label(statsContainer, text="Wins: 0", bg=colors['white'], font=fonts['body'])
winLabel.grid(row=0, column=0, padx=5)

drawLabel = Label(statsContainer, text="Draws: 0", bg=colors['white'], font=fonts['body'])
drawLabel.grid(row=0, column=1, padx=5)

lossLabel = Label(statsContainer, text="Losses: 0", bg=colors['white'], font=fonts['body'])
lossLabel.grid(row=0, column=2, padx=5)

label = Label(statusFrame, text="", font=fonts['result'], fg=colors['black'], bg=colors['white'],
             wraplength=400, justify='center')
label.pack(pady=10)

buttonFrame = Frame(mainFrame, bg=colors['white'])
buttonFrame.grid(row=1, column=0, columnspan=3, pady=20)

def hit():
    global total, handString, hand2Total, losses, count
    if not cards: newGame()
    x = random.choice(cards)
    cards.remove(x)
    
    if x[1]==1 and total<11: total+=11
    elif x[1]>10: total+=10
    else: total+=x[1]
    
    scoreLabel.config(text=f"Score: {total}")
    
    if hand2Total!=0 and count==0:
        handString += " "
    
    # Add newline if line is getting too long
    if len(handString) > 60:  # Approximately 60 characters per line
        handString += "\n"
    
    if x[1]==1 or x[1]>10:
        handString += number.get(x[1], str(x[1])) + " of " + suit[x[0]] + ", "
    else:
        handString += str(x[1]) + " of " + suit[x[0]] + ", "
    
    hand.config(text=f"Your hand: {handString}")
    
    if total>21 and (hand2Total==0 or hand2Total>21):
        label.config(text="You lose!", fg=colors['red'])
        losses += 1
        lossLabel.config(text=f"Losses: {losses}")
        hitButton.config(state="disabled")
        hit2Button.config(state="disabled")
        splitButton.config(state="disabled")

def preHit():
    global total, handString, previous, canSplit
    x=random.choice(cards)
    cards.remove(x)

    if x[1]==1 and total<11:
        total+=11
    elif x[1]>10:
        total+=10
    else:
        total+=x[1]

    previous = x 

    if x[1]==1 or x[1]>10:
        handString += number.get(x[1], str(x[1])) + " of " + suit[x[0]] + ", "
    else:
        handString+=str(x[1])+" of "+suit[x[0]]+", "

    hand.config(text=f"Your hand: {handString}")
    scoreLabel.config(text=f"Score: {total}")
    
    x=random.choice(cards)
    cards.remove(x)
    if previous[1]==x[1]:
        canSplit=True
        splitButton.config(state="normal")
    else:
        canSplit=False
        splitButton.config(state="disabled")

    if x[1]==1 and total<11:
        total+=11
    elif x[1]>10:
        total+=10
    else:
        total+=x[1]
        
    if x[1]==1 or x[1]>10:
        handString+=number.get(x[1], str(x[1]))+" of "+suit[x[0]]+", "
    else:
        handString+=str(x[1])+" of "+suit[x[0]]+", "
    hand.config(text=f"Your hand: {handString}")
    scoreLabel.config(text=f"Score: {total}")
    
    if total==21:
        label.config(text="Blackjack!", fg=colors['green']) 

def split():
    global total, handString, hand2Total, hand2String, canSplit
    if not canSplit: return

    cardsInHand=handString.split(", ")
    firstCard=cardsInHand[0]
    secondCard=cardsInHand[1]

    total=0
    handString= firstCard
    hand2String=secondCard
    cardValue=previous[1]
    if cardValue==1:
        total=11
    elif cardValue>10:
        total=10
    else:
        total=cardValue
    if previous[1] == 1:
        hand2Total=11
    elif previous[1]>10:
        hand2Total=10
    else:
        hand2Total=previous[1]
    
    hand.config(text=f"Your hand: {handString}")
    scoreLabel.config(text=f"Score: {total}")
    hand2.config(text=f"Second hand: {hand2String}")
    score2Label.config(text=f"Second score: {hand2Total}")
    hit2Button.config(state="normal")
    splitButton.config(state="disabled")
    canSplit=False

def hit2():
    global hand2String, hand2Total, losses
    if not cards: newGame()
    x=random.choice(cards)
    cards.remove(x)
    if x[1]==1 and hand2Total<11:
        hand2Total+=11
    elif x[1]>10:
        hand2Total+=10
    else:
        hand2Total+=x[1]
    score2Label.config(text=f"Second score: {hand2Total}")
    hand2String+=", "
    if x[1]==1 or x[1]>10:
        hand2String+=number.get(x[1], str(x[1]))+" of "+suit[x[0]]+", "
    else:
        hand2String+=str(x[1])+" of "+suit[x[0]]+", "
    hand2.config(text=f"Second hand: {hand2String}")
    if hand2Total>21:
        if total>21:
            label.config(text="Both hands bust! You lose!", fg=colors['red'])
            losses+=1
            lossLabel.config(text=f"Losses: {losses}")
            hitButton.config(state="disabled")
            hit2Button.config(state="disabled")

def dealer():
    global dTotal, total, dHandString, hand2Total, wins, draws, losses
    hitButton.config(state="disabled")
    hit2Button.config(state="disabled")
    splitButton.config(state="disabled")
    while dTotal<=17:
        if not cards: newGame()
        x=random.choice(cards)
        cards.remove(x)
        if x[1]==1 and dTotal<11:
            dTotal+=11
        elif x[1]>10:
            dTotal+=10
        else:
            dTotal+=x[1]
        dealerScoreLabel.config(text=f"Dealer's score: {dTotal}")
        if x[1]==1 or x[1]>10:
            dHandString+=number.get(x[1], str(x[1]))+" of "+suit[x[0]]+", "
        else:
            dHandString+=str(x[1])+" of "+suit[x[0]]+", "
        dHand.config(text=f"Dealer's hand: {dHandString}")
    finalTotal=total
    if hand2Total>0 and hand2Total<=21:
        finalTotal=max(total, hand2Total) if total<=21 else hand2Total
    elif total>21: finalTotal=0
    
    if dTotal>21:
        label.config(text="Dealer busts! You win!", fg=colors['green'])
        wins+=1
    elif finalTotal>dTotal and finalTotal<= 21:
        label.config(text="You win!", fg=colors['green'])
        wins+=1
    elif finalTotal==dTotal:
        label.config(text="Push (Draw)!", fg=colors['blue']) 
        draws+=1
    else:
        label.config(text="You lose!", fg=colors['red'])
        losses+=1
    winLabel.config(text=f"Wins: {wins}")
    drawLabel.config(text=f"Draws: {draws}")
    lossLabel.config(text=f"Losses: {losses}")

def restart():
    global total, dTotal,cards,handString,dHandString,hand2Total,hand2String, canSplit, count
    hand2Total=0
    total=0
    dTotal=0
    count=0
    cards=[]
    newGame()
    handString=""
    dHandString=""
    hand2String=""
    canSplit=False
    scoreLabel.config(text="Score: 0")
    dealerScoreLabel.config(text="Dealer's score: 0")
    label.config(text="")
    score2Label.config(text="")
    hand.config(text="Your hand: ")
    dHand.config(text="Dealer's hand: ")
    hand2.config(text="")
    hitButton.config(state="normal")
    hit2Button.config(state="disabled")
    splitButton.config(state="disabled")
    preHit()
    x=random.choice(cards)
    cards.remove(x)
    if x[1]==1:
        dTotal+=11
    elif x[1]>10:
        dTotal+=10
    else:
        dTotal+=x[1]
    dealerScoreLabel.config(text=f"Dealer's score: {dTotal}")
    if x[1]==1 or x[1]>10:
        dHandString+=number.get(x[1], str(x[1]))+ " of "+ suit[x[0]]+", "
    else:
        dHandString+=str(x[1])+" of "+suit[x[0]]+", "
    dHand.config(text=f"Dealer's hand: {dHandString}")
hitButton = Button(buttonFrame, text="Hit", command=hit, font=fonts['button'])
hitButton.grid(row=0, column=0, padx=5)
hit2Button = Button(buttonFrame, text="Hit 2nd Hand", command=hit2, state="disabled", font=fonts['button'])
hit2Button.grid(row=0, column=1, padx=5)
splitButton = Button(buttonFrame, text="Split", command=split, state="disabled", font=fonts['button'])
splitButton.grid(row=0, column=2, padx=5)
dealerButton = Button(buttonFrame, text="Stand", command=dealer, font=fonts['button'])
dealerButton.grid(row=0, column=3, padx=5)
restartButton = Button(buttonFrame, text="New Game", command=restart, font=fonts['button'])
restartButton.grid(row=0, column=4, padx=5)
restart()
root.mainloop()