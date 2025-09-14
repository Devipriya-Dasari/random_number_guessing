<img width="1215" height="312" alt="Screenshot (67)" src="https://github.com/user-attachments/assets/ea4bcc5a-3928-437f-ae75-0eed87c34b3a" />

# Number Guessing Game

A simple Python console game where the computer randomly picks a number between 1 and 100, and the player tries to guess it. After each guess, the game gives hints like "Too high" or "Too low", and shows the total number of attempts once the correct number is guessed.


##  Features

- Random number generation using Python’s `random.randint()`  
- Input validation: handles non‑numeric or out‑of‑range guesses without crashing  
- Feedback hints: “Too high!” or “Too low!” to guide the player  
- Count of attempts: shows how many guesses you took when you finally get it right  
- Very beginner‑friendly: easy to understand and modify

---

##  How It Works

1. The game selects a random integer between 1 and 100.  
2. You type in your guess.  
3. If your guess isn’t correct, you get a hint:  
   - If too high → “Too high!”  
   - If too low → “Too low!”  
4. You continue guessing until you get the right number.  
5. Once guessed correctly, the game displays how many attempts were made.
