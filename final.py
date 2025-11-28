import escape

while True:
    adventure_choice = input("Welcome to 'Escape the Castle' choose your own adventure story! Are you ready?\nEnter Y or N: ").lower()
    
    if adventure_choice == 'escape from the castle':
        print("If at any point you are no longer interested in the story, simply enter Q to quit.")
        escape.Escape_From_The_Castle()
        break

    else:
        print("Invalid choice. Please try again.")