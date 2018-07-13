from random import randint

print("THE GAME IS PLAYED USING THE NUMPAD")
isRunning = True


def introduce_number(messageBeforeIntroduction):
    """Makes the user introduce the desired number and tests it if it is correct or not."""
    number = int(input(messageBeforeIntroduction))
    while not is_correct_number(number):
        number = int(input("introduce the number again"))
    if number < 4:
        number += 6
    elif number > 6:
        number -= 6
    return number


def is_correct_number(correct_number):
    """Verifies if the number is correct or not."""
    if type(correct_number) == int and 10 > correct_number > 0:
        return True
    return False


def randomize_badplayer_movement(player):
    """Randomizes the bad player's move."""
    badPlayerMove = randint(1, 9)
    while len(list(filter(lambda item: item == badPlayerMove, movementList))) > 0:
        badPlayerMove = randint(1, 9)
    else:
        movementList.append(badPlayerMove)
        OMovementList.append(badPlayerMove) if player == 'x' else xMovementList.append(badPlayerMove)


def player_input(player):
    """Player input."""
    playersMove = introduce_number("introduce number")
    while len(list(filter(lambda item: item == playersMove, movementList))) > 0:
        playersMove = introduce_number("introduce another number")
    else:
        movementList.append(playersMove)
        xMovementList.append(playersMove) if player == 'x' else OMovementList.append(playersMove)


def draw_matrix():
    """Draws the matrix to emulate the Tic Tac Toe board."""
    row = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    for i in range(3):
        row = set_rows(i + 1, row)
    for i in range(3):
        if i == 1:
            print(f'   {row[0]}   |  {row[1]}  |   {row[2]}   ')
        else:
            print(f'       |     |      ')
    print('-----------------------')
    for i in range(3, 6):
        row = set_rows(i + 1, row)
    for i in range(3, 6):
        if i == 4:
            print(f'   {row[3]}   |  {row[4]}  |   {row[5]}   ')
        else:
            print(f'       |     |       ')
    print('-----------------------')
    for i in range(6, 9):
        row = set_rows(i + 1, row)
    for i in range(6, 9):
        if i == 7:
            print(f'   {row[6]}   |  {row[7]}  |   {row[8]}   ')
        else:
            print(f'       |     |       ')


def set_rows(i, row):
    """Sets the individual rows of the Tic Tac Toe board."""
    if i in list(filter(lambda item: item == i, xMovementList)):
        row[i - 1] = 'X'
    if i in list(filter(lambda item: item == i, OMovementList)):
        row[i - 1] = '0'
    return row


def check_win():
    """Checks if one of the players finished the game and WON"""
    if check_XorO_win(xMovementList):
        print('X has won')
        return True
    if check_XorO_win(OMovementList):
        print('0 has won')
        return True
    return False


def check_XorO_win(list):
    for i in range(1, 4):
        if i in list and i + 3 in list and i + 6 in list:
            return True
    for i in range(1, 8, 3):
        if i in list and i + 1 in list and i + 2 in list:
            return True
    if 1 in list and 5 in list and 9 in list:
        return True
    if 3 in list and 5 in list and 7 in list:
        return True
    return False


movementList = []
xMovementList = []
OMovementList = []

while isRunning:
    movementList = []
    xMovementList = []
    OMovementList = []
    draw_matrix()
    isPlayerTurn = False
    player = input('Do you want to be X or 0?')

    if player.lower() == 'x':
        isPlayerTurn = True

    if isPlayerTurn:
        player_input(player)
        isPlayerTurn = False
        randomize_badplayer_movement(player)
        isPlayerTurn = True
    else:
        randomize_badplayer_movement(player)
        isPlayerTurn = True
        player_input(player)
        isPlayerTurn = False

    draw_matrix()
    while len(movementList) < 9:
        if isPlayerTurn:
            player_input(player)
            if check_win():
                break
            isPlayerTurn = False
        else:
            randomize_badplayer_movement(player)
            if check_win():
                break
            isPlayerTurn = True
        draw_matrix()

    draw_matrix()

    continueGame = int(input('Do you still want to play the game (1)->yes (0) ->no'))
    if continueGame == 0:
        isRunning = False
