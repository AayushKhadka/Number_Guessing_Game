# ================================
# Number Guessing Game
# ================================
# Author: Ayush Khadka
# Description:
#   A console-based number guessing game where
#   the player chooses a difficulty level and
#   tries to guess a random number. Score
#   decreases with every wrong guess.
# ================================

import random
from colorama import Fore, Style

score = 100


print(Fore.GREEN + "================================" + Style.RESET_ALL)
print(Fore.GREEN + "   Welcome to the Guessing Game!" + Style.RESET_ALL)
print(Fore.GREEN + "================================\n" + Style.RESET_ALL)


print(Fore.CYAN + "Choose a difficulty:" + Style.RESET_ALL)
print("1. Easy   (1-50,  10 attempts, -5 per wrong guess)")
print("2. Medium (1-100,  7 attempts, -15 per wrong guess)")
print("3. Hard   (1-200,  5 attempts, -25 per wrong guess)")

level = int(input(Fore.CYAN + "\nEnter 1, 2 or 3: " + Style.RESET_ALL))


if level == 1:
    secret_number = random.randint(1, 50)
    attempts = 10
    penalty = 5
    print(Fore.GREEN + "\n🟢 Easy mode! Good luck!\n" + Style.RESET_ALL)
elif level == 2:
    secret_number = random.randint(1, 100)
    attempts = 7
    penalty = 15
    print(Fore.YELLOW + "\n🟡 Medium mode! Good luck!\n" + Style.RESET_ALL)
elif level == 3:
    secret_number = random.randint(1, 200)
    attempts = 5
    penalty = 25
    print(Fore.RED + "\n🔴 Hard mode! Good luck!\n" + Style.RESET_ALL)
else:
    print(Fore.RED + "Invalid choice! Starting Medium mode." + Style.RESET_ALL)
    secret_number = random.randint(1, 100)
    attempts = 7
    penalty = 15

print(Fore.YELLOW + f"You have {attempts} attempts. Good luck!\n" + Style.RESET_ALL)


while attempts > 0:
    guess = int(input(Fore.WHITE + "What is your guess?: " + Style.RESET_ALL))

 
    if guess == secret_number:
        print(Fore.GREEN + f"\n🎉 Damn! You got it right! Congrats!" + Style.RESET_ALL)
        print(Fore.CYAN + f"🏆 Your final score: {score}" + Style.RESET_ALL)
        break

    # Too high
    elif guess > secret_number:
        attempts -= 1
        score -= penalty
        print(Fore.RED + f"📈 Too high! Attempts left: {attempts} | Score: {score}\n" + Style.RESET_ALL)

    # Too low
    else:
        attempts -= 1
        score -= penalty
        print(Fore.YELLOW + f"📉 Too low! Attempts left: {attempts} | Score: {score}\n" + Style.RESET_ALL)


if attempts == 0:
    print(Fore.RED + f"\n💀 Game over! The number was {secret_number}." + Style.RESET_ALL)
    print(Fore.RED + f"Better luck next time! Final score: {score}" + Style.RESET_ALL)