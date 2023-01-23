import fuelpump, hashgame

def main():
    while True:
        print('Challenges by Lucas')
        print('-------------------')
        print()
        print(' 1 - Hashgame')
        print(' 2 - Fuel Pump')
        print(' 3 - Exit')
        
        try:
            choice = int(input('Choice: '))
            if choice == 3: break
            
            if choice == 1: hashgame.game()
            elif choice == 2: fuelpump.open()
        except ValueError:
            print('Invalid choice, try again.')
        

if __name__ == '__main__':
    main()
