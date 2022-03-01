# UW-Work-Sample
This is a work sample for UW CLMS. 

The purpose of this program is to provide possible solutions for Wordle.
Users can enter known letters and positions, known letters with unknown positions, and known wrong letters to generate a list of possible solutions. 

## Getting Started
1. Clone this repo
2. Open a terminal
3. Run the following: 
```
$ python WordleSolutions.py
```

## Using the Wordle Solution
When you run WordleSolutions.py, you will see a prompt like this: 
```
Enter letters using the following format: 
????? (known letters and position), ????? (known letters but unknown position), abc (wrong letters). 
For example: f??e?, ?s???, pln
Enter letters:
```

To properly generate a solution, enter letters with known positions, known letters with unknown positions, and unknown letters. Separate each of the three groups by a comma. For those familiar with Wordle, the first group is green letters, the second group is yellow letters, and the last group are grey letters. For example, if I have guessed the word "faces" and, based on this guess, learned that "f" and "a" are in the right position, "c" and "e" are in the word, but not in that position, and "s" is not in the word at all, I would answer the prompt as follows:
```
fa???, ??ce?, s
```

