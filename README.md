# 🎮 Number Guessing Game

A Python console game where the player guesses a randomly generated number.
Built as a personal project at CCBC to practice Python fundamentals including
loops, conditionals, functions, and the colorama library for colored output.

---

## 🎯 How to Play

1. Choose a difficulty level at the start
2. Try to guess the secret number
3. You get hints after each guess (too high or too low)
4. Score decreases by a penalty for every wrong guess
5. Guess correctly before running out of attempts to win!

---

## ⚙️ Difficulty Levels

| Level | Range | Attempts | Penalty per wrong guess |
|---|---|---|---|
| 🟢 Easy | 1 – 50 | 10 | -5 points |
| 🟡 Medium | 1 – 100 | 7 | -15 points |
| 🔴 Hard | 1 – 200 | 5 | -25 points |

---

## 💻 Example Output
```
================================
   Welcome to the Guessing Game!
================================

Choose a difficulty:
1. Easy   (1-50,  10 attempts, -5 per wrong guess)
2. Medium (1-100,  7 attempts, -15 per wrong guess)
3. Hard   (1-200,  5 attempts, -25 per wrong guess)

Enter 1, 2 or 3: 1
🟢 Easy mode! Good luck!

What is your guess?: 32
📈 Too high! Attempts left: 9 | Score: 95

What is your guess?: 12
📉 Too low! Attempts left: 8 | Score: 90

What is your guess?: 21
🎉 Damn! You got it right! Congrats!
🏆 Your final score: 75
```

---

## 🛠 How to Run

**Step 1 — Install colorama:**
```bash
pip3 install colorama
```

**Step 2 — Run the game:**
```bash
python3 Number_Gussing_Game.py
```

---

## 💡 Concepts Used

- Random number generation
- While loops and for loops
- If / elif / else conditionals
- F-strings for clean output
- Colorama library for colored terminal text
- Score and penalty system

---

## 👤 Author

**Ayush Khadka**
[GitHub](https://github.com/AayushKhadka) • [LinkedIn](https://www.linkedin.com/in/ayush-khadka-662b082a7/)
