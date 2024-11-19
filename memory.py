"""
ᴛᴇꜱᴛ ʏᴏᴜʀ ᴍᴇᴍᴏʀʏ (ᴀ ᴛᴇxᴛ ʙᴀꜱᴇᴅ ᴍᴇᴍᴏʀʏ ɢᴀᴍᴇ)
"""
import random
import sys
import os 
import subprocess
import time


def initialState(n):
    """
    Returns a n x n sized board containing the initial state
    
    Parameters:
        n (int): Size of the board

    Returns:
        stateBoard (list): multidimensional list of size n x n containing the initial state
    
    Initial state - all boards are not solved
    """

    # return stateBoard
    pass


def initialAssignment(n):
    """
    Returns a n x n sized board containing the assignment of values. Values location is subjected to randomization.

    Parameters:
        n (int): Size of the board

    Returns:
        assignmentBoard (list): multidimensional list of size n x n containing values with randomized placement
    """

    # return assignmentBoard
    pass


def loadBoard(folderName):
    """
    Loads and returns the state board, assignment board and score of a previous game

    Parameters:
        fileName (str): Location of the folder to be read containing the state board, assignment board and score

    Returns:
        assignmentBoard (list): multidimensional list of size n x n containing the saved assignments
        stateBoard (list): multidimensional list of size n x n containing the saved state
        totalMoves (int): score of the saved game
        currentSelection (list): list containing the currently selected cards of the player

    Validation check: No files found in folder

    NOTE: Use os library to traverse folders
    """

    # return assignmentBoard, stateBoard, totalMoves, currentSelection
    pass


def saveBoard(assignmentBoard, stateBoard, totalMoves, currentSelection):
    """
    Exports the current assignment board, state board, current selection and total moves to a file that could be loaded for later use

    Parameters:
        assignmentBoard (list): multidimensional list of size n x n containing the assignments
        stateBoard (list): multidimensional list of size n x n containing the state
        totalMoves (int): score of the game
        currentSelection (list): list containing the currently selected cards of the player

    Returns:
        None
    """
    pass


def gameOver(stateBoard):
    """
    Checks if the board is in the terminal state / fully solved

    Parameters:
        stateBoard (list): multidimensional list of size n x n containing the state

    Returns:
        Returns True if the board is in the terminal state / no more cards left, False otherwise
    """
    pass


def displayBoard(assignmentBoard, stateBoard, currentSelection):
    """
    Displays 2 boards to be played each move of the game

    First board: Displays the board containing the "coordinates" - guide for selection
    Second board: Displays the board with faced up solved pieces and currently selected cards

    Parameters:
        assignmentBoard (list): multidimensional list of size n x n containing the assignments
        stateBoard (list): multidimensional list of size n x n containing the state
        totalMoves (int): score of the game
        currentSelection (list): list containing the currently selected cards of the player

    Returns:
        None (only prints the board)
    """
    pass


def selectCard(assignmentBoard, stateBoard, currentSelection):
    """
    Asks the user for a valid card

    Parameters:
        assignmentBoard (list): multidimensional list of size n x n containing the assignments
        stateBoard (list): multidimensional list of size n x n containing the state
        currentSelection (list): list containing the currently selected cards of the player

    Returns:
        validCardSelected (int): valid card coordinate selected
        False: if an invalid card is selected

    Includes a validation system
    Includes also an option to exit and save game state
    """

    # NOTE: Pseudo-code for exit condition, assuming 'Z' is the key for exit
    # if userInput == 'Z':
    #     # Additional confirmation
    #     print("Input 'Y' or 'y' if you are sure you want to exit")
    #     print("Input any other key to return back to the game")
    #     confirmUserInput = input("Press key: ")
    #     if confirmUserInput == 'Y':
    #         saveBoard(assignmentBoard, stateBoard, currentSelection, totalMoves)
    #         sys.exit()
    #     else:
    #         pass
        
    # if card selected is valid:
    #   return validCardSelected
    # else:
    #   return False
    pass


