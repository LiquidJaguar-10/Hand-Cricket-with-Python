import random
name = input('Enter your name')
print('Welcome to hand cricket arena,', name)

def playerbatting():
    player_score = 0
    while(True):

        player_runs = int(input('Enter a number from 0 to 6'))
        computer_bowling = random.randint(0, 6)
        if player_runs > 6:
            print('Invalid Input')
            exit()
        if player_runs < 0:
            print('Invalid Input')
            exit()
        print('Computer chose:', computer_bowling)
        if player_runs != computer_bowling:
            player_score = player_score + player_runs
            print('Your score is', player_score)
        elif player_runs == computer_bowling:
            print('You are',random.choice(['cleaned up by an outstanding yorker','caught at slip','run out','stumped by a lightning quick stumping']))
            print('Your score is:', player_score)
            break
    print('Computer needs', player_score + 1, 'runs to win')
    print('Second Innings has Started! Now enter your numbers')
    computer_score = 0
    while(True):
        player_bowling = int(input('Enter a number from 0 to 6'))
        computer_runs = random.randint(0, 6)
        if player_bowling > 6:
            print('Invalid Input')
            exit()
        if player_bowling < 0:
            print('Invalid Input')
            exit()
        print('Computer chose', computer_runs)
        computer_score = computer_score + computer_runs
        print('Computer score is', computer_score)
        if computer_score > player_score:
            print('COMPUTER FINISHES THE GAME IN STYLE WITH A THUMPING W!')
            exit()
        if computer_runs == player_bowling:
            print('COMPUTER IS OUT WITH A SCORE OF', computer_score)
            if computer_score < player_score:
                print('YOU SUCCESSFULLY WIN THE GAME COMPREHENSIVELY BY', player_score - computer_score,'RUNS!')
            else:
                print('THE MATCH IS TIED! WHAT AN END TO THE GAME!')
                exit()

def computerbatting():
    computer_score = 0
    while(True):

        player_bowling = int(input('Enter a number from 1 to 6'))
        computer_runs = random.randint(1, 6)
        if player_bowling > 6:
            print('Invalid Input')
            exit()
        if player_bowling < 1:
            print('Invalid Input')
            exit()
        print('Computer chose:', computer_runs)
        if computer_runs != player_bowling:
            computer_score = computer_score + computer_runs
            print('Computer\'s score is', computer_score)
        elif computer_runs == player_bowling:
            print('Computer is',random.choice(['cleaned up by an outstanding yorker','caught at slip','run out','stumped by a lightning quick stumping']))
            print('Computer\'s score is:', computer_score)
            break
    print(name,'needs', computer_score + 1, 'runs to win')
    print('Second Innings has Started! Now enter your numbers')
    player_score = 0
    while(True):
        player_runs = int(input('Enter a number from 1 to 6'))
        computer_bowling = random.randint(1, 6)
        if player_runs > 6:
            print('Invalid Input')
            exit()
        if player_runs < 1:
            print('Invalid Input')
            exit()
        print('You chose', player_runs)
        print('Computer chose:',computer_bowling)
        player_score = player_score + player_runs
        print('Player Score is', player_score)
        if computer_score < player_score:
            print('YOU FINISH THE GAME IN STYLE WITH A THUMPING W!')
            exit()
        if player_runs == computer_bowling:
            print('YOU ARE OUT WITH A SCORE OF', player_score)
            if player_score < computer_score:
                print('COMPUTER SUCCESSFULLY WINS THE GAME COMPREHENSIVELY BY', computer_score - player_score, 'RUNS!')
            else:
                print('THE MATCH IS TIED! WHAT AN END TO THE GAME!')
                exit()

a = input('Enter heads or tails')
toss = random.choice(['heads', 'tails'])
if a == toss:
    player_input = input('You win the toss and what do you choose to do? (bat/bowl)')
    print('You decided to', player_input, 'first')
    if player_input == 'bat':
        print('First Innings has Started!')
        playerbatting()
    elif player_input == 'bowl':
        print('First Innings has Started!')
        computerbatting()
    else:
        print('INVALID INPUT')
else:
    computer_input = random.choice(['bat', 'bowl'])
    print('Computer wins the toss and chooses to', computer_input)
    if computer_input == 'bat':
        print('First Innings has Started!')
        playerbatting()
    else:
        print('First Innings has Started!')
        computerbatting()
