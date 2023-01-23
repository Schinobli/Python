hashgame = [['','',''],['','',''],['','','']]
class InvalidValue(Exception):
    pass


def play(player, move:int):
    if move in (1,2,3):
        if not hashgame[0][move-1]:
            hashgame[0][move-1] = player
            return True
        else: return False
    elif move in (4,5,6):
        if not hashgame[1][move-4]:
            hashgame[1][move-4] = player
            return True
        else: return False
    elif move in (7,8,9):
        if not hashgame[2][move-7]:
            hashgame[2][move-7] = player
            return True
        else: return False
        
def resetGame():
    global hashgame
    hashgame = [['','',''],['','',''],['','','']]

        
def verifyWin():
    x = False
    y = False
    for i in range(3):
        if not x:
            x = True if hashgame[i][0] == hashgame[i][1] == hashgame[i][2] != '' else False
        if not y:
            y = True if hashgame[0][i] == hashgame[1][i] == hashgame[2][i] != '' else False
    if x: return x
    if y: return y
    
    z = False
    if not z:
        z = True if hashgame[0][0] == hashgame[1][1] == hashgame[2][2] != '' else False
    if not z:
        z = True if hashgame[0][2] == hashgame[1][1] == hashgame[2][0] != '' else False
    if z: return z

def game():
    while True:
        print()
        print('------   HASHGAME ------')
        print('--by Lucas Schinobli----')
        print()
        print('-1 to exit')
        playerX = input('Player X name: ')
        if playerX == '-1': break
        playerO = input('Player O name: ')
        if playerO == '-1': break
        move = 'O'
        cont = 0
        resetGame()
        
        while True:
            for i in hashgame:
                print(i)
                
            if verifyWin():
                print('{} win. '.format(playerX if move == 'X' else playerO))
                break
            try:
                move = 'X' if move == 'O' else 'O'
                col = int(input('{} what is your choice? '.format(playerX if move == 'X' else playerO)))
                
                if col > 9: raise ValueError
                
                if not play(move, col):
                    raise InvalidValue
    
                cont += 1
                
                if cont == 9: 
                    print('Draw.')
                    break 
                
            except (ValueError, InvalidValue):
                move = 'X' if move == 'O' else 'O'
                print('Invalid choice.')

