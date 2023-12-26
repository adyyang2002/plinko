import locale
import random

class PlinkoGame:
    def __init__(self, initial_balance=0):
        # Initialize game variables here
        self.balance = initial_balance

    def play(self):
        print(f"Balance before play: {self.balance}")
        amount = self.get_amount()
        num_rows = self.get_num_rows()
        risk = self.get_risk()
        self.balance -= amount
        result = self.single_play(amount, risk, num_rows)
        self.balance += result
        if result >= amount:
            print(f"Amount earned: {result - amount}")
        else:
            print(f"Score: {result}")
            print(f"Amount lost: {round((amount - result) * -1, 2)}")

        print(f"Balance after play: {self.balance}")
        #implement play again
        self.play_again()
    def get_amount(self):
        # Get the amount of money from the user
        while True:
            try:
                # Make sure to regulate the amount
                bet = float(input("Enter bet amount: "))
                if bet < 0:
                    print("Please enter an amount over 0.")
                elif bet > self.balance:
                    print(f"Please enter an amount under {self.balance}")
                else:
                    return bet
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_num_rows(self):
        # Get the number of rows from the user
        while True:
            try:
                num_rows = int(input("Enter the number of rows (8-16): "))
                if num_rows < 8 or num_rows > 16:
                    print("Please enter a number in the range 8-16.")
                else:
                    return num_rows
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_risk(self):
        while True:
            try:
                risk = int(input("Enter risk (1, 2, or 3): "))
                if risk in {1, 2, 3}:
                    return risk
                else:
                    print("Invalid risk level. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def single_play(self, bet, risk, num_rows):
        return self.score_game(bet, risk, num_rows)

    def play_again(self):
        while True:
            try:
                decision = input("Would you like to play again? [Y] or [N]:")
                if decision == 'Y' or decision == 'y':
                    return self.play()
                elif decision == 'N' or decision == 'n':
                    return
            except ValueError:
                print("Invalid input. Please enter [Y] or [N].")


    def score_game(self, bet, risk, num_rows):
        #generates the buckets and calculates the risk of each bucket
        #note: might need to seperate generating the buckets and applying the risk
        bucket_list = []
        buckets = num_rows + 1
        counter = buckets * risk * risk
        multiplier = (risk + 1) * .8
        for x in range(buckets):
            if x < buckets/2:
                counter = counter / multiplier
            elif x == buckets/2:
                continue
            else:
                counter = counter * multiplier
            bucket_list.append(round(counter, 1))
        print(bucket_list)
        # determines where the ball ends up
        if num_rows % 2 == 0:
            counter = 0
        else:
            counter = .5

        for i in range(num_rows):
            """
            I know this is an old question, but for anyone curious about random.choice, 
            all it does is return seq[int(self.random() * len(seq))]  
            # raises IndexError if seq is empty (exact code from 2.7.2)
            """
            #coin flip 50/50
            counter += random.choice([-.5, .5])

        counter = int(counter)
        print("counter:")
        print(counter)

        if (num_rows % 2 == 0):
            counter += int(num_rows / 2)
        elif (buckets % 2 == 0):
            counter += int(buckets / 2)

        print("bucket is:")
        print(bucket_list[counter])
        # print("new count:")
        # print(counter)

        # calculate the result based on the bet*risk of the bucket landed
        print("bet size:")
        print(bet)

        return round(bucket_list[counter] * bet, 2)

# Example Usage:
plinko_game = PlinkoGame(initial_balance=100)  # Set an initial balance have an api call to sui?
plinko_game.play()
