# CarmenSandiegoGame
# This program is a basic version of the game "Where in the World is Carmen Sandiego?" which gets the user's name and asks the user to guess a location based on a clue, giving 4
# answer choices for each question. The user has the option to quit the game after answering each question. Once the user gets a total of 5 correct or incorrect guesses, the game
# ends, printing the result as well as the user's score. The score starts at 5, with 1 point being added for every correct answer, and 1 point being deducted for every incorrect 
# answer (5 incorrect answers with 0 correct answers gets you the lowest score of 0, and 5 correct answers with 0 incorrect answers gets you the highest score of 100). The program
# then compares the user's score to the scores in the lists that compose the high scores dataframe, replacing the name and score of the lowest score if it is higher. When the user 
# returns to the main menu, the high scores will be updated to include their score if warranted, and the dataframe is sorted by highest score before being printed. The main menu
# consists of the welcome screen, the high scores dataframe, and the options to start a new game or quit. This screen wil always be displayed when the program starts as well as after 
# the completion of each game, provided the user doesn't quit.
