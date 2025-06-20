# Blackjack
This is a complete implementation of the classic Blackjack (21) card game built with Python and Tkinter. The game features a graphical user interface with realistic card dealing, scoring, and game mechanics. It includes all standard Blackjack rules plus special features like splitting pairs.

The game runs in a resizable window that adapts to different screen sizes while maintaining proper text formatting and layout. The elegant interface includes card suit symbols (♣♦♥♠) and a customizable background image.

Features

Complete Blackjack Implementation: All standard rules including hitting, standing, splitting, and automatic dealer play
Visual Card Display: Shows cards with proper suit symbols and formatting
Score Tracking: Keeps track of wins, losses, and draws
Split Hand Functionality: Allows splitting pairs into separate hands
Responsive Design: Adapts to different screen sizes
Customizable Appearance: Change fonts, colors, and background image
Proper Card Counting: Handles Ace as 1 or 11 automatically
Game State Management: Tracks all game variables and enforces rules
Installation

Prerequisites:
Python 3.6 or higher
PIL/Pillow library (pip install pillow)
Run the game:
bash
python blackjack.py
Customize:
Replace the background image by editing the path in the code
Adjust colors and fonts in the colors and fonts dictionaries
How to Play

Start a new game by clicking "New Game"
You'll be dealt two cards automatically
Choose to:
Hit: Take another card
Stand: Keep your current hand
Split: If you have a pair, split them into two separate hands
The dealer will automatically play after you stand
Win by:
Having a higher score than the dealer without busting (going over 21)
The dealer busting
Getting Blackjack (Ace + 10-value card)
Game Rules

Standard Blackjack rules apply
Dealer must hit on 16 or below, stand on 17 or above
Aces count as 11 unless that would cause a bust, then as 1
Face cards (Jack, Queen, King) count as 10
You can split any pair into two separate hands
Blackjack pays 3:2 (not currently implemented in scoring)
Push (tie) returns your bet
Technical Details

Built With:
Python 3
Tkinter for GUI
PIL/Pillow for image handling
Key Components:
Card deck representation using tuples (suit, value)
Game state management with global variables
Text wrapping and formatting for card displays
Responsive layout using grid and pack geometry managers
Files:
blackjack.py: Main game file (contains all code)
background.jpg: Background image (can be replaced)
