import pandas as pd
import random

destinations = {
    1 : ("Buenos Aires, Argentina",'Carmen is in the second largest country in South America, in a city with a name that means "fair winds" in Spanish.'),
    2 : ("Rio de Janeiro, Brazil","Carmen is in a city known for the Christ the Redeemer statue, in the largest country in South America, and the only country in the Americas with Portuguese as its official language."),
    3 : ("Sydney, Australia","Carmen is in a city well known for its Opera House, in the only country that is also a continent."),
    4 : ("Port Moresby, Papua New Guinea","Carmen is in the capital and largest city of the world's third largest island country. Its only land border is Indonesia to the west."),
    5 : ("Montreal, Canada","Carmen is in a city named after Mount Royal, around which the early settlement was built. It is in the second largest country with the world's longest coastline"),
    6 : ("New York, United States","Carmen is in the world's third largest country, which is also the third most populous country. She is in a city known as a global center of finance, with one of the trademark locations being Wall St."),
    7 : ("Cairo, Egypt","Carmen is in the capital of a country at the northeast corner of Africa, a city known for its proximity to the Pyramids of Giza and the Nile Delta."),
    8 : ("Bamako, Mali","Carmen is in the capital of a West African country containing the Sahara desert in the north, and the Sudanian savanna in the south. Mansa Musa, thought to be the wealthiest person in history, once ruled an empire bearing the same name as this country."),
    9 : ("Paris, France","Carmen is in a city known for the Eiffel Tower, the capital and largest city of a West European country."),
    10 : ("Rome, Italy","Carmen is in a city known for the Colosseum, the capital of a Western European country with the Alps on its northern border. This city also contains Vatican City, the smallest country in the world, within its borders."),
    11 : ("Beijing, China","Carmen is in the world's most populous national capital, a global center of finance that is home to the 4 largest financial institutions in the world. This Asian country is the second most populous country in the world."),
    12 : ("Tokyo, Japan","Carmen is in the capital of an island country off the northeast coast of the Asian mainland. This country sits on the Pacific Ring of Fire and is vulnerable to earthquakes."),
    13 : ("New Delhi, India","Carmen is in the capital of the world's most populous country, a country located in South Asia and known for the Taj Mahal."),
    14 : ("London, United Kingdom","Carmen is in the capital of both the country and the greater union of 4 countries- a set of islands off the west coast of continental Europe. The city is known for the clock tower Big Ben."),
    15 : ("Oslo, Norway","Carmen is in a city founded at the end of the Viking Age, the capital and largest city of a Nordic country that borders Sweden, Finland, and Russia.")
}
player_names = ["Player Name","Player Name","Player Name"]
player_scores = [2,1,0]


def main_menu():
    correct_guesses = 0
    incorrect_guesses = 0
    sentinel = ""

    high_scores_data = {
    "Name" : player_names,
    "Score" : player_scores }
    high_scores = pd.DataFrame(high_scores_data)
    sorted_scores = high_scores.sort_values(by=['Score'],ascending=False)

    print("\nWHERE IN THE WORLD IS CARMEN SANDIEGO?\n")
    print("Welcome!\n")
    print("HIGH SCORES")
    print(sorted_scores.to_string(index=False))
    print("\nOptions:")
    print("1. New Game")
    print("2. Quit")
    menu_choice = input("Select 1 or 2: ")

    if menu_choice == '1':
        print("STARTING NEW GAME")
        name = input("What is your name? ")
        print(f"""
***BEGIN TRANSMISSION***

Dear Agent {name},
Carmen Sandiego has stolen Duke’s helmet, and you need to help track her down using clues about possible destinations she has absconded to with it.
You have five days to catch up with her before she gets away. Each day you will be given one clue as to where Carmen is.
The hunt ends when you locate or fail to locate Carmen for 5 days.

-Camden Jones

***END TRANSMISSION 830.681028***\n""")
        
        input("Enter to continue: ")
        remaining_keys = list(destinations.keys())
        carmen_locations = []
        incorrect_details = []
        clue_number = 1

        while sentinel != "0" and correct_guesses < 5 and incorrect_guesses < 5:

            answer = random.choice(remaining_keys)
            carmen_locations.append(destinations[answer])
            remaining_keys.remove(answer)
            if answer > len(remaining_keys)/2:
                choice1 = answer - 1
                choice2 = answer - 2
                choice3 = answer - 3
            elif answer <= len(remaining_keys)/2:
                choice1 = answer + 1
                choice2 = answer + 2
                choice3 = answer + 3
            answer_choices = [answer, choice1, choice2, choice3]
            random.shuffle(answer_choices)

            print(f"\nCLUE {clue_number}: {destinations[answer][1]}")
            clue_number += 1
            print("CHOICES:")
            iterable = 1
            answer_number = answer_choices.index(answer)
            for i in answer_choices:
                print(f"{iterable}. {destinations[i][0]}")
                iterable += 1
            user_guess = int(input("Where is Carmen now?(Select one of the number choices): "))-1
            user_answer_number = answer_choices[user_guess]
            if user_guess == answer_number:
                correct_guesses += 1
                print("\nYou located Carmen for today!\n")
            else:
                incorrect_guesses += 1
                incorrect_details.append(destinations[user_answer_number])
                print("\nYou failed to locate Carmen for today!\n")

            sentinel = input("Press Enter to continue (Enter 0 to quit): ")
        if incorrect_guesses == 5:
            print("\nOh no! Carmen Sandiego got away with Duke's helmet!\n")
        elif correct_guesses == 5:
            print("\nWell done! You caught Carmen Sandiego!\n")
        elif sentinel == '0':
            print("\nYou let Carmen Sandiego escape!\n")
        if sentinel != '0':
            score = 5 + correct_guesses - incorrect_guesses
            print(f"Your final score: {score}\nCorrect Guesses: {correct_guesses}\nIncorrect Guesses: {incorrect_guesses}\n")
            min_spot = player_scores.index(min(player_scores))
            if score > min(player_scores):
                player_scores[min_spot] = score
                player_names[min_spot] = name
            sentinel = input("Press Enter to continue to the main menu (Enter 0 to quit): ")
            if sentinel != '0':
                main_menu()
main_menu()
        

            






            

