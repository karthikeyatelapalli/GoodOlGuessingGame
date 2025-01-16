# Good Ol' Guessing Game

This Python program is an engaging and simple guessing game. The program randomly selects a number between 1 and 100, and the user must guess the number within 10 attempts. The program provides feedback for each guess, helping the user refine their predictions.

---

## **Features**
1. **Random Number Generation**:
   - The program generates a random number between 1 and 100 using Python's `random` module.

2. **Input Validation**:
   - Ensures the user's guess is within the range of 1 to 100.
   - Prompts the user to re-enter a valid guess if the input is out of range.

3. **Feedback Mechanism**:
   - Tells the user if their guess is too high, too low, or correct.
   - Tracks the number of guesses made.

4. **Win or Lose Conditions**:
   - **Win**: If the user guesses the number correctly within 10 attempts, the program congratulates them and displays the number of tries.
   - **Lose**: If the user fails to guess the number within 10 attempts, the program reveals the correct answer.

---

## **How to Run**

### **Requirements**
- Python 3.x
- No additional libraries are required.

### **Steps**
1. Save the program as `guessing_game.py`.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the program.
4. Run the program:
   ```bash
   python3 guessing_game.py