def coordinateToIndexMap(n):
    """
    Creates a dictionary which maps a coordinate to its x and y index board position

    Parameters:
        size (n): size of the board 

    Returns:
        ciMapDict (dict): Dictionary which maps a "coordinate" to its x and y index board position
    """
    pass


def indexToCoordinateMap(n):
    """
    Creates a dictionary which maps the x and y index board position to its coordinate

    Parameters:
        size (n): size of the board 

    Returns:
        icMapDict (dict): Dictionary which maps the x and y index board positions to the "coordinate"    
    """
    pass


def getAvailableCoordinates(n):
    """
    Gets the list of available coordinates (to be used for validity checking in card selection)

    Parameters:
        assignmentBoard (list): multidimensional list of size n x n containing the assignments
        stateBoard (list): multidimensional list of size n x n containing the state
        currentSelection (list): list containing the currently selected cards of the player
    Returns:
        availableCoordinates (list): list of available coordinates
    """
    # TODO:
    # Get all existing coordinates in the board
    # Get all currently occupied coordinates
    # Get the available coordinates by subtracting the occupied coordinates from existing coordinates
    pass


def checkMatchUpdateBoard(assignmentBoard, stateBoard, currentSelection, matchFound):
    """
    Checks if the two selections are matching and if matching updates the state board
    
    Returns the updated assignmentBoard and stateBoard


    Parameters:
        assignmentBoard (list): multidimensional list of size n x n containing the assignments
        stateBoard (list): multidimensional list of size n x n containing the state
        currentSelection (list): list containing the 2 currently selected cards of the player
    Returns:
        Updated assignmentBoard and stateBoard
        matchFound (bool): True if a match is found, False otherwise

    TODO: Validate that current selection is of size 2
    """

    # return assignmentBoard, stateBoard
    pass


def mainMenu():
    """
    Prints a menu interface that asks the user if they want to start a new game / or continue a previous game / check leaderboards
    Triggers an error if there is no saved game found if user chooses to continue a previous game

    Parameters:
        None
    Returns:
        1 (int): If user wants to start a new game
        2 (int): If user wants to continue a previous saved game 
        3 (int): If user wants to check the leaderboards
        4 (int): If user wants to exit game
        5 (int): If user wants to change user name (create new user, delete user, change user)
    """
    pass


def leaderboards(gameLogFile):
    """
    Creates leaderboards based from game logs and displays the leaderboard
    If the game logs file does not exist, display an empty leaderboard

    Parameters:
        gameLogFile (str): Location of the game log / records file
    Returns:
        1 (int): If user wants to exit the leaderboard back to the menu

    NOTE: There should be seperate leaderboards per each game size mode
    NOTE: The leaderboard contains player name, score, date achieved
    NOTE: Incorporate tiebreak mechanism 
    """

    # return 1
    pass


def updateLeaderboard(name, score, n, gameLogFolderName):
    """
    Determines if the user is added to the leaderboard

    Parameters:
        name (str): Name of the player
        score (int): Final score / total moves after the game is finished
        n (int): Size of the board
        gameLogFile (str): Location of the folder containing the leaderboards
    Returns:
        True, if user is added to leaderboard
        False, if user does not meet requirements for leaderboard
    """
    # Create a ranking of the games
    # Determine if the latest game is part of the leaderboard - meets ranking required for the leaderboard
    # NOTE: Consider tiebreak mechanism

    pass


def clearScreen():
    """
    Clears the terminal screen

    Reference: https://www.youtube.com/watch?v=Kmu6rmPQt4c 
    """ 

    # Get the operating system
    opSystem = sys.platform

    # For Windows OS
    if opSystem == 'win32':
        subprocess.run('cls')
    # For Linux and Mac OS
    elif opSystem == 'linux' or opSystem == 'darwin':
        subprocess.run('clear')


def welcomeScreen(currentName):
    """
    Displays a welcome sequence (to make the player feel welcomed/hyped)

    Parameters:
        currentName (str): Current username of the player  
    Returns:
        None
    """
    print(f"Welcome {currentName}. Get ready to 'Test Your Memory'")
    time.sleep(2)
    clearScreen()


