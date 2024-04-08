import numpy as np
import matplotlib.pyplot as plt

def simulate_reverse_martingale_with_variable_profit_taking(initial_balance, initial_bet, n_flips):
    bank_balance = np.zeros(n_flips)
    current_balance = initial_balance
    current_bet = initial_bet
    consecutive_wins = 0 # Track consecutive wins
    bank_balance[0] = current_balance

    for i in range(1, n_flips):
        # Simulate coin flip: 1 for win, 0 for loss
        flip_result = np.random.randint(0, 2)
        if flip_result == 1: # win
            current_balance += current_bet
            consecutive_wins += 1
            if consecutive_wins in [7]:
                current_bet = initial_bet # Take profit and reset bet
                consecutive_wins = 0 # reset consecutive wins count
            else:
                current_bet *= 2 # double the bet if not at a profit-taking point
        else: # loss
            current_balance -= current_bet
            current_bet = initial_bet # reset bet to initial bet
            consecutive_wins = 0 # reset consecutive wins count
        
        # Update bank balance
        bank_balance[i] = current_balance
        
        # End simulation if balance is 0 or less
        if current_balance <= 0:
            break
            
    return bank_balance[:i+1] # return the updated bank balance

# Simulation parameters
initial_balance = int(input("What would you like your initial balance to be? : "))
initial_bet = initial_balance / 100
n_flips = int(input("How many flips would you like to simulate? : "))

# Simulate the Reverse Martingale strategy with profit-taking feature
bank_balance = simulate_reverse_martingale_with_variable_profit_taking(initial_balance, initial_bet, n_flips)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(bank_balance, label='Bank Balance')
plt.title('Reverse Martingale Strategy with Profit Taking')
plt.xlabel('Number of Flips')
plt.ylabel('Bank Balance')
plt.axhline(initial_balance, color='r', linestyle='--', label='Initial Balance')
plt.legend()
plt.show()