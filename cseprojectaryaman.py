import random #random module to select random sentences
import time  #time module to measure typing duration


def calculate_wpm(time_taken, textlength): #function to calculate words per minute
    if time_taken <= 0:
        return 0
    wordstyped = textlength / 5
    wpm = (wordstyped / time_taken) * 60    #convert to minutes
    return round(wpm)

def typing_test():  #main function to run the typing test
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming in Python is fun and easy to learn.",
        "Learning to code opens many new doors.",
        "You say this after someone fails, and you hope they do better next time.",
        "This ship is too big to pass through the canal.",
        "She didn't drink, but she didn't want people to realize that, so she ordered a ginger ale at the bar.",
        "She wanted her grandmother's old bike, but the tires were worn out and she couldn't find a shop that could replace them.",
        "The tree was so old that it was considered a historic monument.",
        "Tom is used to driving a pickup truck, but he's never driven a monster truck.",
        "She broke the pot two hours after she bought it.",
        "The alligator's teeth were so scary that I ran back to the car as fast as I could.",
        "I saw some cool vintage chairs in a thrift store, but I really need to stop buying things.",
        "Hello world is the classic starting program.",
        "The green trees out the window swayed in the wind.",
        "I'm just trying to stop you from making a big mistake.",
        "He liked chocolate and banana milkshakes because his mom used to make them when he was sick.",
        "You are, hands down, the biggest idiot I've ever met.",
        "The chocolate chip cookies smelled so good that I ate one without asking.",
        "Always remember to comment your code clearly.",
    ]
    targettext = random.choice(sentences)   #select a random sentence
    print("**" * 75)
    print("TYPING SPEED TEST")
    print("**" * 75)
    print("Type the following phrase exactly as it appears:")
    print("-" * 75)
    print(f"\n\n>>>>> {targettext}<<<< \n\n")
    print("-" * 75)
    start_time = time.time()
    u_input = input("Type the above phrase here : ")  #get user input
    end_time = time.time()
    total_time = end_time - start_time  #calculate time taken
    if u_input.strip() == targettext.strip():
        wpm = calculate_wpm(total_time, len(targettext))   #calculate WPM
        print("\n" + "*" * 50)
        print("CONGRATULATIONS! Your answer is correct.")
        print(f"Your typing speed is: {wpm} words per minute (WPM)")
        print(f"Time taken: {total_time:.1f} seconds")
        print("#" * 50)
    else:
        print("\n" + "!" * 50)
        print("SORRY! Your answer is incorrect.")  #notify user of incorrect input
        print("Please try again for accurate WPM.")
        print(f"Time taken: {total_time:.1f} seconds")
        print(f"Provided Entry:{targettext}")
        print(f"Your Entry:{u_input}")   #show user input vs target text
        print("\nDifferences:")
        targetwords=targettext.strip().split()  #split target text into words
        u_words=u_input.strip().split()  #split user input into words
        for i in range(len(targetwords)):
            if i < len(u_words):
                if targetwords[i] != u_words[i]:
                    print(f"Mismatch at character {i+1}: expected '{targetwords[i]}', got '{u_words[i]}'")
            else:
                print(f"Mismatch at character {i+1}: expected '{targetwords[i]}', got 'No character'")
        
        print("!" * 50)

if __name__ == "__main__":
    typing_test()  #run the typing test function
 