def congratsScreen(currentName):
    """
    Displays a screen congratulating the user for reaching the leaderboard

    Parameters:
        currentName (str): Current username of the player  
    Returns:
        None    
    """
    # print(f"Congratulations {currentName}! You have been added to the leaderboard.")
    pass


def setUserName(currentUserName):
    """
    Allows user to add user, change current user, delete user

    The current user name will be used for the leaderboards

    After adding/deleting users or changing current user, it should reflect on updating the file containing usernames and current name 

    Parameters:
        currentUserName (str): Current username of the player    
    Returns:
        updatedUserName (str): Updated username of the player

    NOTE: Limit the number of users to be made
    NOTE: Create warning that the user's records will be deleted if the user is deleted
    """

    # TODO: If user is deleted, update game log
    # updateGameLog(currentNameList)

    # TODO: Update user name list file
    # updateNameListFile(currentNameList)

    # TODO: Update current user name file
    # updateNameFile(currentName)

    # return updatedUserName
    pass


def loadRecentUsername():
    """
    Retrieves last set user name
    If no user name was set, ask user to input their name

    Parameters:
        None    
    Returns:
        name (str): last set or newly set username of the player
    """

    name = None

    ####################
    # TODO: Retrieve user name, if it exist
    

    ####################
    # Ask user for a username, if it does not exist
    if name == None:
        while True:

            name = input("What is your name? (Will be used for leaderboards): ")
            time.sleep(1) # Add 2.5 second delay
            clearScreen()

            # Confirm if user inputs the correct name
            nameConfirm = input(f"Hi your name will be '{name}'. Type 'Y' or 'y' to confirm. Enter any other key to re-enter name. \n")

            if nameConfirm in ['Y', 'y']:
                clearScreen()
                time.sleep(1)
                break

            time.sleep(1) # Add 2.5 second delay
            clearScreen()    

    # TODO: Update user name list
    # updateNameListFile(currentNameList)

    return name


def updateNameFile(currentName):
    """
    Updates current user name file

    Parameters:
        currentName (str): Current username of the player (that will overwrite the current username file)   
    Returns:
        None
    """
    pass


def updateNameListFile(currentNameList):
    """
    Updates current name list file

    Parameters:
        currentNameList (list): Current username list (that will overwrite the current username list file)   
    Returns:
        None
    """
    pass


def recordGameLog(currrentName, score, n):
    """
    Stores completed game data into a csv file with columns [id, name, score, gameType, datetime completed]

    If game log file does not exist, create one and add the first entry

    Parameters:
        currentName (str): Current username of the player
        score (int): Score by the user
        n (int): Size of the board
    Returns:
        None
    """
    pass


def updateGameLog(currentNameList):
    """
    If a user is deleted, updates the game log file (deletes all log entries of deleted user)
    After updating, reorganizes the log such that there are no empty rows

    Parameters:
        currentNameList (list): Current username list
    Returns:
        None
    """
    # Check for deleted user/s: Compare name in the log with those not in the name list

    # Delete log entries of deleted user

    # Reorganizes log such that there are no empty rows
    pass


def totalMovesToScore(totalMoves):
    """
    Converts total moves to score

    Parameters:
        totalMoves (int): Total moves by the user
    Returns:
        score (int): Score by the user

    TODO: Create a scoring system
    """

    # return score
    pass


def playGame(type, name):
    """
    Executes the logic of the game depending if the user wants to play a new game or load a saved game
    
    Parameters:
        type (int): 1, for new game; 2, for continuing a saved game  
        name (str): Current username of the player    
    Returns:
        0 (int): Signal to return back to main menu after game is over
    """

    # Initialize expected folder name
    
    # TODO: (Test if folder is created)
    # Create a folder called 'gameLog' if it does not exist
    currentDir = os.getcwd()
    finalDir = os.path.join(currentDir, r'gameLog')
    if not os.path.exists(finalDir):
        os.makedirs('gameLog')

    gameLogsFolderName = 'gameLog'
    savedFilesFolderName = 'save'

    # CASE 1: New game
    if type == 1:
        
        # Initialize nChoice (for game board size)
        nChoice = -1 # Note: -1 is arbitrarily selected to enter while loop

        while nChoice not in ['A', 'B', 'C']:
            
            # Ask user for board size
            print("What game board do you want to play?")
            print("A: 4x4 size")
            print("B: 6x6 size")
            print("C: 8x8 size")
            
            nChoice = input("Select memory game board (Input only the letter):")

            if nChoice == 'A' or nChoice == 'a':
                n = 4
            elif nChoice == 'B' or nChoice == 'b':
                n = 6
            elif nChoice == 'C' or nChoice == 'c':
                n = 8
            else:
                print("")
                print("Input not in choices.")
                print("")

            time.sleep(2.5) # Add 2.5 second delay

            clearScreen()

        clearScreen()

        stateBoard = initialState(n)
        assignmentBoard = initialAssignment(n)
        totalMoves = 0 # Used to track score

        # Initialize empty current selection
        currentSelection = []

        # Play the game
        # Simulate a complete round (complete round - flipping 2 cards)
        while gameOver(stateBoard) == False:
            
            selectedCard = False # Initialize selected card (for while loop entry)

            while selectedCard == False:
                # Ask user for the position of the first card they want to flip
                displayBoard(assignmentBoard, stateBoard, currentSelection)
                selectedCard = selectCard(assignmentBoard, stateBoard, currentSelection, totalMoves)
                clearScreen()
            
            # Add card to current selection
            currentSelection.append(selectedCard)

            # Update total moves
            totalMoves += 1

            time.sleep(1/3)
            clearScreen()

            selectedCard = False # Initialize selected card (for while loop entry)

            while selectedCard == False:
                # Ask user for the position of the second card they want to flip
                displayBoard(assignmentBoard, stateBoard, currentSelection)
                selectedCard = selectCard(assignmentBoard, stateBoard, currentSelection, totalMoves)
                clearScreen()

            # Add card to current selection
            currentSelection.append(selectedCard)

            # Update total moves
            totalMoves += 1

            # Check if current selection matches or not and update if necessary
            assignmentBoard, stateBoard, matchFound = checkMatchUpdateBoard(assignmentBoard, stateBoard, currentSelection)

            # Print indicator of whether the player has found a match
            if matchFound == True:
                # TODO: Print check mark
                pass 
            else:
                # TODO: Print cross mark
                pass

            # Clear current selection of cards
            currentSelection.pop()
            currentSelection.pop()

            time.sleep(1/3)
            clearScreen()

            # Check if game is over / arrived in terminal state
            if gameOver(stateBoard) == True:
                print(f"Your final score is {totalMovesToScore(totalMoves)}")
                recordGameLog(name, totalMovesToScore(totalMoves), n)
                if updateLeaderboard(name, totalMovesToScore(totalMoves), n, gameLogsFolderName) == True:
    
                    clearScreen()
                    congratsScreen(name)
                    time.sleep(6) # 6 seconds delay
                    clearScreen()

                    input("Press Enter to return to main menu...")
                    return 0 # Returns user back to main() - back to main menu

            else:
                pass
            
    # CASE 2: Load previous game
    elif type == 2:

        # Load saved files
        assignmentBoard, stateBoard, totalMoves, currentSelection = loadBoard(savedFilesFolderName)

        # Get n (use assignmentBoard as reference)
        n = len(assignmentBoard)

        # Special case: One card has already been selected
        if len(currentSelection) == 1:

            selectedCard = False # Initialize selected card (for while loop entry)

            while selectedCard == False:
                # Ask user for the position of the second card they want to flip
                displayBoard(assignmentBoard, stateBoard, currentSelection)
                selectedCard = selectCard(assignmentBoard, stateBoard, currentSelection, totalMoves)
                clearScreen()

            # Add card to current selection
            currentSelection.append(selectedCard)

            # Update total moves
            totalMoves += 1

            # Check if current selection matches or not and update if necessary
            assignmentBoard, stateBoard, matchFound = checkMatchUpdateBoard(assignmentBoard, stateBoard, currentSelection)

            # Print indicator of whether the player has found a match
            if matchFound == True:
                # TODO: Print check mark
                pass 
            else:
                # TODO: Print cross mark
                pass    

            # Clear current selection of cards
            currentSelection.pop()
            currentSelection.pop()

            time.sleep(1/3)
            clearScreen()

            # Check if game is over / arrived in terminal state
            if gameOver(stateBoard) == True:
                print(f"Your final score is {totalMovesToScore(totalMoves)}")
                recordGameLog(name, totalMovesToScore(totalMoves), n)
                if updateLeaderboard(name, totalMovesToScore(totalMoves), n, gameLogsFolderName) == True:
    
                    clearScreen()
                    congratsScreen(name)
                    time.sleep(6) # 6 seconds delay
                    clearScreen()

                    input("Press Enter to return to main menu...")
                    return 0 # Returns user back to main() - back to main menu
                
        # Simulate a complete round (complete round - flipping 2 cards)
        while gameOver(stateBoard) == False:

            selectedCard = False # Initialize selected card (for while loop entry)

            while selectedCard == False:
                # Ask user for the position of the first card they want to flip
                displayBoard(assignmentBoard, stateBoard, currentSelection)
                selectedCard = selectCard(assignmentBoard, stateBoard, currentSelection, totalMoves)
                clearScreen()
            
            # Add card to current selection
            currentSelection.append(selectedCard)

            # Update total moves
            totalMoves += 1

            time.sleep(1/3)
            clearScreen()

            # Ask user for the position of the second card they want to flip
            displayBoard(assignmentBoard, stateBoard, currentSelection)
            selectedCard = selectCard(assignmentBoard, stateBoard, currentSelection, totalMoves)

            # Add card to current selection
            currentSelection.append(selectedCard)

            # Update total moves
            totalMoves += 1

            # Check if current selection matches or not and update if necessary
            assignmentBoard, stateBoard, matchFound = checkMatchUpdateBoard(assignmentBoard, stateBoard, currentSelection)

            # Print indicator of whether the player has found a match
            if matchFound == True:
                # TODO: Print check mark
                pass 
            else:
                # TODO: Print cross mark
                pass

            # Clear current selection of cards
            currentSelection.pop()
            currentSelection.pop()

            time.sleep(1/3)
            clearScreen()

            # Check if game is over / arrived in terminal state
            if gameOver(stateBoard) == True:
                print(f"Your final score is {totalMoves}")
                recordGameLog(name, totalMovesToScore(totalMoves), n)
                if updateLeaderboard(name, totalMovesToScore(totalMoves), n, gameLogsFolderName) == True:
    
                    clearScreen()
                    congratsScreen(name)
                    time.sleep(6) # 6 seconds delay
                    clearScreen()

                    input("Press Enter to return to main menu...")
                    return 0 # Returns user back to main() - back to main menu

            else:
                pass

    else:
        raise Exception("Invalid Type")
    

def main():
    """
    Executes the flow of the program
    """

    clearScreen()

    # Retrieve name of user from previous session. If no name can be retrieved, ask for the name.
    currentName = loadRecentUsername()

    # Welcome screen
    welcomeScreen(currentName)

    # Start program (begins with main menu)
    while True:

        menuChoice = mainMenu()

        # Choice 1: Play a new game
        if menuChoice == 1:
            type = 1
            playGame(type, currentName)

        # Choice 2: Load previous game
        elif menuChoice == 2:
            type = 2
            playGame(type, currentName)

        # Choice 3: Display leaderboard screen
        elif menuChoice == 3:
            leaderboards()
        
        # Choice 4: Exit program
        elif menuChoice == 4:
            sys.exit()

        # Choice 5: Set user name screen
        elif menuChoice == 5:
            currentName = setUserName(currentName)
        
        else:
            raise Exception("Invalid Choice")
        

if __name__ == "__main__":
    main()


