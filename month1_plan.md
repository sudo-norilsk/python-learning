# Month 1 Detailed Plan - Python Foundations 🐍

## **MONTH 1 OVERVIEW**
**Goal:** Master Python fundamentals and build 12+ real projects
**Daily Commitment:** 5-6 hours (2h morning, 2-3h afternoon, 1h evening)
**Books:** "Python Crash Course" + "Code" by Petzold + "Automate the Boring Stuff"

---

# **LINUX SETUP COMMANDS** 🐧

## **Initial System Setup (Run Once)**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install development tools
sudo apt install -y build-essential curl wget git vim nano tree htop

# Install Python 3.11+
sudo apt install -y python3 python3-pip python3-venv python3-dev

# Install VS Code
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update && sudo apt install -y code

# Create workspace
mkdir -p ~/python-projects/{week1,week2,week3,week4}
cd ~/python-projects

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install essential packages
pip install requests beautifulsoup4 matplotlib pandas flask

# Git configuration
git config --global user.name "Your Name"
git config --global user.email "your.email@gmail.com"

# Create useful alias
echo 'alias pyenv="source ~/python-projects/venv/bin/activate"' >> ~/.bashrc
source ~/.bashrc

# Verify everything works
python3 --version && pip --version && code --version && git --version
```

---

# **WEEK 1: PYTHON BASICS & ENVIRONMENT**

## **DAY 1: SETUP & FIRST PROGRAM**

### **Morning (2 hours): Environment Setup**
**8:00-9:00 AM: System Installation**
- [ ] **Run:** All Linux setup commands above
- [ ] **Test:** `python3 --version` (should show 3.11+)
- [ ] **Test:** `code --version` (should show VS Code)
- [ ] **Create:** GitHub account with professional username
- [ ] **Navigate:** `cd ~/python-projects/week1`

**9:00-10:00 AM: First Python Program**
- [ ] **Resource:** "Python Crash Course" Chapter 1 (Getting Started)
- [ ] **Read:** Pages 1-18 (Python basics, variables)
- [ ] **Create:** `hello.py`
- [ ] **Write:** Your first program:
```python
print("Hello, World!")
print("My name is [Your Name]")
print("I'm learning Python to get a job in Czech Republic!")
print("Today is my Day 1 of programming!")

# Variables practice
name = "Your Name"
age = 22
country = "Czech Republic"
goal = "Python Developer"

print(f"\nAbout me:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")
print(f"Goal: {goal}")

# Simple calculations
hours_per_day = 6
days_per_week = 7
total_weekly_hours = hours_per_day * days_per_week

print(f"\nLearning commitment:")
print(f"Hours per day: {hours_per_day}")
print(f"Days per week: {days_per_week}")
print(f"Total weekly hours: {total_weekly_hours}")
```

### **Afternoon (2 hours): Calculator Project**
**2:00-3:00 PM: Basic Calculator**
- [ ] **Resource:** freeCodeCamp Python Tutorial (YouTube) - Calculator section (45min mark)
- [ ] **Create:** `calculator_basic.py`
- [ ] **Build:** Simple calculator:
```python
# Basic calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero!"

# Test the functions
print("Testing calculator functions:")
print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")
print(f"10 * 5 = {multiply(10, 5)}")
print(f"10 / 5 = {divide(10, 5)}")
print(f"10 / 0 = {divide(10, 0)}")
```

**3:00-4:00 PM: Advanced Calculator**
- [ ] **Create:** `calculator_advanced.py`
- [ ] **Build:** Interactive calculator with menu:
```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero!"

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return x ** 0.5
    else:
        return "Error: Cannot calculate square root of negative number!"

def main():
    print("🧮 Advanced Calculator 🧮")
    
    while True:
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Square Root (√)")
        print("7. Quit")
        
        choice = input("\nChoose operation (1-7): ")
        
        if choice == '7':
            print("Thank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"Result: {num1} * {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
                elif choice == '5':
                    result = power(num1, num2)
                    print(f"Result: {num1} ^ {num2} = {result}")
                    
            except ValueError:
                print("Error: Please enter valid numbers!")
                
        elif choice == '6':
            try:
                num = float(input("Enter number for square root: "))
                result = square_root(num)
                print(f"Result: √{num} = {result}")
            except ValueError:
                print("Error: Please enter a valid number!")
        else:
            print("Invalid choice! Please select 1-7.")

if __name__ == "__main__":
    main()
```

### **Evening (1 hour): Reading & Practice**
**8:00-8:30 PM: Book Reading**
- [ ] **Resource:** "Code" by Charles Petzold
- [ ] **Read:** Chapter 1 (Best Friends) - pages 1-15
- [ ] **Focus:** Understanding electricity, switches, and binary basics
- [ ] **Notes:** Write key insights in `day01_notes.txt`

**8:30-9:00 PM: Python Shell Practice**
- [ ] **Open:** Terminal and type `python3`
- [ ] **Practice:** Basic operations:
```python
>>> 2 + 3
>>> 10 / 3
>>> 10 // 3  # Floor division
>>> 10 % 3   # Remainder/modulo
>>> 2 ** 8   # Power
>>> abs(-5)  # Absolute value
>>> round(3.7)  # Rounding
>>> "Hello" + " World"  # String concatenation
>>> "Python" * 3  # String repetition
>>> len("Hello")  # String length
```

### **Day 1 Deliverables:**
- [ ] `hello.py` - First program with variables
- [ ] `calculator_basic.py` - Basic calculator functions
- [ ] `calculator_advanced.py` - Interactive calculator with menu
- [ ] `day01_notes.txt` - Notes from "Code" chapter 1
- [ ] All programs run without errors

---

## **DAY 2: DATA TYPES & COLLECTIONS**

### **Morning (2 hours): Variables & Strings**
**8:00-9:00 AM: String Operations**
- [ ] **Resource:** "Python Crash Course" Chapter 2 (Variables and Simple Data Types)
- [ ] **Read:** Pages 19-35 (variables, strings, numbers)
- [ ] **Create:** `day02_strings.py`
- [ ] **Practice:** String methods:
```python
# String basics
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"Full name: {full_name}")

# String methods
message = "  hello world  "
print(f"Original: '{message}'")
print(f"Upper: '{message.upper()}'")
print(f"Lower: '{message.lower()}'")
print(f"Title: '{message.title()}'")
print(f"Stripped: '{message.strip()}'")
print(f"Replace: '{message.replace('world', 'Python')}'")

# String formatting
name = "Python"
version = 3.11
year = 2024

print(f"{name} {version} was created in {year}")
print("Language: {}, Version: {:.1f}".format(name, version))

# Multi-line strings
poem = """
Programming is fun,
Python makes it easy,
Code every day!
"""
print(poem)
```

**9:00-10:00 AM: Numbers & Math**
- [ ] **Practice:** Number operations:
```python
# Number types
integer_num = 42
float_num = 3.14159
complex_num = 3 + 4j

print(f"Integer: {integer_num}, type: {type(integer_num)}")
print(f"Float: {float_num}, type: {type(float_num)}")
print(f"Complex: {complex_num}, type: {type(complex_num)}")

# Math operations
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulo: {a} % {b} = {a % b}")
print(f"Power: {a} ** {b} = {a ** b}")

# Math functions
import math
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Ceiling of 3.2: {math.ceil(3.2)}")
print(f"Floor of 3.8: {math.floor(3.8)}")
print(f"Pi: {math.pi}")
```

### **Afternoon (2 hours): Lists & Dictionaries Projects**
**2:00-3:00 PM: Shopping List Challenge**

**🎯 YOUR TURN - Build Shopping List Manager:**
Try to create a program that can:
1. Add items to a shopping list
2. Remove items from the list
3. Show all items
4. Keep running until user quits

```python
# Try to build this yourself first!
# Use a list to store items
# Use a while loop to keep the program running
# Handle user input for add/remove/show/quit
```

**✅ My Approach (check after trying):**
```python
# Shopping List Manager
shopping_list = []

def display_menu():
    print("\n🛒 Shopping List Manager 🛒")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Sort list")
    print("5. Search item")
    print("6. Clear list")
    print("7. Quit")

def add_item():
    item = input("Enter item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"✅ Added '{item}' to list")
    else:
        print("❌ Cannot add empty item")

def remove_item():
    if not shopping_list:
        print("❌ List is empty!")
        return
    
    view_list()
    try:
        index = int(input("Enter item number to remove: ")) - 1
        if 0 <= index < len(shopping_list):
            removed = shopping_list.pop(index)
            print(f"✅ Removed '{removed}' from list")
        else:
            print("❌ Invalid item number")
    except ValueError:
        print("❌ Please enter a valid number")

def view_list():
    if not shopping_list:
        print("📝 Shopping list is empty")
    else:
        print(f"\n📝 Shopping List ({len(shopping_list)} items):")
        for i, item in enumerate(shopping_list, 1):
            print(f"  {i}. {item}")

def sort_list():
    if shopping_list:
        shopping_list.sort()
        print("✅ List sorted alphabetically")
        view_list()
    else:
        print("❌ List is empty!")

def search_item():
    if not shopping_list:
        print("❌ List is empty!")
        return
    
    search_term = input("Enter item to search: ").strip().lower()
    found_items = [item for item in shopping_list if search_term in item.lower()]
    
    if found_items:
        print(f"🔍 Found {len(found_items)} item(s):")
        for item in found_items:
            print(f"  - {item}")
    else:
        print(f"❌ No items found containing '{search_term}'")

def clear_list():
    if shopping_list:
        confirm = input("Are you sure you want to clear the list? (y/n): ")
        if confirm.lower() == 'y':
            shopping_list.clear()
            print("✅ List cleared")
    else:
        print("❌ List is already empty!")

def main():
    while True:
        display_menu()
        choice = input("Choose option (1-7): ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_list()
        elif choice == '4':
            sort_list()
        elif choice == '5':
            search_item()
        elif choice == '6':
            clear_list()
        elif choice == '7':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
```

**3:00-4:00 PM: Student Grade Manager Challenge**

**🎯 YOUR TURN - Build Grade Manager:**
Try to create a program that can:
1. Add new students (store name and empty grade list)
2. Add grades to existing students  
3. Show a student's grades and average
4. Show all students and their averages

```python
# Try to build this yourself first!
# Use a dictionary where keys are student names
# Values should be lists of grades
# Calculate averages when displaying
```

**✅ My Approach (check after trying):**
[Previous complete code here - but now user tries first!]

---

## **DAY 3: CONTROL FLOW & LOGIC**

### **Morning (2 hours): If/Else and Loops**
**8:00-9:00 AM: Conditional Challenges**

**🎯 YOUR TURN - Try These First:**
```python
# Challenge 1: Grade Letter Calculator
# Ask for a numeric grade (0-100)
# Print the letter grade (A, B, C, D, F)
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59

# Challenge 2: Age Category
# Ask for person's age
# Print their category: Child (0-12), Teen (13-19), Adult (20-64), Senior (65+)

# Challenge 3: Password Strength Checker
# Ask for a password
# Check if it's at least 8 characters
# Check if it has both letters and numbers
# Print "Strong" or "Weak" with reasons
```

**✅ My Solutions:**
[Solutions provided after challenges]

### **Afternoon (2 hours): Number Guessing Game - Build Step by Step**
**2:00-3:00 PM: Basic Game (Step 1)**

**🎯 YOUR TURN - Build Basic Version:**
Try to create a simple number guessing game:
1. Computer picks random number 1-10
2. User guesses
3. Tell them if they got it right or wrong
4. Show the answer

```python
# You'll need: import random
# random.randint(1, 10) gives random number 1-10
# Try building this basic version first!
```

**✅ Step 1 Solution:**
```python
import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Correct! You win!")
else:
    print(f"Wrong! The number was {number}")
```

**3:00-3:30 PM: Add Hints (Step 2)**

**🎯 YOUR TURN - Add Features:**
Improve your game:
1. Tell user if their guess is too high or too low
2. Let them keep guessing until they get it right
3. Count how many attempts they took

```python
# Try adding while loop and attempt counter
# Give "too high" or "too low" hints
```

**3:30-4:00 PM: Multiple Difficulty Levels (Step 3)**

**🎯 YOUR TURN - Final Challenge:**
Add these advanced features:
1. Let user choose difficulty (Easy: 1-50, Medium: 1-100, Hard: 1-200)
2. Limit number of attempts based on difficulty
3. Add a "play again" option
4. Keep track of wins/losses

```python
# This is the challenging part - try your best!
# Don't worry if you can't get everything working
```

**✅ My Complete Solution:**
[Full advanced game code here]

---

## **The Pattern for ALL Projects:**

### **Every Day Structure:**
1. **🎯 YOUR TURN** - Challenges to try yourself first
2. **✅ My Approach** - My solution (only look after trying)
3. **Step-by-step building** - Start simple, add features
4. **Progressive difficulty** - Each step builds on the last

### **Why This Works:**
- ✅ **Active learning** - You think before seeing solutions
- ✅ **Problem-solving skills** - You develop your own approach  
- ✅ **Confidence building** - You realize you can figure things out
- ✅ **Better understanding** - Compare your approach with mine
- ✅ **Real programming** - This is how developers actually work

### **When You Get Stuck:**
1. **Try for 15-30 minutes** on your own
2. **Look at my hints** (if provided)
3. **Check my solution** and understand the differences
4. **Try coding it again** from scratch using what you learned

**This approach makes you a programmer, not just a code copier!** 🚀

### **Evening (1 hour): Reading & Practice**
**8:00-8:30 PM: Continue "Code"**
- [ ] **Resource:** "Code" by Charles Petzold
- [ ] **Read:** Chapter 2 (Codes and Combinations) - pages 16-30
- [ ] **Focus:** Understanding different types of codes (Morse, Braille)
- [ ] **Notes:** Add insights to `day02_notes.txt`

**8:30-9:00 PM: Python Shell Practice**
- [ ] **Practice:** List and dictionary operations:
```python
>>> fruits = ['apple', 'banana', 'orange']
>>> fruits.append('grape')
>>> fruits
>>> fruits[0]
>>> fruits[-1]  # Last element
>>> fruits[1:3]  # Slicing

>>> person = {'name': 'John', 'age': 25, 'city': 'Prague'}
>>> person['name']
>>> person['country'] = 'Czech Republic'
>>> person.keys()
>>> person.values()
>>> person.items()
```

### **Day 2 Deliverables:**
- [ ] `day02_strings.py` - String operations and formatting
- [ ] `day02_lists.py` - Complete shopping list manager
- [ ] `day02_student_grades.py` - Student grade management system
- [ ] `day02_notes.txt` - Notes from "Code" chapter 2
- [ ] All programs run without errors and handle user input properly

---

## **DAY 3: CONTROL FLOW & LOGIC**

### **Morning (2 hours): Conditionals**
**8:00-9:00 AM: If Statements**
- [ ] **Resource:** "Python Crash Course" Chapter 5 (If Statements)
- [ ] **Read:** Pages 81-94 (conditional tests, if-elif-else chains)
- [ ] **Create:** `day03_conditionals.py`
- [ ] **Practice:** Decision making:
```python
# Basic conditionals
age = 22
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Multiple conditions
temperature = 25
if temperature > 30:
    print("It's hot outside")
elif temperature > 20:
    print("Nice weather")
elif temperature > 10:
    print("A bit cool")
else:
    print("It's cold")

# Logical operators
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Access granted")
elif username == "admin" or username == "user":
    print("Wrong password")
else:
    print("Unknown user")

# Checking multiple values
programming_languages = ['python', 'java', 'javascript', 'c++']
favorite = 'python'

if favorite in programming_languages:
    print(f"{favorite} is a great choice!")
else:
    print(f"{favorite} is not in our list")

# Boolean expressions
is_student = True
has_discount = False

if is_student and not has_discount:
    print("You qualify for student discount!")
```

**9:00-10:00 AM: Complex Conditions**
- [ ] **Build:** Grade calculator with conditions:
```python
def calculate_letter_grade(score):
    """Convert numeric score to letter grade"""
    if score >= 97:
        return 'A+'
    elif score >= 93:
        return 'A'
    elif score >= 90:
        return 'A-'
    elif score >= 87:
        return 'B+'
    elif score >= 83:
        return 'B'
    elif score >= 80:
        return 'B-'
    elif score >= 77:
        return 'C+'
    elif score >= 73:
        return 'C'
    elif score >= 70:
        return 'C-'
    elif score >= 67:
        return 'D+'
    elif score >= 65:
        return 'D'
    else:
        return 'F'

def get_grade_description(letter_grade):
    """Get description for letter grade"""
    descriptions = {
        'A+': 'Excellent work!',
        'A': 'Outstanding performance!',
        'A-': 'Great job!',
        'B+': 'Very good work!',
        'B': 'Good performance!',
        'B-': 'Above average!',
        'C+': 'Satisfactory plus!',
        'C': 'Satisfactory work!',
        'C-': 'Needs some improvement!',
        'D+': 'Below average, needs work!',
        'D': 'Poor performance, study more!',
        'F': 'Failing grade, requires significant improvement!'
    }
    return descriptions.get(letter_grade, 'Unknown grade')

# Test the grade calculator
test_scores = [98, 85, 73, 67, 45]
for score in test_scores:
    letter = calculate_letter_grade(score)
    description = get_grade_description(letter)
    print(f"Score: {score} → Grade: {letter} ({description})")
```

### **Afternoon (2 hours): Number Guessing Game**
**2:00-3:00 PM: Basic Game Logic**
- [ ] **Resource:** Think about game design and user experience
- [ ] **Create:** `day03_guessing_game.py`
- [ ] **Build:** Enhanced number guessing game:
```python
import random
import time

def display_welcome():
    """Display welcome message and rules"""
    print("🎯" + "="*50 + "🎯")
    print("        WELCOME TO THE NUMBER GUESSING GAME!")
    print("🎯" + "="*50 + "🎯")
    print("\n📋 HOW TO PLAY:")
    print("• I'll think of a number within your chosen range")
    print("• You guess the number")
    print("• I'll tell you if your guess is too high or too low")
    print("• Try to guess with as few attempts as possible!")
    print("• Type 'quit' anytime to exit")

def get_difficulty():
    """Let user choose difficulty level"""
    print("\n🎮 Choose your difficulty:")
    print("1. 🟢 Easy   (1-50,  unlimited attempts)")
    print("2. 🟡 Medium (1-100, 10 attempts)")
    print("3. 🔴 Hard   (1-200, 7 attempts)")
    print("4. 💀 Expert (1-500, 5 attempts)")
    
    while True:
        choice = input("\nSelect difficulty (1-4): ").strip()
        if choice == '1':
            return 50, float('inf'), "Easy"
        elif choice == '2':
            return 100, 10, "Medium"
        elif choice == '3':
            return 200, 7, "Hard"
        elif choice == '4':
            return 500, 5, "Expert"
        else:
            print("❌ Please enter 1, 2, 3, or 4")

def play_game(max_num, max_attempts, difficulty):
    """Main game logic"""
    secret_number = random.randint(1, max_num)
    attempts = 0
    
    print(f"\n🎯 {difficulty} Mode: Guess the number between 1 and {max_num}")
    if max_attempts != float('inf'):
        print(f"💥 You have {max_attempts} attempts!")
    
    start_time = time.time()
    
    while attempts < max_attempts:
        # Get user guess
        guess_input = input(f"\n🔢 Attempt {attempts + 1}: Your guess (or 'quit'): ").strip()
        
        if guess_input.lower() == 'quit':
            print(f"🏃 You quit! The number was {secret_number}")
            return False, attempts + 1
        
        # Validate input
        try:
            guess = int(guess_input)
            if guess < 1 or guess > max_num:
                print(f"❌ Please enter a number between 1 and {max_num}")
                continue
        except ValueError:
            print("❌ Please enter a valid number")
            continue
        
        attempts += 1
        
        # Check guess
        if guess == secret_number:
            end_time = time.time()
            time_taken = round(end_time - start_time, 1)
            print(f"\n🎉 CONGRATULATIONS! 🎉")
            print(f"✅ You guessed {secret_number} correctly!")
            print(f"📊 Attempts: {attempts}")
            print(f"⏱️  Time: {time_taken} seconds")
            
            # Performance feedback
            if attempts == 1:
                print("🍀 Incredible! First try!")
            elif attempts <= max_attempts // 3:
                print("🌟 Excellent performance!")
            elif attempts <= max_attempts // 2:
                print("👍 Good job!")
            else:
                print("💪 You made it!")
            
            return True, attempts
            
        elif guess < secret_number:
            remaining = max_attempts - attempts
            if remaining > 0 and max_attempts != float('inf'):
                print(f"📈 Too low! {remaining} attempts remaining")
            else:
                print("📈 Too low! Try higher")
                
            # Give hints for harder difficulties
            if difficulty in ["Hard", "Expert"] and attempts >= 2:
                if abs(guess - secret_number) <= 10:
                    print("🔥 You're getting warm!")
                elif abs(guess - secret_number) <= 25:
                    print("🌡️  You're in the right neighborhood")
                    
        else:  # guess > secret_number
            remaining = max_attempts - attempts
            if remaining > 0 and max_attempts != float('inf'):
                print(f"📉 Too high! {remaining} attempts remaining")
            else:
                print("📉 Too high! Try lower")
                
            # Give hints for harder difficulties
            if difficulty in ["Hard", "Expert"] and attempts >= 2:
                if abs(guess - secret_number) <= 10:
                    print("🔥 You're getting warm!")
                elif abs(guess - secret_number) <= 25:
                    print("🌡️  You're in the right neighborhood")
    
    # Game over - ran out of attempts
    print(f"\n💀 Game Over! You ran out of attempts.")
    print(f"🎯 The number was: {secret_number}")
    return False, attempts

def display_statistics(stats):
    """Display player statistics"""
    if not stats['games_played']:
        print("\n📊 No games played yet!")
        return
    
    print(f"\n📊 YOUR STATISTICS:")
    print("="*40)
    print(f"🎮 Games played: {stats['games_played']}")
    print(f"🏆 Games won: {stats['games_won']}")
    print(f"💔 Games lost: {stats['games_lost']}")
    print(f"📈 Win rate: {stats['win_rate']:.1f}%")
    
    if stats['total_attempts'] > 0:
        avg_attempts = stats['total_attempts'] / stats['games_played']
        print(f"🎯 Average attempts: {avg_attempts:.1f}")
    
    if stats['best_game']:
        print(f"🌟 Best game: {stats['best_game']} attempts")
    
    print("\nDifficulty breakdown:")
    for difficulty, count in stats['difficulty_stats'].items():
        if count > 0:
            print(f"  {difficulty}: {count} games")

def main():
    """Main program loop"""
    # Initialize statistics
    stats = {
        'games_played': 0,
        'games_won': 0,
        'games_lost': 0,
        'win_rate': 0.0,
        'total_attempts': 0,
        'best_game': None,
        'difficulty_stats': {'Easy': 0, 'Medium': 0, 'Hard': 0, 'Expert': 0}
    }
    
    display_welcome()
    
    while True:
        print("\n" + "="*52)
        print("🎯 MAIN MENU")
        print("="*52)
        print("1. 🎮 Play Game")
        print("2. 📊 View Statistics")
        print("3. ❓ How to Play")
        print("4. 🚪 Quit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            max_num, max_attempts, difficulty = get_difficulty()
            won, attempts = play_game(max_num, max_attempts, difficulty)
            
            # Update statistics
            stats['games_played'] += 1
            stats['total_attempts'] += attempts
            stats['difficulty_stats'][difficulty] += 1
            
            if won:
                stats['games_won'] += 1
                if stats['best_game'] is None or attempts < stats['best_game']:
                    stats['best_game'] = attempts
            else:
                stats['games_lost'] += 1
            
            stats['win_rate'] = (stats['games_won'] / stats['games_played']) * 100
            
            # Ask if they want to play again
            play_again = input("\n🔄 Play another game? (y/n): ").strip().lower()
            if play_again != 'y':
                continue
                
        elif choice == '2':
            display_statistics(stats)
            
        elif choice == '3':
            display_welcome()
            
        elif choice == '4':
            print("\n👋 Thanks for playing! Goodbye!")
            if stats['games_played'] > 0:
                print(f"Final stats: {stats['games_won']}/{stats['games_played']} wins ({stats['win_rate']:.1f}%)")
            break
            
        else:
            print("❌ Invalid choice! Please select 1-4")

if __name__ == "__main__":
    main()
```

### **Evening (1 hour): Reading & Loop Practice**
**8:00-8:30 PM: Continue "Code"**
- [ ] **Resource:** "Code" by Charles Petzold
- [ ] **Read:** Chapter 3 (Braille and Binary Codes) - pages 31-45
- [ ] **Focus:** Binary number system, how computers represent numbers
- [ ] **Notes:** Add to `day03_notes.txt`

**8:30-9:00 PM: Loop Practice**
- [ ] **Practice:** Basic loops in Python shell:
```python
>>> # For loops
>>> for i in range(5):
...     print(f"Count: {i}")

>>> # While loops
>>> count = 0
>>> while count < 3:
...     print(f"While: {count}")
...     count += 1

>>> # Loop through lists
>>> colors = ['red', 'green', 'blue']
>>> for color in colors:
...     print(f"I like {color}")

>>> # Loop with enumerate
>>> for index, color in enumerate(colors):
...     print(f"{index}: {color}")
```

### **Day 3 Deliverables:**
- [ ] `day03_conditionals.py` - Conditional logic examples
- [ ] `day03_guessing_game.py` - Complete number guessing game with statistics
- [ ] `day03_notes.txt` - Notes from "Code" chapter 3
- [ ] Understanding of if/elif/else and logical operators
- [ ] Experience with user input validation and game design

---

## **DAY 4: FUNCTIONS & MODULARITY**

### **Morning (2 hours): Function Fundamentals**
**8:00-9:00 AM: Function Basics**
- [ ] **Resource:** "Python Crash Course" Chapter 8 (Functions)
- [ ] **Read:** Pages 135-155 (defining functions, passing arguments, return values)
- [ ] **Create:** `day04_functions.py`
- [ ] **Practice:** Function fundamentals:
```python
# Basic function definition
def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

# Function with multiple parameters
def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

# Function with default parameter
def greet_with_title(name, title="Mr."):
    """Greet someone with a title"""
    return f"Hello, {title} {name}!"

# Function with keyword arguments
def create_profile(name, age, city="Unknown", country="Unknown"):
    """Create a user profile"""
    profile = {
        'name': name,
        'age': age,
        'city': city,
        'country': country
    }
    return profile

# Function with variable arguments
def calculate_average(*numbers):
    """Calculate average of any number of arguments"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Function with keyword variable arguments
def create_car(**car_info):
    """Create a car dictionary with any number of properties"""
    car = {}
    for key, value in car_info.items():
        car[key] = value
    return car

# Testing all functions
print("Function Testing:")
print("="*40)

# Test basic functions
print(greet("Python Learner"))
print(f"5 + 3 = {add_numbers(5, 3)}")

# Test default parameters
print(greet_with_title("Smith"))
print(greet_with_title("Johnson", "Ms."))

# Test keyword arguments
profile1 = create_profile("John", 25)
profile2 = create_profile("Jane", 30, city="Prague", country="Czech Republic")
print(f"Profile 1: {profile1}")
print(f"Profile 2: {profile2}")

# Test variable arguments
print(f"Average of 1,2,3,4,5: {calculate_average(1, 2, 3, 4, 5)}")
print(f"Average of 10,20: {calculate_average(10, 20)}")

# Test keyword variable arguments
my_car = create_car(make="Skoda", model="Octavia", year=2020, color="Blue")
print(f"My car: {my_car}")
```

**9:00-10:00 AM: Advanced Functions**
- [ ] **Practice:** More complex function examples:
```python
# Function returning multiple values
def get_name_parts(full_name):
    """Split full name into parts"""
    parts = full_name.strip().split()
    first_name = parts[0] if parts else ""
    last_name = " ".join(parts[1:]) if len(parts) > 1 else ""
    return first_name, last_name

# Function with nested logic
def classify_temperature(temp, unit="C"):
    """Classify temperature as hot, warm, cool, or cold"""
    if unit.upper() == "F":
        # Convert Fahrenheit to Celsius
        temp = (temp - 32) * 5/9
    
    if temp > 30:
        return "Hot"
    elif temp > 20:
        return "Warm"
    elif temp > 10:
        return "Cool"
    else:
        return "Cold"

# Recursive function
def factorial(n):
    """Calculate factorial recursively"""
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function with lambda expressions
def apply_operation(numbers, operation):
    """Apply an operation to a list of numbers"""
    return [operation(num) for num in numbers]

# Testing advanced functions
print("\nAdvanced Function Testing:")
print("="*40)

# Test name splitting
first, last = get_name_parts("John Doe Smith")
print(f"Name: '{first}' + '{last}'")

# Test temperature classification
print(f"25°C is: {classify_temperature(25)}")
print(f"77°F is: {classify_temperature(77, 'F')}")

# Test factorial
print(f"5! = {factorial(5)}")

# Test lambda with function
numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, lambda x: x**2)
doubled = apply_operation(numbers, lambda x: x*2)
print(f"Squared: {squared}")
print(f"Doubled: {doubled}")
```

### **Afternoon (2 hours): Password Validator Project**
**2:00-4:00 PM: Complete Password Validator**
- [ ] **Create:** `day04_password_validator.py`
- [ ] **Build:** Comprehensive password validation system:
```python
import re
import string
import secrets

class PasswordValidator:
    """Comprehensive password validation and generation system"""
    
    def __init__(self):
        self.common_passwords = [
            "password", "123456", "123456789", "qwerty", "abc123",
            "password123", "admin", "letmein", "welcome", "monkey",
            "dragon", "master", "hello", "login", "pass", "guest",
            "user", "root", "toor", "test", "qwerty123", "1234567890"
        ]
        
        self.common_patterns = [
            r"(.)\1{2,}",  # Repeated characters (aaa, 111)
            r"123456|654321|abcdef|fedcba",  # Sequential patterns
            r"qwerty|asdfgh|zxcvbn",  # Keyboard patterns
        ]
    
    def check_length(self, password, min_length=8):
        """Check if password meets minimum length requirement"""
        return len(password) >= min_length, f"Password should be at least {min_length} characters long"
    
    def check_character_types(self, password):
        """Check for different character types"""
        checks = []
        
        # Uppercase letters
        has_upper = any(c.isupper() for c in password)
        checks.append((has_upper, "Include uppercase letters (A-Z)"))
        
        # Lowercase letters
        has_lower = any(c.islower() for c in password)
        checks.append((has_lower, "Include lowercase letters (a-z)"))
        
        # Digits
        has_digits = any(c.isdigit() for c in password)
        checks.append((has_digits, "Include numbers (0-9)"))
        
        # Special characters
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        has_special = any(c in special_chars for c in password)
        checks.append((has_special, "Include special characters (!@#$%^&*)"))
        
        return checks
    
    def check_common_passwords(self, password):
        """Check if password is in common passwords list"""
        is_common = password.lower() in self.common_passwords
        return not is_common, "Avoid common passwords"
    
    def check_patterns(self, password):
        """Check for common weak patterns"""
        for pattern in self.common_patterns:
            if re.search(pattern, password.lower()):
                return False, "Avoid common patterns (123456, qwerty, repeated characters)"
        return True, "No common patterns detected"
    
    def check_personal_info(self, password, personal_info=None):
        """Check if password contains personal information"""
        if not personal_info:
            return True, "No personal information to check"
        
        password_lower = password.lower()
        for info in personal_info:
            if info.lower() in password_lower and len(info) > 2:
                return False, f"Avoid using personal information like '{info}'"
        
        return True, "No personal information detected"
    
    def calculate_strength_score(self, password, personal_info=None):
        """Calculate password strength score and provide feedback"""
        score = 0
        feedback = []
        
        # Length check
        length_ok, length_msg = self.check_length(password)
        if length_ok:
            score += 2
            if len(password) >= 12:
                score += 1  # Bonus for longer passwords
            if len(password) >= 16:
                score += 1  # Extra bonus for very long passwords
        else:
            feedback.append(f"❌ {length_msg}")
        
        # Character type checks
        char_checks = self.check_character_types(password)
        for passed, message in char_checks:
            if passed:
                score += 1
            else:
                feedback.append(f"❌ {message}")
        
        # Common password check
        not_common, common_msg = self.check_common_passwords(password)
        if not_common:
            score += 2
        else:
            feedback.append(f"❌ {common_msg}")
        
        # Pattern check
        no_patterns, pattern_msg = self.check_patterns(password)
        if no_patterns:
            score += 1
        else:
            feedback.append(f"❌ {pattern_msg}")
        
        # Personal info check
        no_personal, personal_msg = self.check_personal_info(password, personal_info)
        if no_personal:
            score += 1
        else:
            feedback.append(f"❌ {personal_msg}")
        
        return score, feedback
    
    def get_strength_level(self, score):
        """Convert numerical score to strength level"""
        if score <= 2:
            return "🔴 Very Weak", "This password is easily guessable"
        elif score <= 4:
            return "🟠 Weak", "This password needs significant improvement"
        elif score <= 6:
            return "🟡 Fair", "This password is okay but could be stronger"
        elif score <= 8:
            return "🟢 Strong", "This is a good password"
        else:
            return "🔵 Very Strong", "Excellent password! Very secure"
    
    def generate_password(self, length=12, include_symbols=True):
        """Generate a secure random password"""
        if length < 8:
            length = 8
        
        # Define character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?" if include_symbols else ""
        
        # Ensure at least one character from each set
        password = [
            secrets.choice(lowercase),
            secrets.choice(uppercase),
            secrets.choice(digits)
        ]
        
        if include_symbols:
            password.append(secrets.choice(symbols))
        
        # Fill the rest with random characters from all sets
        all_chars = lowercase + uppercase + digits + symbols
        for _ in range(length - len(password)):
            password.append(secrets.choice(all_chars))
        
        # Shuffle the password list
        secrets.SystemRandom().shuffle(password)
        
        return ''.join(password)
    
    def analyze_password(self, password, personal_info=None):
        """Complete password analysis"""
        score, feedback = self.calculate_strength_score(password, personal_info)
        strength_level, description = self.get_strength_level(score)
        
        return {
            'score': score,
            'max_score': 10,
            'strength_level': strength_level,
            'description': description,
            'feedback': feedback,
            'length': len(password)
        }

def main():
    """Main program loop"""
    validator = PasswordValidator()
    
    print("🔐" + "="*60 + "🔐")
    print("           ADVANCED PASSWORD SECURITY CHECKER")
    print("🔐" + "="*60 + "🔐")
    
    while True:
        print("\n🛡️  PASSWORD SECURITY MENU:")
        print("1. 🔍 Check password strength")
        print("2. 🎲 Generate secure password")
        print("3. 📚 Password security tips")
        print("4. 🚪 Quit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            check_password_strength(validator)
        elif choice == '2':
            generate_secure_password(validator)
        elif choice == '3':
            show_security_tips()
        elif choice == '4':
            print("\n👋 Stay secure! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select 1-4")

def check_password_strength(validator):
    """Check the strength of a user-provided password"""
    password = input("\n🔑 Enter password to check: ")
    
    if not password:
        print("❌ Password cannot be empty!")
        return
    
    # Optional: collect personal info for better analysis
    collect_personal = input("Include personal info check? (y/n): ").strip().lower()
    personal_info = []
    
    if collect_personal == 'y':
        print("Enter personal information to avoid in passwords (press Enter when done):")
        while True:
            info = input("Personal info (name, birthdate, etc.): ").strip()
            if not info:
                break
            personal_info.append(info)
    
    # Analyze password
    analysis = validator.analyze_password(password, personal_info if personal_info else None)
    
    # Display results
    print("\n" + "="*50)
    print("🔍 PASSWORD ANALYSIS RESULTS")
    print("="*50)
    print(f"Password: {'*' * len(password)}")
    print(f"Length: {analysis['length']} characters")
    print(f"Strength: {analysis['strength_level']}")
    print(f"Score: {analysis['score']}/{analysis['max_score']}")
    print(f"Assessment: {analysis['description']}")
    
    if analysis['feedback']:
        print(f"\n💡 SUGGESTIONS FOR IMPROVEMENT:")
        for suggestion in analysis['feedback']:
            print(f"   {suggestion}")
    else:
        print(f"\n✅ Great job! Your password meets all security criteria!")
    
    # Password strength visualization
    print(f"\nStrength meter: ", end="")
    filled_bars = int((analysis['score'] / analysis['max_score']) * 10)
    for i in range(10):
        if i < filled_bars:
            print("█", end="")
        else:
            print("░", end="")
    print(f" ({analysis['score']}/10)")

def generate_secure_password(validator):
    """Generate a secure password with user preferences"""
    print("\n🎲 SECURE PASSWORD GENERATOR")
    print("="*40)
    
    # Get user preferences
    try:
        length = int(input("Password length (minimum 8, recommended 12+): "))
        if length < 8:
            print("⚠️  Minimum length is 8. Setting to 8.")
            length = 8
    except ValueError:
        print("❌ Invalid input. Using default length of 12.")
        length = 12
    
    include_symbols = input("Include special characters? (y/n): ").strip().lower() == 'y'
    count = 1
    
    try:
        count = int(input("How many passwords to generate? (1-10): "))
        if count < 1 or count > 10:
            count = 1
    except ValueError:
        count = 1
    
    print(f"\n🔐 Generated {count} secure password(s):")
    print("-" * 50)
    
    for i in range(count):
        password = validator.generate_password(length, include_symbols)
        analysis = validator.analyze_password(password)
        
        print(f"Password {i+1}: {password}")
        print(f"Strength: {analysis['strength_level']} (Score: {analysis['score']}/10)")
        
        if i < count - 1:
            print()
    
    print("-" * 50)
    print("💡 TIP: Test your generated password with option 1 for detailed analysis!")

def show_security_tips():
    """Display password security best practices"""
    print("\n📚 PASSWORD SECURITY BEST PRACTICES")
    print("="*50)
    
    tips = [
        "🔸 Use at least 12 characters (longer is better)",
        "🔸 Mix uppercase, lowercase, numbers, and symbols",
        "🔸 Avoid common words and patterns",
        "🔸 Don't use personal information",
        "🔸 Use unique passwords for each account",
        "🔸 Consider using a password manager",
        "🔸 Enable two-factor authentication when possible",
        "🔸 Change passwords if they're compromised",
        "🔸 Don't share passwords or write them down",
        "🔸 Update passwords periodically for sensitive accounts"
    ]
    
    for tip in tips:
        print(tip)
    
    print(f"\n🎯 REMEMBER: A strong password is your first line of defense!")
    print(f"🛡️  The extra effort to create secure passwords pays off in protection!")

if __name__ == "__main__":
    main()
```

### **Evening (1 hour): Reading & Documentation**
**8:00-8:30 PM: Continue "Code"**
- [ ] **Resource:** "Code" by Charles Petzold
- [ ] **Read:** Chapter 4 (Anatomy of a Flashlight) - pages 46-60
- [ ] **Focus:** Understanding electrical circuits and switches
- [ ] **Notes:** Add to `day04_notes.txt`

**8:30-9:00 PM: Python Documentation Practice**
- [ ] **Resource:** Python Built-in Functions documentation
- [ ] **URL:** https://docs.python.org/3/library/functions.html
- [ ] **Practice:** Explore useful built-in functions:
```python
>>> # String and conversion functions
>>> abs(-42)
>>> round(3.14159, 2)
>>> len("Hello World")
>>> str(123)
>>> int("456")
>>> float("3.14")

>>> # Sequence functions
>>> max([1, 5, 3, 9, 2])
>>> min([1, 5, 3, 9, 2])
>>> sum([1, 2, 3, 4, 5])
>>> sorted([3, 1, 4, 1, 5])
>>> reversed([1, 2, 3, 4])

>>> # Advanced functions
>>> enumerate(['a', 'b', 'c'])
>>> list(enumerate(['a', 'b', 'c']))
>>> zip([1, 2, 3], ['a', 'b', 'c'])
>>> list(zip([1, 2, 3], ['a', 'b', 'c']))

>>> # Boolean and logical functions
>>> all([True, True, False])  # False
>>> any([True, True, False])  # True
>>> bool(0)  # False
>>> bool(42)  # True
```

### **Day 4 Deliverables:**
- [ ] `day04_functions.py` - Function fundamentals and advanced examples
- [ ] `day04_password_validator.py` - Complete password validation system
- [ ] `day04_notes.txt` - Notes from "Code" chapter 4
- [ ] Understanding of function parameters, return values, and scope
- [ ] Experience with object-oriented design principles

---

## **DAY 5: FILE HANDLING & DATA PERSISTENCE**

### **Morning (2 hours): File Operations**
**8:00-9:00 AM: File I/O Basics**
- [ ] **Resource:** "Python Crash Course" Chapter 10 (Files and Exceptions)
- [ ] **Read:** Pages 187-205 (reading/writing files, handling exceptions)
- [ ] **Create:** `day05_files/` directory for practice
- [ ] **Practice:** File operations:
```python
import os
from pathlib import Path

# Create practice directory
os.makedirs('day05_files', exist_ok=True)

# Basic file writing
def write_basic_file():
    """Demonstrate basic file writing"""
    content = """This is my first file!
I'm learning Python file operations.
This is line 3.
And this is the final line."""
    
    with open('day05_files/basic_file.txt', 'w') as file:
        file.write(content)
    print("✅ Created basic_file.txt")

# Basic file reading
def read_basic_file():
    """Demonstrate basic file reading"""
    try:
        with open('day05_files/basic_file.txt', 'r') as file:
            content = file.read()
            print("📖 File contents:")
            print(content)
    except FileNotFoundError:
        print("❌ File not found!")

# Reading line by line
def read_lines():
    """Read file line by line"""
    try:
        with open('day05_files/basic_file.txt', 'r') as file:
            print("📖 Reading line by line:")
            for line_num, line in enumerate(file, 1):
                print(f"Line {line_num}: {line.strip()}")
    except FileNotFoundError:
        print("❌ File not found!")

# Appending to files
def append_to_file():
    """Demonstrate appending to existing file"""
    additional_content = "\nThis line was added later!"
    
    with open('day05_files/basic_file.txt', 'a') as file:
        file.write(additional_content)
    print("✅ Appended content to file")

# Safe file operations with error handling
def safe_file_operations():
    """Demonstrate safe file operations"""
    def safe_write(filename, content):
        try:
            with open(filename, 'w') as file:
                file.write(content)
            return True, "File written successfully"
        except PermissionError:
            return False, "Permission denied"
        except Exception as e:
            return False, f"Error: {e}"
    
    def safe_read(filename):
        try:
            with open(filename, 'r') as file:
                return True, file.read()
        except FileNotFoundError:
            return False, "File not found"
        except PermissionError:
            return False, "Permission denied"
        except Exception as e:
            return False, f"Error: {e}"
    
    # Test safe operations
    success, message = safe_write('day05_files/safe_test.txt', "Safe file content")
    print(f"Write result: {message}")
    
    success, content = safe_read('day05_files/safe_test.txt')
    if success:
        print(f"Read result: {content}")
    else:
        print(f"Read error: {content}")

# Execute file operation demos
if __name__ == "__main__":
    print("🗂️  FILE OPERATIONS DEMO")
    print("="*30)
    
    write_basic_file()
    read_basic_file()
    print()
    read_lines()
    print()
    append_to_file()
    read_basic_file()  # Read again to see appended content
    print()
    safe_file_operations()
```

**9:00-10:00 AM: Working with Different File Formats**
- [ ] **Create:** `day05_file_formats.py`
- [ ] **Practice:** JSON, CSV, and text file handling:
```python
import json
import csv
from datetime import datetime

# Working with JSON files
def json_operations():
    """Demonstrate JSON file operations"""
    # Sample data
    student_data = {
        "students": [
            {"name": "Alice", "age": 20, "grades": [85, 92, 78, 90]},
            {"name": "Bob", "age": 22, "grades": [88, 76, 95, 82]},
            {"name": "Charlie", "age": 21, "grades": [92, 89, 94, 87]}
        ],
        "course": "Python Programming",
        "semester": "Spring 2024"
    }
    
    # Write JSON file
    with open('day05_files/students.json', 'w') as file:
        json.dump(student_data, file, indent=2)
    print("✅ Created students.json")
    
    # Read JSON file
    with open('day05_files/students.json', 'r') as file:
        loaded_data = json.load(file)
    
    print("📖 Loaded JSON data:")
    print(f"Course: {loaded_data['course']}")
    print(f"Semester: {loaded_data['semester']}")
    print(f"Number of students: {len(loaded_data['students'])}")
    
    for student in loaded_data['students']:
        avg_grade = sum(student['grades']) / len(student['grades'])
        print(f"  {student['name']} (age {student['age']}): avg {avg_grade:.1f}")

# Working with CSV files
def csv_operations():
    """Demonstrate CSV file operations"""
    # Sample expense data
    expenses = [
        ["Date", "Category", "Amount", "Description"],
        ["2024-01-15", "Food", "250.50", "Grocery shopping"],
        ["2024-01-16", "Transport", "45.00", "Bus ticket"],
        ["2024-01-17", "Entertainment", "120.00", "Movie tickets"],
        ["2024-01-18", "Food", "85.75", "Restaurant dinner"],
        ["2024-01-19", "Utilities", "1200.00", "Monthly rent"]
    ]
    
    # Write CSV file
    with open('day05_files/expenses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)
    print("✅ Created expenses.csv")
    
    # Read CSV file
    print("📖 Reading CSV data:")
    with open('day05_files/expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row_num, row in enumerate(reader):
            if row_num == 0:
                print(f"Headers: {', '.join(row)}")
            else:
                print(f"  {row[0]} | {row[1]} | {row[2]} CZK | {row[3]}")
    
    # Read CSV as dictionary
    print("\n📖 Reading CSV as dictionary:")
    with open('day05_files/expenses.csv', 'r') as file:
        reader = csv.DictReader(file)
        total = 0
        for row in reader:
            amount = float(row['Amount'])
            total += amount
            print(f"  {row['Category']}: {amount} CZK")
        print(f"Total expenses: {total} CZK")

# Working with configuration files
def config_file_operations():
    """Demonstrate configuration file handling"""
    # Create a simple config file
    config_content = """# Application Configuration
app_name = "My Python App"
version = "1.0.0"
debug_mode = true
max_users = 100
database_url = "localhost:5432"

# User Settings
theme = "dark"
language = "en"
auto_save = true
"""
    
    with open('day05_files/config.txt', 'w') as file:
        file.write(config_content)
    print("✅ Created config.txt")
    
    # Parse configuration file
    config = {}
    with open('day05_files/config.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('"')
                    
                    # Try to convert to appropriate type
                    if value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
                    elif value.isdigit():
                        value = int(value)
                    
                    config[key] = value
    
    print("📖 Parsed configuration:")
    for key, value in config.items():
        print(f"  {key}: {value} ({type(value).__name__})")

# Execute all demos
if __name__ == "__main__":
    print("📄 FILE FORMAT OPERATIONS")
    print("="*35)
    
    json_operations()
    print()
    csv_operations()
    print()
    config_file_operations()
```

### **Afternoon (2 hours): Personal Expense Tracker**
**2:00-4:00 PM: Complete Expense Tracker System**
- [ ] **Create:** `day05_expense_tracker.py`
- [ ] **Build:** Full-featured expense tracking application:
```python
import json
import csv
from datetime import datetime, timedelta
import os

class ExpenseTracker:
    """Complete expense tracking system with file persistence"""
    
    def __init__(self, data_file='day05_files/expenses_data.json'):
        self.data_file = data_file
        self.expenses = []
        self.categories = set()
        self.load_data()
    
    def load_data(self):
        """Load expenses from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    self.expenses = data.get('expenses', [])
                    self.categories = set(data.get('categories', []))
                print(f"✅ Loaded {len(self.expenses)} expenses from file")
            else:
                print("📝 Creating new expense database")
                self.save_data()  # Create the file
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            self.expenses = []
            self.categories = set()
    
    def save_data(self):
        """Save expenses to JSON file"""
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            
            data = {
                'expenses': self.expenses,
                'categories': list(self.categories),
                'last_updated': datetime.now().isoformat()
            }
            
            with open(self.data_file, 'w') as file:
                json.dump(data, file, indent=2)
            return True
        except Exception as e:
            print(f"❌ Error saving data: {e}")
            return False
    
    def add_expense(self, amount, category, description="", date=None):
        """Add a new expense"""
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        
        expense = {
            'id': len(self.expenses) + 1,
            'amount': float(amount),
            'category': category.title(),
            'description': description,
            'date': date,
            'timestamp': datetime.now().isoformat()
        }
        
        self.expenses.append(expense)
        self.categories.add(category.title())
        
        if self.save_data():
            print(f"✅ Added expense: {amount} CZK for {category}")
            return True
        return False
    
    def view_expenses(self, limit=None):
        """Display expenses with optional limit"""
        if not self.expenses:
            print("📝 No expenses recorded yet")
            return
        
        # Sort by date (newest first)
        sorted_expenses = sorted(self.expenses, key=lambda x: x['date'], reverse=True)
        
        if limit:
            sorted_expenses = sorted_expenses[:limit]
        
        print(f"\n💰 {'Recent ' if limit else ''}Expenses:")
        print("-" * 80)
        print(f"{'ID':<4} {'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<25}")
        print("-" * 80)
        
        total = 0
        for expense in sorted_expenses:
            print(f"{expense['id']:<4} {expense['date']:<12} {expense['category']:<15} "
                  f"{expense['amount']:<10.2f} {expense['description']:<25}")
            total += expense['amount']
        
        print("-" * 80)
        print(f"{'Total:':<31} {total:<10.2f} CZK")
        
        if limit and len(self.expenses) > limit:
            print(f"... and {len(self.expenses) - limit} more expenses")
    
    def view_by_category(self):
        """Display expenses grouped by category"""
        if not self.expenses:
            print("📝 No expenses recorded yet")
            return
        
        category_totals = {}
        for expense in self.expenses:
            category = expense['category']
            if category not in category_totals:
                category_totals[category] = {'total': 0, 'count': 0}
            category_totals[category]['total'] += expense['amount']
            category_totals[category]['count'] += 1
        
        total_amount = sum(data['total'] for data in category_totals.values())
        
        print(f"\n📊 Expenses by Category:")
        print("-" * 60)
        print(f"{'Category':<15} {'Count':<8} {'Total':<12} {'Percentage':<10}")
        print("-" * 60)
        
        # Sort by total amount (highest first)
        sorted_categories = sorted(category_totals.items(), 
                                 key=lambda x: x[1]['total'], reverse=True)
        
        for category, data in sorted_categories:
            percentage = (data['total'] / total_amount) * 100
            print(f"{category:<15} {data['count']:<8} {data['total']:<12.2f} {percentage:<10.1f}%")
        
        print("-" * 60)
        print(f"{'TOTAL:':<15} {len(self.expenses):<8} {total_amount:<12.2f} {'100.0%':<10}")
    
    def monthly_report(self, year=None, month=None):
        """Generate monthly expense report"""
        if year is None:
            year = datetime.now().year
        if month is None:
            month = datetime.now().month
        
        month_str = f"{year}-{month:02d}"
        monthly_expenses = [exp for exp in self.expenses if exp['date'].startswith(month_str)]
        
        if not monthly_expenses:
            print(f"📝 No expenses found for {month_str}")
            return
        
        total = sum(exp['amount'] for exp in monthly_expenses)
        avg_per_day = total / 30  # Approximate
        
        print(f"\n📅 Monthly Report for {month_str}:")
        print("="*50)
        print(f"Total Expenses: {total:.2f} CZK")
        print(f"Number of Transactions: {len(monthly_expenses)}")
        print(f"Average per Transaction: {total/len(monthly_expenses):.2f} CZK")
        print(f"Average per Day: {avg_per_day:.2f} CZK")
        
        # Category breakdown for the month
        category_totals = {}
        for expense in monthly_expenses:
            category = expense['category']
            category_totals[category] = category_totals.get(category, 0) + expense['amount']
        
        print(f"\nCategory Breakdown:")
        for category, amount in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total) * 100
            print(f"  {category}: {amount:.2f} CZK ({percentage:.1f}%)")
    
    def delete_expense(self, expense_id):
        """Delete an expense by ID"""
        for i, expense in enumerate(self.expenses):
            if expense['id'] == expense_id:
                deleted = self.expenses.pop(i)
                if self.save_data():
                    print(f"✅ Deleted expense: {deleted['amount']} CZK for {deleted['category']}")
                    return True
                return False
        print(f"❌ Expense with ID {expense_id} not found")
        return False
    
    def export_to_csv(self, filename=None):
        """Export all expenses to CSV file"""
        if not self.expenses:
            print("❌ No expenses to export")
            return False
        
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'day05_files/expenses_export_{timestamp}.csv'
        
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                # Write header
                writer.writerow(['ID', 'Date', 'Category', 'Amount', 'Description', 'Timestamp'])
                
                # Write expenses (sorted by date)
                sorted_expenses = sorted(self.expenses, key=lambda x: x['date'])
                for expense in sorted_expenses:
                    writer.writerow([
                        expense['id'],
                        expense['date'],
                        expense['category'],
                        expense['amount'],
                        expense['description'],
                        expense['timestamp']
                    ])
            
            print(f"✅ Exported {len(self.expenses)} expenses to {filename}")
            return True
        except Exception as e:
            print(f"❌ Error exporting to CSV: {e}")
            return False
    
    def import_from_csv(self, filename):
        """Import expenses from CSV file"""
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                imported_count = 0
                
                for row in reader:
                    # Add expense (skip ID to auto-generate)
                    self.add_expense(
                        amount=float(row['Amount']),
                        category=row['Category'],
                        description=row['Description'],
                        date=row['Date']
                    )
                    imported_count += 1
                
                print(f"✅ Imported {imported_count} expenses from {filename}")
                return True
        except Exception as e:
            print(f"❌ Error importing from CSV: {e}")
            return False
    
    def get_statistics(self):
        """Get comprehensive expense statistics"""
        if not self.expenses:
            return None
        
        amounts = [exp['amount'] for exp in self.expenses]
        total = sum(amounts)
        
        # Date range
        dates = [exp['date'] for exp in self.expenses]
        earliest = min(dates)
        latest = max(dates)
        
        # Days between first and last expense
        start_date = datetime.strptime(earliest, '%Y-%m-%d')
        end_date = datetime.strptime(latest, '%Y-%m-%d')
        days_span = (end_date - start_date).days + 1
        
        return {
            'total_expenses': len(self.expenses),
            'total_amount': total,
            'average_expense': total / len(self.expenses),
            'highest_expense': max(amounts),
            'lowest_expense': min(amounts),
            'categories_count': len(self.categories),
            'date_range': f"{earliest} to {latest}",
            'days_span': days_span,
            'daily_average': total / days_span if days_span > 0 else 0
        }

def main():
    """Main program loop"""
    tracker = ExpenseTracker()
    
    print("💰" + "="*60 + "💰")
    print("              PERSONAL EXPENSE TRACKER")
    print("💰" + "="*60 + "💰")
    
    while True:
        print(f"\n📊 EXPENSE TRACKER MENU:")
        print("1.  ➕ Add Expense")
        print("2.  👀 View All Expenses")
        print("3.  🔍 View Recent Expenses")
        print("4.  📊 View by Category")
        print("5.  📅 Monthly Report")
        print("6.  📈 Statistics")
        print("7.  🗑️  Delete Expense")
        print("8.  📤 Export to CSV")
        print("9.  📥 Import from CSV")
        print("10. 🚪 Quit")
        
        choice = input("\nSelect option (1-10): ").strip()
        
        if choice == '1':
            add_expense_interactive(tracker)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            try:
                limit = int(input("How many recent expenses to show? (default 10): ") or "10")
                tracker.view_expenses(limit)
            except ValueError:
                tracker.view_expenses(10)
        elif choice == '4':
            tracker.view_by_category()
        elif choice == '5':
            monthly_report_interactive(tracker)
        elif choice == '6':
            show_statistics(tracker)
        elif choice == '7':
            delete_expense_interactive(tracker)
        elif choice == '8':
            tracker.export_to_csv()
        elif choice == '9':
            import_csv_interactive(tracker)
        elif choice == '10':
            print(f"\n💾 Saving data...")
            if tracker.save_data():
                print("✅ Data saved successfully!")
            print("👋 Thanks for using Expense Tracker! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select 1-10")

def add_expense_interactive(tracker):
    """Interactive expense addition"""
    try:
        amount = float(input("💵 Enter amount (CZK): "))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")
        return
    
    print(f"\n📂 Available categories: {', '.join(sorted(tracker.categories))}")
    category = input("📂 Enter category: ").strip()
    if not category:
        print("❌ Category cannot be empty!")
        return
    
    description = input("📝 Enter description (optional): ").strip()
    
    date_input = input("📅 Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date_input:
        try:
            # Validate date format
            datetime.strptime(date_input, '%Y-%m-%d')
            date = date_input
        except ValueError:
            print("❌ Invalid date format! Using today's date.")
            date = None
    else:
        date = None
    
    tracker.add_expense(amount, category, description, date)

def monthly_report_interactive(tracker):
    """Interactive monthly report generation"""
    current_year = datetime.now().year
    current_month = datetime.now().month
    
    year_input = input(f"📅 Enter year (default {current_year}): ").strip()
    month_input = input(f"📅 Enter month (1-12, default {current_month}): ").strip()
    
    try:
        year = int(year_input) if year_input else current_year
        month = int(month_input) if month_input else current_month
        
        if month < 1 or month > 12:
            print("❌ Invalid month! Using current month.")
            month = current_month
            
        tracker.monthly_report(year, month)
    except ValueError:
        print("❌ Invalid input! Using current date.")
        tracker.monthly_report()

def show_statistics(tracker):
    """Display comprehensive statistics"""
    stats = tracker.get_statistics()
    
    if not stats:
        print("📝 No expense data available for statistics")
        return
    
    print(f"\n📈 EXPENSE STATISTICS:")
    print("="*40)
    print(f"Total Expenses: {stats['total_expenses']}")
    print(f"Total Amount: {stats['total_amount']:.2f} CZK")
    print(f"Average Expense: {stats['average_expense']:.2f} CZK")
    print(f"Highest Expense: {stats['highest_expense']:.2f} CZK")
    print(f"Lowest Expense: {stats['lowest_expense']:.2f} CZK")
    print(f"Categories Used: {stats['categories_count']}")
    print(f"Date Range: {stats['date_range']}")
    print(f"Days Tracked: {stats['days_span']}")
    print(f"Daily Average: {stats['daily_average']:.2f} CZK")

def delete_expense_interactive(tracker):
    """Interactive expense deletion"""
    tracker.view_expenses(10)  # Show recent expenses
    
    try:
        expense_id = int(input("\n🗑️  Enter expense ID to delete: "))
        confirm = input(f"Are you sure you want to delete expense {expense_id}? (y/n): ")
        if confirm.lower() == 'y':
            tracker.delete_expense(expense_id)
    except ValueError:
        print("❌ Invalid ID! Please enter a number.")

def import_csv_interactive(tracker):
    """Interactive CSV import"""
    filename = input("📥 Enter CSV filename to import: ").strip()
    if filename and os.path.exists(filename):
        tracker.import_from_csv(filename)
    else:
        print("❌ File not found!")

if __name__ == "__main__":
    main()
```

### **Evening (1 hour): Reading & JSON Practice**
**8:00-8:30 PM: Continue "Code"**
- [ ] **Resource:** "Code" by Charles Petzold
- [ ] **Read:** Chapter 5 (Seeing Around Corners) - pages 61-75
- [ ] **Focus:** Understanding relays and how they enable complex logic
- [ ] **Notes:** Add to `day05_notes.txt`

**8:30-9:00 PM: JSON and Data Formats**
- [ ] **Resource:** Python JSON documentation
- [ ] **URL:** https://docs.python.org/3/library/json.html
- [ ] **Practice:** JSON operations in Python shell:
```python
>>> import json
>>> 
>>> # Basic JSON operations
>>> data = {"name": "John", "age": 30, "skills": ["Python", "JavaScript"]}
>>> json_string = json.dumps(data)
>>> print(json_string)
>>> 
>>> # Pretty printing
>>> print(json.dumps(data, indent=2))
>>> 
>>> # Parsing JSON
>>> parsed = json.loads(json_string)
>>> print(parsed['name'])
>>> 
>>> # Working with nested data
>>> complex_data = {
...     "users": [
...         {"id": 1, "name": "Alice", "active": True},
...         {"id": 2, "name": "Bob", "active": False}
...     ],
...     "total": 2
... }
>>> print(json.dumps(complex_data, indent=2))
```

### **Day 5 Deliverables:**
- [ ] `day05_files/` directory with all practice files
- [ ] `day05_files.py` - File operations demonstration
- [ ] `day05_file_formats.py` - JSON, CSV, and config file handling
- [ ] `day05_expense_tracker.py` - Complete expense tracking system
- [ ] `day05_notes.txt` - Notes from "Code" chapter 5
- [ ] Working expense tracker with data persistence
- [ ] Understanding of file I/O, JSON, CSV, and error handling

---

## **DAY 6: TEXT PROCESSING & STRING MANIPULATION**

### **Morning (2 hours): Advanced String Operations**
**8:00-9:00 AM: String Methods Deep Dive**
- [ ] **Resource:** "Python Crash Course" Chapter 2 review + Python documentation
- [ ] **Create:** `day06_strings.py`
- [ ] **Practice:** Advanced string manipulation:
```python
# Advanced string operations
text = "  Python Programming is Amazing!  "

print("Original text:", repr(text))
print("Length:", len(text))

# Cleaning operations
cleaned = text.strip()
print("Stripped:", repr(cleaned))
print("Lowercase:", cleaned.lower())
print("Uppercase:", cleaned.upper())
print("Title case:", cleaned.title())
print("Swap case:", cleaned.swapcase())

# Checking string properties
print("Is alphabetic:", cleaned.isalpha())
print("Is alphanumeric:", cleaned.replace(" ", "").isalnum())
print("Is digit:", "123".isdigit())
print("Is lowercase:", cleaned.islower())
print("Is uppercase:", cleaned.isupper())
print("Is title:", cleaned.istitle())

# String searching
search_text = "Python Programming is Amazing!"
print("Find 'Python':", search_text.find("Python"))
print("Find 'Java':", search_text.find("Java"))  # Returns -1 if not found
print("Count 'a':", search_text.count('a'))
print("Starts with 'Python':", search_text.startswith("Python"))
print("Ends with '!':", search_text.endswith("!"))

# String replacement and splitting
print("Replace 'Python' with 'Java':", search_text.replace("Python", "Java"))
print("Replace first 'a' with '@':", search_text.replace('a', '@', 1))

words = search_text.split()
print("Split by space:", words)
print("Join with '-':", "-".join(words))

# String formatting examples
name = "Alice"
age = 25
score = 87.5

# Different formatting methods
print(f"f-string: {name} is {age} years old and scored {score:.1f}%")
print("format(): {} is {} years old and scored {:.1f}%".format(name, age, score))
print("% formatting: %s is %d years old and scored %.1f%%" % (name, age, score))

# Advanced formatting
pi = 3.14159
print(f"Pi rounded: {pi:.2f}")
print(f"Pi with padding: {pi:8.2f}")
print(f"Left aligned: '{name:<10}'")
print(f"Right aligned: '{name:>10}'")
print(f"Center aligned: '{name:^10}'")
```

**9:00-10:00 AM: Regular Expressions Introduction**
- [ ] **Learn:** Basic pattern matching with `re` module:
```python
import re

# Basic pattern matching
text = "My phone number is 123-456-7890 and email is john@example.com"

# Finding patterns
phone_pattern = r'\d{3}-\d{3}-\d{4}'
email_pattern = r'\w+@\w+\.\w+'

phone = re.search(phone_pattern, text)
email = re.search(email_pattern, text)

if phone:
    print(f"Phone found: {phone.group()}")
if email:
    print(f"Email found: {email.group()}")

# Finding all matches
numbers = re.findall(r'\d+', "I have 5 apples and 3 oranges")
print(f"All numbers: {numbers}")

# Replacing patterns
clean_text = re.sub(r'\d+', 'X', "Call 123-456-7890 or 987-654-3210")
print(f"Numbers replaced: {clean_text}")

# Splitting by pattern
parts = re.split(r'[,;]', "apple,banana;orange,grape")
print(f"Split by comma or semicolon: {parts}")
```

### **Afternoon (2 hours): Text Analyzer Project**
**2:00-4:00 PM: Complete Text Analysis Tool**
- [ ] **Create:** `day06_text_analyzer.py`
- [ ] **Build:** Comprehensive text analysis application:
```python
import re
import string
from collections import Counter
from datetime import datetime

class TextAnalyzer:
    """Comprehensive text analysis tool"""
    
    def __init__(self):
        self.text = ""
        self.analysis_results = {}
    
    def load_text(self, text):
        """Load text for analysis"""
        self.text = text
        self.analysis_results = {}
        return len(text) > 0
    
    def load_from_file(self, filename):
        """Load text from file"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.text = file.read()
                self.analysis_results = {}
                print(f"✅ Loaded text from {filename}")
                return True
        except FileNotFoundError:
            print(f"❌ File {filename} not found")
            return False
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            return False
    
    def basic_statistics(self):
        """Calculate basic text statistics"""
        if not self.text:
            return None
        
        # Character counts
        total_chars = len(self.text)
        chars_no_spaces = len(self.text.replace(' ', ''))
        whitespace_chars = total_chars - chars_no_spaces
        
        # Word and sentence counts
        words = self.text.split()
        word_count = len(words)
        
        # Sentence count (approximate)
        sentence_endings = ['.', '!', '?']
        sentence_count = sum(self.text.count(ending) for ending in sentence_endings)
        
        # Paragraph count
        paragraphs = [p.strip() for p in self.text.split('\n\n') if p.strip()]
        paragraph_count = len(paragraphs)
        
        # Line count
        lines = self.text.split('\n')
        line_count = len(lines)
        
        return {
            'total_characters': total_chars,
            'characters_no_spaces': chars_no_spaces,
            'whitespace_characters': whitespace_chars,
            'word_count': word_count,
            'sentence_count': sentence_count,
            'paragraph_count': paragraph_count,
            'line_count': line_count,
            'average_word_length': sum(len(word.strip(string.punctuation)) for word in words) / word_count if word_count > 0 else 0,
            'average_sentence_length': word_count / sentence_count if sentence_count > 0 else 0
        }
    
    def character_frequency(self):
        """Analyze character frequency"""
        if not self.text:
            return None
        
        # Count all characters
        char_count = Counter(self.text.lower())
        
        # Separate into categories
        letters = {char: count for char, count in char_count.items() if char.isalpha()}
        digits = {char: count for char, count in char_count.items() if char.isdigit()}
        punctuation = {char: count for char, count in char_count.items() if char in string.punctuation}
        whitespace = {char: count for char, count in char_count.items() if char.isspace()}
        
        return {
            'all_characters': dict(char_count.most_common()),
            'letters': dict(sorted(letters.items(), key=lambda x: x[1], reverse=True)),
            'digits': dict(sorted(digits.items(), key=lambda x: x[1], reverse=True)),
            'punctuation': dict(sorted(punctuation.items(), key=lambda x: x[1], reverse=True)),
            'whitespace': dict(sorted(whitespace.items(), key=lambda x: x[1], reverse=True))
        }
    
    def word_frequency(self, top_n=10):
        """Analyze word frequency"""
        if not self.text:
            return None
        
        # Clean and split words
        words = re.findall(r'\b\w+\b', self.text.lower())
        word_count = Counter(words)
        
        # Common English stop words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
            'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
            'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must',
            'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them',
            'my', 'your', 'his', 'her', 'its', 'our', 'their', 'this', 'that', 'these', 'those'
        }
        
        # Filter out stop words
        content_words = {word: count for word, count in word_count.items() 
                        if word not in stop_words and len(word) > 2}
        
        return {
            'total_unique_words': len(word_count),
            'top_words_all': dict(word_count.most_common(top_n)),
            'top_content_words': dict(Counter(content_words).most_common(top_n)),
            'word_length_distribution': self._word_length_distribution(words)
        }
    
    def _word_length_distribution(self, words):
        """Calculate distribution of word lengths"""
        lengths = [len(word) for word in words]
        length_count = Counter(lengths)
        return dict(sorted(length_count.items()))
    
    def readability_analysis(self):
        """Calculate readability metrics"""
        if not self.text:
            return None
        
        stats = self.basic_statistics()
        if not stats:
            return None
        
        # Flesch Reading Ease Score (approximate)
        avg_sentence_length = stats['average_sentence_length']
        avg_syllables_per_word = 1.5  # Approximation
        
        flesch_score = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syllables_per_word)
        
        # Flesch-Kincaid Grade Level (approximate)
        grade_level = (0.39 * avg_sentence_length) + (11.8 * avg_syllables_per_word) - 15.59
        
        # Reading difficulty interpretation
        if flesch_score >= 90:
            difficulty = "Very Easy"
        elif flesch_score >= 80:
            difficulty = "Easy"
        elif flesch_score >= 70:
            difficulty = "Fairly Easy"
        elif flesch_score >= 60:
            difficulty = "Standard"
        elif flesch_score >= 50:
            difficulty = "Fairly Difficult"
        elif flesch_score >= 30:
            difficulty = "Difficult"
        else:
            difficulty = "Very Difficult"
        
        return {
            'flesch_reading_ease': max(0, min(100, flesch_score)),
            'flesch_kincaid_grade': max(0, grade_level),
            'difficulty_level': difficulty,
            'estimated_reading_time_minutes': stats['word_count'] / 200  # 200 words per minute average
        }
    
    def find_patterns(self):
        """Find common patterns in text"""
        if not self.text:
            return None
        
        patterns = {
            'emails': re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', self.text),
            'phone_numbers': re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', self.text),
            'urls': re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.text),
            'dates': re.findall(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b', self.text),
            'numbers': re.findall(r'\b\d+\.?\d*\b', self.text),
            'capitalized_words': re.findall(r'\b[A-Z][a-z]+\b', self.text),
            'all_caps_words': re.findall(r'\b[A-Z]{2,}\b', self.text)
        }
        
        return {key: list(set(value)) for key, value in patterns.items()}
    
    def generate_report(self):
        """Generate comprehensive analysis report"""
        if not self.text:
            return "No text loaded for analysis"
        
        report = []
        report.append("📊 TEXT ANALYSIS REPORT")
        report.append("=" * 50)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Basic Statistics
        stats = self.basic_statistics()
        if stats:
            report.append("📈 BASIC STATISTICS:")
            report.append("-" * 20)
            report.append(f"Total Characters: {stats['total_characters']:,}")
            report.append(f"Characters (no spaces): {stats['characters_no_spaces']:,}")
            report.append(f"Words: {stats['word_count']:,}")
            report.append(f"Sentences: {stats['sentence_count']:,}")
            report.append(f"Paragraphs: {stats['paragraph_count']:,}")
            report.append(f"Lines: {stats['line_count']:,}")
            report.append(f"Average Word Length: {stats['average_word_length']:.1f} characters")
            report.append(f"Average Sentence Length: {stats['average_sentence_length']:.1f} words")
            report.append("")
        
        # Readability
        readability = self.readability_analysis()
        if readability:
            report.append("📖 READABILITY ANALYSIS:")
            report.append("-" * 25)
            report.append(f"Reading Difficulty: {readability['difficulty_level']}")
            report.append(f"Flesch Reading Ease: {readability['flesch_reading_ease']:.1f}")
            report.append(f"Flesch-Kincaid Grade: {readability['flesch_kincaid_grade']:.1f}")
            report.append(f"Estimated Reading Time: {readability['estimated_reading_time_minutes']:.1f} minutes")
            report.append("")
        
        # Word Frequency
        word_freq = self.word_frequency()
        if word_freq:
            report.append("🔤 WORD FREQUENCY:")
            report.append("-" * 18)
            report.append(f"Unique Words: {word_freq['total_unique_words']:,}")
            report.append("Top 10 Most Common Words:")
            for word, count in list(word_freq['top_words_all'].items())[:10]:
                report.append(f"  {word}: {count}")
            report.append("")
            
            report.append("Top 10 Content Words (excluding common words):")
            for word, count in list(word_freq['top_content_words'].items())[:10]:
                report.append(f"  {word}: {count}")
            report.append("")
        
        # Character Frequency
        char_freq = self.character_frequency()
        if char_freq:
            report.append("🔠 CHARACTER FREQUENCY:")
            report.append("-" * 22)
            report.append("Most Common Letters:")
            for char, count in list(char_freq['letters'].items())[:10]:
                report.append(f"  '{char}': {count}")
            report.append("")
        
        # Patterns
        patterns = self.find_patterns()
        if patterns:
            report.append("🔍 PATTERNS FOUND:")
            report.append("-" * 17)
            for pattern_type, matches in patterns.items():
                if matches:
                    report.append(f"{pattern_type.replace('_', ' ').title()}: {len(matches)} found")
                    for match in matches[:5]:  # Show first 5
                        report.append(f"  {match}")
                    if len(matches) > 5:
                        report.append(f"  ... and {len(matches) - 5} more")
                    report.append("")
        
        return "\n".join(report)
    
    def save_report(self, filename=None):
        """Save analysis report to file"""
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'day06_files/text_analysis_report_{timestamp}.txt'
        
        report = self.generate_report()
        
        try:
            import os
            os.makedirs('day06_files', exist_ok=True)
            
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(report)
            print(f"✅ Report saved to {filename}")
            return True
        except Exception as e:
            print(f"❌ Error saving report: {e}")
            return False

def main():
    """Main program for text analyzer"""
    analyzer = TextAnalyzer()
    
    print("📊" + "="*50 + "📊")
    print("              TEXT ANALYZER TOOL")
    print("📊" + "="*50 + "📊")
    
    while True:
        print("\n📝 TEXT ANALYZER MENU:")
        print("1. 📥 Load text from input")
        print("2. 📁 Load text from file") 
        print("3. 📊 Show basic statistics")
        print("4. 🔤 Show word frequency")
        print("5. 🔠 Show character frequency")
        print("6. 📖 Show readability analysis")
        print("7. 🔍 Find patterns")
        print("8. 📋 Generate full report")
        print("9. 💾 Save report to file")
        print("10. 🚪 Quit")
        
        choice = input("\nSelect option (1-10): ").strip()
        
        if choice == '1':
            text = input("\n📝 Enter or paste your text:\n")
            if analyzer.load_text(text):
                print("✅ Text loaded successfully!")
            else:
                print("❌ No text provided!")
                
        elif choice == '2':
            filename = input("📁 Enter filename: ").strip()
            analyzer.load_from_file(filename)
            
        elif choice == '3':
            stats = analyzer.basic_statistics()
            if stats:
                print("\n📈 BASIC STATISTICS:")
                print("-" * 20)
                for key, value in stats.items():
                    formatted_key = key.replace('_', ' ').title()
                    if isinstance(value, float):
                        print(f"{formatted_key}: {value:.2f}")
                    else:
                        print(f"{formatted_key}: {value:,}")
            else:
                print("❌ No text loaded!")
                
        elif choice == '4':
            word_freq = analyzer.word_frequency()
            if word_freq:
                print(f"\n🔤 WORD FREQUENCY (Top 15):")
                print("-" * 30)
                print("All Words:")
                for word, count in list(word_freq['top_words_all'].items())[:15]:
                    print(f"  {word}: {count}")
                print("\nContent Words (excluding common words):")
                for word, count in list(word_freq['top_content_words'].items())[:15]:
                    print(f"  {word}: {count}")
            else:
                print("❌ No text loaded!")
                
        elif choice == '5':
            char_freq = analyzer.character_frequency()
            if char_freq:
                print("\n🔠 CHARACTER FREQUENCY:")
                print("-" * 22)
                print("Letters:")
                for char, count in list(char_freq['letters'].items())[:10]:
                    print(f"  '{char}': {count}")
                if char_freq['digits']:
                    print("Digits:")
                    for char, count in char_freq['digits'].items():
                        print(f"  '{char}': {count}")
            else:
                print("❌ No text loaded!")
                
        elif choice == '6':
            readability = analyzer.readability_analysis()
            if readability:
                print("\n📖 READABILITY ANALYSIS:")
                print("-" * 25)
                print(f"Difficulty Level: {readability['difficulty_level']}")
                print(f"Flesch Reading Ease: {readability['flesch_reading_ease']:.1f}/100")
                print(f"Flesch-Kincaid Grade: {readability['flesch_kincaid_grade']:.1f}")
                print(f"Estimated Reading Time: {readability['estimated_reading_time_minutes']:.1f} minutes")
            else:
                print("❌ No text loaded!")
                
        elif choice == '7':
            patterns = analyzer.find_patterns()
            if patterns:
                print("\n🔍 PATTERNS FOUND:")
                print("-" * 17)
                for pattern_type, matches in patterns.items():
                    if matches:
                        print(f"{pattern_type.replace('_', ' ').title()}: {len(matches)} found")
                        for match in matches[:3]:
                            print(f"  {match}")
                        if len(matches) > 3:
                            print(f"  ... and {len(matches) - 3} more")
                        print()
            else:
                print("❌ No text loaded!")
                
        elif choice == '8':
            report = analyzer.generate_report()
            print("\n" + report)
            
        elif choice == '9':
            if analyzer.text:
                analyzer.save_report()
            else:
                print("❌ No text loaded!")
                
        elif choice == '10':
            print("👋 Thanks for using Text Analyzer! Goodbye!")
            break
            
        else:
            print("❌ Invalid choice! Please select 1-10")

if __name__ == "__main__":
    main()
```

### **Evening (1 hour): Reading & Regex Practice**
**8:00-8:30 PM: Continue "Code"**
- [ ] **Resource:** "Code" by Charles Petzold
- [ ] **Read:** Chapter 6 (Telegraphs and Relays) - pages 76-90
- [ ] **Focus:** Understanding how telegraphs work and relay logic
- [ ] **Notes:** Add to `day06_notes.txt`

**8:30-9:00 PM: Regular Expressions Practice**
- [ ] **Resource:** Python `re` module documentation
- [ ] **URL:** https://docs.python.org/3/library/re.html
- [ ] **Practice:** Pattern matching:
```python
>>> import re
>>> 
>>> # Basic patterns
>>> text = "My phone is 123-456-7890 and email is john@test.com"
>>> re.findall(r'\d+', text)  # Find all numbers
>>> re.findall(r'\w+@\w+\.\w+', text)  # Find emails
>>> 
>>> # Character classes
>>> re.findall(r'[aeiou]', "hello world")  # Vowels
>>> re.findall(r'[A-Z]', "Hello World")  # Uppercase
>>> re.findall(r'\b\w{5}\b', "These are some words")  # 5-letter words
>>> 
>>> # Substitution
>>> re.sub(r'\d+', 'XXX', text)  # Replace numbers
>>> re.sub(r'(\w+)@(\w+)', r'\1 AT \2', text)  # Replace email format
```

### **Day 6 Deliverables:**
- [ ] `day06_strings.py` - Advanced string operations
- [ ] `day06_text_analyzer.py` - Complete text analysis tool
- [ ] `day06_files/` directory with analysis reports
- [ ] `day06_notes.txt` - Notes from "Code" chapter 6
- [ ] Understanding of string methods, regex basics, and text processing

---

## **DAY 7: WEEK 1 REVIEW & PORTFOLIO SETUP**

### **Morning (2 hours): Git & GitHub Setup**
**8:00-9:00 AM: Git Fundamentals**
- [ ] **Resource:** "Git Tutorial for Beginners" (Programming with Mosh - YouTube)
- [ ] **Practice:** Essential Git commands:
```bash
# Navigate to your projects directory
cd ~/python-projects/week1

# Initialize git repository
git init

# Configure git (if not done already)
git config --global user.name "Your Name"
git config --global user.email "your.email@gmail.com"

# Check status
git status

# Add files to staging area
git add .

# Create first commit
git commit -m "Initial commit: Week 1 Python projects"

# Check commit history
git log --oneline

# Create .gitignore file
echo "__pycache__/" > .gitignore
echo "*.pyc" >> .gitignore
echo ".vscode/" >> .gitignore
echo "day*/files/" >> .gitignore

# Add and commit .gitignore
git add .gitignore
git commit -m "Add .gitignore file"
```

**9:00-10:00 AM: GitHub Repository Creation**
- [ ] **Create:** Professional GitHub repository
- [ ] **Setup:** Connect local repo to GitHub:
```bash
# Create repository on GitHub first (through website)
# Then connect your local repo

# Add remote origin
git remote add origin https://github.com/yourusername/python-learning-journey.git

# Push to GitHub
git branch -M main
git push -u origin main

# Create README.md
cat > README.md << 'EOF'
# Python Learning Journey 🐍

## About
This repository documents my journey learning Python programming to become a software developer in Czech Republic.

## Week 1 Projects
- **Day 1**: Calculator with menu system
- **Day 2**: Shopping list & student grade manager
- **Day 3**: Number guessing game with statistics
- **Day 4**: Password validator with security analysis
- **Day 5**: Expense tracker with file persistence
- **Day 6**: Text analyzer with comprehensive reporting
- **Day 7**: Portfolio setup and Git workflow

## Skills Learned
- Python fundamentals (variables, functions, control flow)
- File I/O and data persistence
- Object-oriented programming basics
- String manipulation and text processing
- Error handling and input validation
- Git version control

## Goals
- [ ] Complete 12-month Python roadmap
- [ ] Build impressive portfolio
- [ ] Land Python developer job in Czech Republic

## Contact
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
EOF

# Add and commit README
git add README.md
git commit -m "Add README with project overview"
git push
```

### **Afternoon (2 hours): Week 1 Project Refinement**
**2:00-3:00 PM: Code Review & Improvement**
- [ ] **Review:** All Week 1 projects for code quality
- [ ] **Create:** `day07_code_improvements.py`
- [ ] **Refactor:** Previous projects with improvements:
```python
# Code improvement checklist and examples

def improved_calculator():
    """
    Improved version of Day 1 calculator with better error handling
    """
    import math
    
    def safe_divide(x, y):
        """Safe division with error handling"""
        try:
            return x / y
        except ZeroDivisionError:
            return "Error: Cannot divide by zero"
    
    def safe_sqrt(x):
        """Safe square root with error handling"""
        try:
            if x < 0:
                return "Error: Cannot calculate square root of negative number"
            return math.sqrt(x)
        except (TypeError, ValueError):
            return "Error: Invalid input for square root"
    
    def get_number_input(prompt):
        """Get validated number input from user"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("❌ Please enter a valid number!")
    
    operations = {
        '1': ('Addition (+)', lambda x, y: x + y),
        '2': ('Subtraction (-)', lambda x, y: x - y),
        '3': ('Multiplication (*)', lambda x, y: x * y),
        '4': ('Division (/)', safe_divide),
        '5': ('Power (^)', lambda x, y: x ** y),
        '6': ('Square Root (√)', lambda x, _: safe_sqrt(x)),
        '7': ('Logarithm (log)', lambda x, _: math.log(x) if x > 0 else "Error: Logarithm undefined for non-positive numbers")
    }
    
    print("🧮 IMPROVED CALCULATOR")
    print("=" * 30)
    
    while True:
        print("\nOperations:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("8. Quit")
        
        choice = input("\nChoose operation (1-8): ").strip()
        
        if choice == '8':
            print("Calculator closed. Goodbye!")
            break
        
        if choice in operations:
            operation_name, operation_func = operations[choice]
            
            num1 = get_number_input("Enter first number: ")
            
            if choice != '6' and choice != '7':  # Operations requiring two numbers
                num2 = get_number_input("Enter second number: ")
            else:
                num2 = None
            
            result = operation_func(num1, num2)
            print(f"Result: {result}")
        else:
            print("❌ Invalid choice! Please select 1-8.")

def code_quality_checklist():
    """
    Demonstrate code quality best practices learned this week
    """
    
    # 1. Use descriptive variable names
    user_age = 25  # Good
    # a = 25  # Bad
    
    # 2. Add docstrings to functions
    def calculate_bmi(weight_kg, height_m):
        """
        Calculate Body Mass Index.
        
        Args:
            weight_kg (float): Weight in kilograms
            height_m (float): Height in meters
        
        Returns:
            tuple: (bmi_value, category_string)
        """
        bmi = weight_kg / (height_m ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        return round(bmi, 1), category
    
    # 3. Use constants for magic numbers
    MIN_PASSWORD_LENGTH = 8
    MAX_LOGIN_ATTEMPTS = 3
    
    # 4. Handle errors gracefully
    def safe_file_read(filename):
        """Safely read file with proper error handling"""
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File {filename} not found")
            return None
        except PermissionError:
            print(f"Permission denied for {filename}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    # 5. Use list comprehensions when appropriate
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_squares = [x**2 for x in numbers if x % 2 == 0]  # Good
    
    # Instead of:
    # even_squares = []
    # for x in numbers:
    #     if x % 2 == 0:
    #         even_squares.append(x**2)
    
    # 6. Use f-strings for formatting
    name = "Alice"
    score = 95.5
    message = f"{name} scored {score:.1f}%"  # Good
    # message = name + " scored " + str(score) + "%"  # Bad
    
    print("✅ Code quality examples demonstrated")
    return True

def create_project_documentation():
    """Create documentation for all Week 1 projects"""
    
    documentation = {
        'day01_calculator': {
            'description': 'Interactive calculator with basic arithmetic operations',
            'features': ['Addition, subtraction, multiplication, division', 'Menu-driven interface', 'Error handling'],
            'files': ['calculator_basic.py', 'calculator_advanced.py']
        },
        'day02_data_structures': {
            'description': 'Programs demonstrating lists and dictionaries',
            'features': ['Shopping list manager', 'Student grade tracker', 'CRUD operations'],
            'files': ['day02_lists.py', 'day02_student_grades.py']
        },
        'day03_control_flow': {
            'description': 'Number guessing game with statistics',
            'features': ['Multiple difficulty levels', 'Game statistics', 'User-friendly interface'],
            'files': ['day03_guessing_game.py']
        },
        'day04_functions': {
            'description': 'Password validation system',
            'features': ['Strength analysis', 'Security recommendations', 'Password generation'],
            'files': ['day04_password_validator.py']
        },
        'day05_file_handling': {
            'description': 'Expense tracking application',
            'features': ['Data persistence', 'JSON/CSV export', 'Reporting'],
            'files': ['day05_expense_tracker.py']
        },
        'day06_text_processing': {
            'description': 'Comprehensive text analysis tool',
            'features': ['Text statistics', 'Readability analysis', 'Pattern detection'],
            'files': ['day06_text_analyzer.py']
        }
    }
    
    # Create documentation file
    doc_content = "# Week 1 Project Documentation\n\n"
    
    for project, details in documentation.items():
        doc_content += f"## {project.replace('_', ' ').title()}\n\n"
        doc_content += f"**Description:** {details['description']}\n\n"
        doc_content += f"**Key Features:**\n"
        for feature in details['features']:
            doc_content += f"- {feature}\n"
        doc_content += f"\n**Files:**\n"
        for file in details['files']:
            doc_content += f"- `{file}`\n"
        doc_content += "\n---\n\n"
    
    try:
        with open('day07_files/project_documentation.md', 'w') as file:
            file.write(doc_content)
        print("✅ Project documentation created")
        return True
    except Exception as e:
        print(f"❌ Error creating documentation: {e}")
        return False

if __name__ == "__main__":
    print("🔧 CODE IMPROVEMENT SESSION")
    print("=" * 35)
    
    # Demonstrate improved calculator
    print("\n1. Testing improved calculator...")
    # improved_calculator()  # Uncomment to test
    
    # Show code quality examples
    print("\n2. Code quality checklist...")
    code_quality_checklist()
    
    # Create project documentation
    print("\n3. Creating project documentation...")
    import os
    os.makedirs('day07_files', exist_ok=True)
    create_project_documentation()
```

**3:00-4:00 PM: Portfolio Website Creation**
- [ ] **Create:** `day07_portfolio.html`
- [ ] **Build:** Simple portfolio webpage:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Learning Journey - Week 1</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 40px;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }
        
        .header h1 {
            color: #2c3e50;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .header .subtitle {
            color: #7f8c8d;
            font-size: 1.2em;
            margin-bottom: 20px;
        }
        
        .stats {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 20px;
        }
        
        .stat-item {
            text-align: center;
        }
        
        .stat-number {
            font-size: 2em;
            font-weight: bold;
            color: #3498db;
        }
        
        .stat-label {
            color: #7f8c8d;
            text-transform: uppercase;
            font-size: 0.9em;
        }
        
        .projects {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }
        
        .project-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
        }
        
        .project-card h3 {
            color: #2c3e50;
            margin-bottom: 15px;
            font-size: 1.4em;
        }
        
        .project-description {
            color: #555;
            margin-bottom: 15px;
            line-height: 1.5;
        }
        
        .project-features {
            list-style: none;
            margin-bottom: 20px;
        }
        
        .project-features li {
            color: #27ae60;
            margin-bottom: 5px;
            position: relative;
            padding-left: 20px;
        }
        
        .project-features li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #27ae60;
            font-weight: bold;
        }
        
        .project-tech {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }
        
        .tech-tag {
            background: #3498db;
            color: white;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: 500;
        }
        
        .footer {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            margin-top: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }
        
        .contact-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        
        .contact-links a {
            color: #3498db;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }
        
        .contact-links a:hover {
            color: #2980b9;
        }
        
        @media (max-width: 768px) {
            .stats {
                flex-direction: column;
                gap: 15px;
            }
            
            .projects {
                grid-template-columns: 1fr;
            }
            
            .contact-links {
                flex-direction: column;
                gap: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>🐍 Python Learning Journey</h1>
            <p class="subtitle">Week 1 Completed - Foundation Projects</p>
            <div class="stats">
                <div class="stat-item">
                    <div class="stat-number">7</div>
                    <div class="stat-label">Days</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">12</div>
                    <div class="stat-label">Projects</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">1000+</div>
                    <div class="stat-label">Lines of Code</div>
                </div>
            </div>
        </header>

        <div class="projects">
            <div class="project-card">
                <h3>📱 Interactive Calculator</h3>
                <p class="project-description">
                    Advanced calculator with menu system, error handling, and multiple mathematical operations including basic arithmetic, powers, and square roots.
                </p>
                <ul class="project-features">
                    <li>Menu-driven interface</li>
                    <li>Error handling for invalid inputs</li>
                    <li>Support for complex calculations</li>
                    <li>User-friendly design</li>
                </ul>
                <div class="project-tech">
                    <span class="tech-tag">Python</span>
                    <span class="tech-tag">Functions</span>
                    <span class="tech-tag">Error Handling</span>
                </div>
            </div>

            <div class="project-card">
                <h3>📝 Data Management Systems</h3>
                <p class="project-description">
                    Comprehensive data management tools including shopping list manager and student grade tracker with full CRUD operations.
                </p>
                <ul class="project-features">
                    <li>Shopping list with sorting/searching</li>
                    <li>Student grade management</li>
                    <li>Statistical analysis features</li>
                    <li>Data validation and error handling</li>
                </ul>
                <div class="project-tech">
                    <span class="tech-tag">Python</span>
                    <span class="tech-tag">Lists</span>
                    <span class="tech-tag">Dictionaries</span>
                    <span class="tech-tag">Data Structures</span>
                </div>
            </div>

            <div class="project-card">
                <h3>🎯 Number Guessing Game</h3>
                <p class="project-description">
                    Interactive guessing game with multiple difficulty levels, comprehensive statistics tracking, and intelligent hint system.
                </p>
                <ul class="project-features">
                    <li>4 difficulty levels</li>
                    <li>Game statistics and win rates</li>
                    <li>Smart hint system</li>
                    <li>Beautiful user interface</li>
                </ul>
                <div class="project-tech">
                    <span class="tech-tag">Python</span>
                    <span class="tech-tag">Random</span>
                    <span class="tech-tag">Loops</span>
                    <span class="tech-tag">Conditionals</span>
                </div>
            </div>

            <div class="project-card">
                <h3>🔐 Password Security System</h3>
                <p class="project-description">
                    Advanced password validation and generation system with security analysis, strength scoring, and best practices recommendations.
                </p>
                <ul class="project-features">
                    <li>Password strength analysis</li>
                    <li>Secure password generation</li>
                    <li>Security recommendations</li>
                    <li>Pattern detection</li>
                </ul>
                <div class="project-tech">
                    <span class="tech-tag">Python</span>
                    <span class="tech-tag">Regular Expressions</span>
                    <span class="tech-tag">Security</span>
                    <span class="tech-tag">OOP</span>
                </div>
            </div>

            <div class="project-card">
                <h3>💰 Expense Tracker</h3>
                <p class="project-description">
                    Full-featured personal finance application with data persistence, comprehensive reporting, and export capabilities.
                </p>
                <ul class="project-features">
                    <li>JSON data persistence</li>
                    <li>Monthly reporting</li>
                    <li>CSV import/export</li>
                    <li>Statistical analysis</li>
                </ul>
                <div class="project-tech">
                    <span class="tech-tag">Python</span>
                    <span class="tech-tag">JSON</span>
                    <span class="tech-tag">File I/O</span>
                    <span class="tech-tag">CSV</span>
                </div>
            </div>

            <div class="project-card">
                <h3>📊 Text Analyzer</h3>
                <p class="project-description">
                    Comprehensive text analysis tool with readability scoring, pattern detection, and detailed statistical reporting.
                </p>
                <ul class="project-features">
                    <li>Text statistics and metrics</li>
                    <li>Readability analysis</li>
                    <li>Pattern detection (emails, URLs, etc.)</li>
                    <li>Word frequency analysis</li>
                </ul>
                <div class="project-tech">
                    <span class="tech-tag">Python</span>
                    <span class="tech-tag">Regular Expressions</span>
                    <span class="tech-tag">Text Processing</span>
                    <span class="tech-tag">Statistics</span>
                </div>
            </div>
        </div>

        <footer class="footer">
            <h3>🎯 Week 1 Goals Achieved!</h3>
            <p>Successfully completed Python fundamentals and built 6 comprehensive applications demonstrating core programming concepts.</p>
            <div class="contact-links">
                <a href="https://github.com/yourusername" target="_blank">GitHub Profile</a>
                <a href="https://linkedin.com/in/yourprofile" target="_blank">LinkedIn</a>
                <a href="mailto:your.email@example.com">Email Contact</a>
            </div>
        </footer>
    </div>
</body>
</html>
```

### **Evening (1 hour): Week 1 Reflection**
**8:00-8:30 PM: Learning Journal**
- [ ] **Resource:** "Code" by Charles Petzold
- [ ] **Read:** Chapter 7 (Our Ten Digits) - pages 91-105
- [ ] **Focus:** Number systems and digital representation
- [ ] **Create:** `day07_week1_reflection.md`
- [ ] **Write:** Reflection on Week 1 learning:
```markdown
# Week 1 Learning Reflection

## Date: [Current Date]

## What I Learned This Week

### Technical Skills
- **Python Fundamentals**: Variables, data types, functions, control flow
- **Data Structures**: Lists, dictionaries, sets, tuples
- **File I/O**: Reading/writing files, JSON, CSV handling
- **Object-Oriented Programming**: Classes, methods, encapsulation basics
- **Text Processing**: String manipulation, regular expressions
- **Error Handling**: Try/except blocks, input validation
- **Git Version Control**: Repository management, commits, GitHub

### Soft Skills
- **Problem Solving**: Breaking down complex problems into smaller parts
- **Code Organization**: Writing clean, readable, maintainable code
- **Documentation**: Adding comments, docstrings, README files
- **Testing**: Manual testing of applications, edge case handling
- **Project Planning**: Designing applications before coding

## Projects Completed
1. **Interactive Calculator** - Mathematical operations with error handling
2. **Shopping List Manager** - CRUD operations with data structures
3. **Student Grade Tracker** - Complex data management with statistics
4. **Number Guessing Game** - Game logic with user interaction
5. **Password Validator** - Security analysis with pattern matching
6. **Expense Tracker** - Data persistence and financial reporting
7. **Text Analyzer** - Comprehensive text processing and analysis

## Challenges Overcome
- **Error Handling**: Learning to anticipate and handle user input errors
- **File Operations**: Understanding file paths, permissions, and data formats
- **Code Organization**: Structuring larger programs with functions and classes
- **Regular Expressions**: Grasping pattern matching concepts
- **Git Workflow**: Understanding staging, commits, and repository management

## Key Insights
- **Practice Makes Perfect**: Daily coding builds muscle memory
- **Start Simple**: Begin with basic functionality, then add features
- **User Experience Matters**: Good interfaces make programs more usable
- **Documentation is Crucial**: Well-documented code is easier to maintain
- **Version Control is Essential**: Git saves time and prevents data loss

## What I'm Proud Of
- Completing all 7 days without skipping any
- Building functional applications, not just following tutorials
- Creating a professional GitHub repository
- Learning to debug programs independently
- Understanding Python documentation

## Areas for Improvement
- **Speed**: Still slow at typing and remembering syntax
- **Advanced Concepts**: Need to learn more about algorithms and data structures
- **Testing**: Should learn formal testing frameworks
- **Performance**: Code works but might not be optimized
- **Web Development**: Ready to learn frameworks like Flask

## Next Week Goals
- Learn object-oriented programming in depth
- Start building web applications
- Understand databases and SQL
- Improve code quality and testing
- Begin working with external libraries

## Motivation Check
**Energy Level**: ⭐⭐⭐⭐⭐ (5/5) - Excited to continue!
**Confidence Level**: ⭐⭐⭐⭐☆ (4/5) - Feel good about basics
**Commitment Level**: ⭐⭐⭐⭐⭐ (5/5) - Fully committed to the journey

## Notes from "Code" by Charles Petzold
- Understanding how computers represent numbers in binary
- Connection between electrical circuits and digital logic
- Historical context of computing and communication systems
- Appreciation for the complexity hidden behind simple operations

## Looking Forward
Week 1 has been an incredible foundation. I've gone from knowing nothing about programming to building functional applications. The concepts are starting to click, and I'm excited to tackle web development in Week 2. The daily routine of learning, coding, and reading is working well.

Next week's focus on web development with Flask will be a big step up, but I feel prepared with the solid foundation from this week.

## Code Quality Improvements Made
- Added proper error handling to all projects
- Implemented input validation everywhere
- Used descriptive variable names
- Added docstrings to functions
- Created clean, modular code structure
- Followed Python naming conventions
```

**8:30-9:00 PM: GitHub Portfolio Update**
- [ ] **Update:** README.md with Week 1 accomplishments
- [ ] **Commit:** All Week 1 projects to GitHub:
```bash
# Add all new files
git add .

# Commit with detailed message
git commit -m "Week 1 complete: 6 Python projects with full functionality

- Calculator with advanced operations and error handling
- Shopping list and student grade management systems  
- Number guessing game with statistics and difficulty levels
- Password validator with security analysis and generation
- Expense tracker with data persistence and reporting
- Text analyzer with comprehensive text processing
- Portfolio website showcasing all projects

Skills demonstrated: Python fundamentals, file I/O, OOP basics, 
error handling, data structures, regex, and Git workflow."

# Push to GitHub
git push origin main

# Create Week 1 release tag
git tag -a week1-complete -m "Week 1: Python Fundamentals Mastered"
git push origin week1-complete
```

### **Day 7 Deliverables:**
- [ ] All Week 1 projects committed to GitHub
- [ ] Professional README.md file
- [ ] `day07_portfolio.html` - Portfolio website
- [ ] `day07_week1_reflection.md` - Learning reflection
- [ ] `day07_code_improvements.py` - Code quality improvements
- [ ] `day07_notes.txt` - Notes from "Code" chapter 7
- [ ] Git repository with proper version control
- [ ] Week 1 completion tag on GitHub

---

# **WEEK 2: OBJECT-ORIENTED PROGRAMMING & LIBRARIES**

## **DAY 8: ADVANCED OOP CONCEPTS**

### **Morning (2 hours): Classes and Objects Deep Dive**
**8:00-9:00 AM: OOP Fundamentals**
- [ ] **Resource:** "Python Crash Course" Chapter 9 (Classes)
- [ ] **Read:** Pages 161-185 (defining classes, creating instances, inheritance)
- [ ] **Create:** `day08_oop_basics.py`
- [ ] **Practice:** Core OOP concepts:
```python
# Basic class definition and usage
class Person:
    """A simple Person class to demonstrate OOP concepts"""
    
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    population = 0
    
    def __init__(self, name, age, email):
        """Initialize a Person instance"""
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        self.email = email
        self.skills = []
        self.friends = []
        
        # Update class variable
        Person.population += 1
    
    def __str__(self):
        """String representation of the person"""
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Person('{self.name}', {self.age}, '{self.email}')"
    
    def introduce(self):
        """Person introduces themselves"""
        skills_str = ", ".join(self.skills) if self.skills else "none yet"
        return f"Hi, I'm {self.name}, {self.age} years old. My skills: {skills_str}"
    
    def add_skill(self, skill):
        """Add a skill to the person"""
        if skill not in self.skills:
            self.skills.append(skill)
            return f"{self.name} learned {skill}!"
        return f"{self.name} already knows {skill}"
    
    def add_friend(self, friend):
        """Add another Person as a friend"""
        if isinstance(friend, Person) and friend not in self.friends:
            self.friends.append(friend)
            friend.friends.append(self)  # Make friendship mutual
            return f"{self.name} and {friend.name} are now friends!"
        return "Invalid friend or already friends"
    
    def have_birthday(self):
        """Increase age by 1"""
        self.age += 1
        return f"Happy birthday {self.name}! Now {self.age} years old."
    
    @classmethod
    def get_population(cls):
        """Get total population (class method)"""
        return f"Total population: {cls.population}"
    
    @staticmethod
    def is_adult(age):
        """Check if age represents an adult (static method)"""
        return age >= 18

# Demonstrate the Person class
print("👥 PERSON CLASS DEMONSTRATION")
print("=" * 35)

# Create instances
alice = Person("Alice", 25, "alice@email.com")
bob = Person("Bob", 30, "bob@email.com")
charlie = Person("Charlie", 17, "charlie@email.com")

print(f"Created people: {alice}, {bob}, {charlie}")
print(Person.get_population())

# Test methods
print(f"\n{alice.introduce()}")
print(alice.add_skill("Python"))
print(alice.add_skill("JavaScript"))
print(alice.add_skill("Python"))  # Already knows it

print(f"\n{bob.introduce()}")
print(bob.add_skill("Data Science"))
print(bob.add_friend(alice))

print(f"\n{alice.have_birthday()}")
print(f"Is Charlie an adult? {Person.is_adult(charlie.age)}")
print(f"Is Alice an adult? {Person.is_adult(alice.age)}")
```

**9:00-10:00 AM: Inheritance and Polymorphism**
- [ ] **Practice:** Advanced OOP with inheritance:
```python
# Inheritance example
class Student(Person):
    """Student class inheriting from Person"""
    
    def __init__(self, name, age, email, student_id, major):
        super().__init__(name, age, email)  # Call parent constructor
        self.student_id = student_id
        self.major = major
        self.grades = {}
        self.gpa = 0.0
    
    def __str__(self):
        return f"Student(name='{self.name}', major='{self.major}')"
    
    def introduce(self):
        """Override parent method"""
        base_intro = super().introduce()
        return f"{base_intro} I'm studying {self.major}."
    
    def add_grade(self, subject, grade):
        """Add a grade for a subject"""
        if 0 <= grade <= 100:
            self.grades[subject] = grade
            self._calculate_gpa()
            return f"Added grade {grade} for {subject}"
        return "Invalid grade (must be 0-100)"
    
    def _calculate_gpa(self):
        """Private method to calculate GPA"""
        if self.grades:
            total = sum(self.grades.values())
            self.gpa = total / len(self.grades)
    
    def get_transcript(self):
        """Get student transcript"""
        if not self.grades:
            return f"{self.name} has no grades yet"
        
        transcript = f"\n📋 TRANSCRIPT FOR {self.name.upper()}\n"
        transcript += f"Student ID: {self.student_id}\n"
        transcript += f"Major: {self.major}\n"
        transcript += "-" * 30 + "\n"
        
        for subject, grade in self.grades.items():
            transcript += f"{subject:<20}: {grade:>3}\n"
        
        transcript += "-" * 30 + "\n"
        transcript += f"{'GPA:':<20}: {self.gpa:>6.2f}\n"
        
        return transcript

class Teacher(Person):
    """Teacher class inheriting from Person"""
    
    def __init__(self, name, age, email, employee_id, department):
        super().__init__(name, age, email)
        self.employee_id = employee_id
        self.department = department
        self.students = []
        self.courses = []
    
    def __str__(self):
        return f"Teacher(name='{self.name}', dept='{self.department}')"
    
    def introduce(self):
        """Override parent method"""
        base_intro = super().introduce()
        return f"{base_intro} I teach in the {self.department} department."
    
    def add_student(self, student):
        """Add a student to teacher's class"""
        if isinstance(student, Student):
            self.students.append(student)
            return f"{student.name} added to {self.name}'s class"
        return "Invalid student"
    
    def add_course(self, course_name):
        """Add a course to teacher's schedule"""
        if course_name not in self.courses:
            self.courses.append(course_name)
            return f"{self.name} now teaches {course_name}"
        return f"{self.name} already teaches {course_name}"
    
    def grade_student(self, student, subject, grade):
        """Grade a student (if student is in teacher's class)"""
        if student in self.students:
            return student.add_grade(subject, grade)
        return f"{student.name} is not in {self.name}'s class"

# Demonstrate inheritance
print("\n🎓 INHERITANCE DEMONSTRATION")
print("=" * 32)

# Create students and teacher
student1 = Student("Emma", 20, "emma@university.edu", "S001", "Computer Science")
student2 = Student("David", 19, "david@university.edu", "S002", "Mathematics")
teacher1 = Teacher("Dr. Smith", 45, "smith@university.edu", "T001", "Computer Science")

# Demonstrate polymorphism (same method, different behavior)
people = [alice, student1, teacher1]
print("Introductions (demonstrating polymorphism):")
for person in people:
    print(f"- {person.introduce()}")

# Teacher-student interactions
print(f"\n{teacher1.add_student(student1)}")
print(f"{teacher1.add_student(student2)}")
print(f"{teacher1.add_course('Python Programming')}")
print(f"{teacher1.add_course('Data Structures')}")

# Grading
print(f"\n{teacher1.grade_student(student1, 'Python Programming', 95)}")
print(f"{teacher1.grade_student(student1, 'Data Structures', 88)}")
print(f"{teacher1.grade_student(student2, 'Calculus', 92)}")

# Show transcripts
print(student1.get_transcript())
```

### **Afternoon (2 hours): Bank Account Management System**
**2:00-4:00 PM: Complete Banking System with OOP**
- [ ] **Create:** `day08_bank_system.py`
- [ ] **Build:** Comprehensive banking application:
```python
from datetime import datetime
import uuid
import json

class Transaction:
    """Represents a single transaction"""
    
    def __init__(self, transaction_type, amount, description="", balance_after=0):
        self.id = str(uuid.uuid4())[:8]
        self.type = transaction_type  # 'deposit', 'withdrawal', 'transfer'
        self.amount = amount
        self.description = description
        self.timestamp = datetime.now()
        self.balance_after = balance_after
    
    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M')} | {self.type.title()} | {self.amount:.2f} CZK"
    
    def to_dict(self):
        """Convert transaction to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'type': self.type,
            'amount': self.amount,
            'description': self.description,
            'timestamp': self.timestamp.isoformat(),
            'balance_after': self.balance_after
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create transaction from dictionary"""
        transaction = cls(data['type'], data['amount'], data['description'], data['balance_after'])
        transaction.id = data['id']
        transaction.timestamp = datetime.fromisoformat(data['timestamp'])
        return transaction

class BankAccount:
    """Base bank account class"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_number = self._generate_account_number()
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []
        self.created_date = datetime.now()
        self.is_active = True
        
        # Record initial deposit if any
        if initial_balance > 0:
            self._add_transaction('deposit', initial_balance, 'Initial deposit')
    
    def _generate_account_number(self):
        """Generate unique account number"""
        return f"ACC{uuid.uuid4().hex[:8].upper()}"
    
    def _add_transaction(self, transaction_type, amount, description=""):
        """Add transaction to history"""
        transaction = Transaction(transaction_type, amount, description, self.balance)
        self.transactions.append(transaction)
        return transaction
    
    def deposit(self, amount, description=""):
        """Deposit money to account"""
        if not self.is_active:
            return False, "Account is inactive"
        
        if amount <= 0:
            return False, "Deposit amount must be positive"
        
        self.balance += amount
        transaction = self._add_transaction('deposit', amount, description)
        return True, f"Deposited {amount:.2f} CZK. New balance: {self.balance:.2f} CZK"
    
    def withdraw(self, amount, description=""):
        """Withdraw money from account"""
        if not self.is_active:
            return False, "Account is inactive"
        
        if amount <= 0:
            return False, "Withdrawal amount must be positive"
        
        if amount > self.balance:
            return False, f"Insufficient funds. Current balance: {self.balance:.2f} CZK"
        
        self.balance -= amount
        transaction = self._add_transaction('withdrawal', amount, description)
        return True, f"Withdrew {amount:.2f} CZK. New balance: {self.balance:.2f} CZK"
    
    def transfer(self, recipient_account, amount, description=""):
        """Transfer money to another account"""
        if not self.is_active:
            return False, "Account is inactive"
        
        if not recipient_account.is_active:
            return False, "Recipient account is inactive"
        
        # Withdraw from this account
        success, message = self.withdraw(amount, f"Transfer to {recipient_account.account_number}")
        if not success:
            return False, message
        
        # Deposit to recipient account
        recipient_account.deposit(amount, f"Transfer from {self.account_number}")
        
        return True, f"Transferred {amount:.2f} CZK to {recipient_account.account_holder}"
    
    def get_balance(self):
        """Get current balance"""
        return self.balance
    
    def get_statement(self, days=30):
        """Get account statement for specified days"""
        cutoff_date = datetime.now() - datetime.timedelta(days=days)
        recent_transactions = [t for t in self.transactions if t.timestamp >= cutoff_date]
        
        statement = f"\n💳 ACCOUNT STATEMENT\n"
        statement += f"Account: {self.account_number}\n"
        statement += f"Holder: {self.account_holder}\n"
        statement += f"Period: Last {days} days\n"
        statement += f"Current Balance: {self.balance:.2f} CZK\n"
        statement += "=" * 50 + "\n"
        
        if not recent_transactions:
            statement += "No transactions in this period.\n"
        else:
            for transaction in reversed(recent_transactions):  # Most recent first
                statement += f"{transaction}\n"
                if transaction.description:
                    statement += f"  Description: {transaction.description}\n"
                statement += f"  Balance after: {transaction.balance_after:.2f} CZK\n"
                statement += "-" * 30 + "\n"
        
        return statement
    
    def close_account(self):
        """Close the account"""
        if self.balance > 0:
            return False, f"Cannot close account with positive balance ({self.balance:.2f} CZK)"
        
        self.is_active = False
        return True, "Account closed successfully"
    
    def to_dict(self):
        """Convert account to dictionary for JSON serialization"""
        return {
            'account_number': self.account_number,
            'account_holder': self.account_holder,
            'balance': self.balance,
            'created_date': self.created_date.isoformat(),
            'is_active': self.is_active,
            'transactions': [t.to_dict() for t in self.transactions]
        }

class SavingsAccount(BankAccount):
    """Savings account with interest calculation"""
    
    def __init__(self, account_holder, initial_balance=0, interest_rate=0.02):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate  # Annual interest rate
        self.minimum_balance = 100  # Minimum balance requirement
    
    def withdraw(self, amount, description=""):
        """Override withdrawal to check minimum balance"""
        if not self.is_active:
            return False, "Account is inactive"
        
        if amount <= 0:
            return False, "Withdrawal amount must be positive"
        
        if (self.balance - amount) < self.minimum_balance:
            return False, f"Withdrawal would violate minimum balance requirement ({self.minimum_balance} CZK)"
        
        return super().withdraw(amount, description)
    
    def calculate_interest(self, days=30):
        """Calculate interest for specified period"""
        daily_rate = self.interest_rate / 365
        interest = self.balance * daily_rate * days
        return interest
    
    def apply_interest(self, days=30):
        """Apply interest to account"""
        interest = self.calculate_interest(days)
        self.balance += interest
        self._add_transaction('deposit', interest, f"Interest for {days} days")
        return interest

class CheckingAccount(BankAccount):
    """Checking account with overdraft protection"""
    
    def __init__(self, account_holder, initial_balance=0, overdraft_limit=1000):
        super().__init__(account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit
        self.overdraft_fee = 50  # Fee for using overdraft
    
    def withdraw(self, amount, description=""):
        """Override withdrawal to allow overdraft"""
        if not self.is_active:
            return False, "Account is inactive"
        
        if amount <= 0:
            return False, "Withdrawal amount must be positive"
        
        # Check if withdrawal exceeds balance + overdraft limit
        if amount > (self.balance + self.overdraft_limit):
            return False, f"Exceeds overdraft limit. Available: {self.balance + self.overdraft_limit:.2f} CZK"
        
        # Check if overdraft will be used
        will_overdraft = amount > self.balance
        
        self.balance -= amount
        transaction = self._add_transaction('withdrawal', amount, description)
        
        # Apply overdraft fee if going into overdraft
        if will_overdraft and self.balance < 0:
            self.balance -= self.overdraft_fee
            self._add_transaction('withdrawal', self.overdraft_fee, "Overdraft fee")
            return True, f"Withdrew {amount:.2f} CZK (overdraft used, fee applied). New balance: {self.balance:.2f} CZK"
        
        return True, f"Withdrew {amount:.2f} CZK. New balance: {self.balance:.2f} CZK"

class Bank:
    """Bank class to manage multiple accounts"""
    
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.total_customers = 0
    
    def create_account(self, account_type, account_holder, initial_balance=0, **kwargs):
        """Create a new account"""
        if account_type.lower() == 'savings':
            account = SavingsAccount(account_holder, initial_balance, kwargs.get('interest_rate', 0.02))
        elif account_type.lower() == 'checking':
            account = CheckingAccount(account_holder, initial_balance, kwargs.get('overdraft_limit', 1000))
        else:
            account = BankAccount(account_holder, initial_balance)
        
        self.accounts[account.account_number] = account
        self.total_customers += 1
        
        return account.account_number, f"Account created successfully for {account_holder}"
    
    def get_account(self, account_number):
        """Get account by account number"""
        return self.accounts.get(account_number)
    
    def close_account(self, account_number):
        """Close an account"""
        account = self.get_account(account_number)
        if not account:
            return False, "Account not found"
        
        success, message = account.close_account()
        if success:
            # Remove from active accounts (but keep record)
            pass
        
        return success, message
    
    def get_bank_summary(self):
        """Get bank summary statistics"""
        total_balance = sum(account.balance for account in self.accounts.values())
        active_accounts = sum(1 for account in self.accounts.values() if account.is_active)
        
        summary = f"\n🏦 {self.name.upper()} SUMMARY\n"
        summary += "=" * 40 + "\n"
        summary += f"Total Customers: {self.total_customers}\n"
        summary += f"Active Accounts: {active_accounts}\n"
        summary += f"Total Deposits: {total_balance:.2f} CZK\n"
        summary += f"Account Types:\n"
        
        type_counts = {}
        for account in self.accounts.values():
            account_type = type(account).__name__
            type_counts[account_type] = type_counts.get(account_type, 0) + 1
        
        for account_type, count in type_counts.items():
            summary += f"  {account_type}: {count}\n"
        
        return summary

def main():
    """Main banking application"""
    bank = Bank("Czech National Bank")
    
    print("🏦" + "="*50 + "🏦")
    print("           BANK ACCOUNT MANAGEMENT SYSTEM")
    print("🏦" + "="*50 + "🏦")
    
    current_account = None
    
    while True:
        if current_account:
            account = bank.get_account(current_account)
            print(f"\n💳 Logged in: {account.account_holder} ({current_account})")
            print(f"💰 Balance: {account.balance:.2f} CZK")
        
        print(f"\n🏛️  MAIN MENU:")
        print("1. 🆕 Create Account")
        print("2. 🔑 Login to Account")
        print("3. 💰 Deposit Money")
        print("4. 💸 Withdraw Money")
        print("5. 🔄 Transfer Money")
        print("6. 📊 View Statement")
        print("7. 🏦 Bank Summary")
        print("8. 🚪 Logout")
        print("9. ❌ Close Account")
        print("10. 🚪 Exit")
        
        choice = input("\nSelect option (1-10): ").strip()
        
        if choice == '1':
            holder_name = input("Enter account holder name: ").strip()
            if not holder_name:
                print("❌ Name cannot be empty!")
                continue
            
            print("Account types:")
            print("1. Basic Account")
            print("2. Savings Account (2% interest)")
            print("3. Checking Account (1000 CZK overdraft)")
            
            account_type_choice = input("Choose account type (1-3): ").strip()
            initial_balance = 0
            
            try:
                balance_input = input("Initial deposit (optional, 0 for none): ").strip()
                if balance_input:
                    initial_balance = float(balance_input)
                    if initial_balance < 0:
                        print("❌ Initial balance cannot be negative!")
                        continue
            except ValueError:
                print("❌ Invalid amount!")
                continue
            
            if account_type_choice == '1':
                account_num, message = bank.create_account('basic', holder_name, initial_balance)
            elif account_type_choice == '2':
                account_num, message = bank.create_account('savings', holder_name, initial_balance)
            elif account_type_choice == '3':
                account_num, message = bank.create_account('checking', holder_name, initial_balance)
            else:
                print("❌ Invalid account type!")
                continue
            
            print(f"✅ {message}")
            print(f"💳 Account Number: {account_num}")
            current_account = account_num
        
        elif choice == '2':
            account_num = input("Enter account number: ").strip().upper()
            account = bank.get_account(account_num)
            if account:
                if account.is_active:
                    current_account = account_num
                    print(f"✅ Logged in successfully!")
                else:
                    print("❌ Account is inactive!")
            else:
                print("❌ Account not found!")
        
        elif choice == '3':
            if not current_account:
                print("❌ Please login first!")
                continue
            
            try:
                amount = float(input("Enter deposit amount (CZK): "))
                description = input("Description (optional): ").strip()
                
                account = bank.get_account(current_account)
                success, message = account.deposit(amount, description)
                
                if success:
                    print(f"✅ {message}")
                else:
                    print(f"❌ {message}")
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == '4':
            if not current_account:
                print("❌ Please login first!")
                continue
            
            try:
                amount = float(input("Enter withdrawal amount (CZK): "))
                description = input("Description (optional): ").strip()
                
                account = bank.get_account(current_account)
                success, message = account.withdraw(amount, description)
                
                if success:
                    print(f"✅ {message}")
                else:
                    print(f"❌ {message}")
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == '5':
            if not current_account:
                print("❌ Please login first!")
                continue
            
            recipient_num = input("Enter recipient account number: ").strip().upper()
            recipient = bank.get_account(recipient_num)
            
            if not recipient:
                print("❌ Recipient account not found!")
                continue
            
            try:
                amount = float(input("Enter transfer amount (CZK): "))
                description = input("Description (optional): ").strip()
                
                account = bank.get_account(current_account)
                success, message = account.transfer(recipient, amount, description)
                
                if success:
                    print(f"✅ {message}")
                else:
                    print(f"❌ {message}")
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == '6':
            if not current_account:
                print("❌ Please login first!")
                continue
            
            try:
                days = int(input("Enter number of days for statement (default 30): ") or "30")
                account = bank.get_account(current_account)
                print(account.get_statement(days))
            except ValueError:
                print("❌ Invalid number of days!")
        
        elif choice == '7':
            print(bank.get_bank_summary())
        
        elif choice == '8':
            if current_account:
                current_account = None
                print("✅ Logged out successfully!")
            else:
                print("❌ Not logged in!")
        
        elif choice == '9':
            if not current_account:
                print("❌ Please login first!")
                continue
            
            confirm = input("Are you sure you want to close this account? (y/n): ").strip().lower()
            if confirm == 'y':
                account = bank.get_account(current_account)
                success, message = bank.close_account(current_account)
                if success:
                    print(f"✅ {message}")
                    current_account = None
                else:
                    print(f"❌ {message}")
        
        elif choice == '10':
            print("👋 Thank you for using our banking system!")
            break
        
        else:
            print("❌ Invalid choice! Please select 1-10")

if __name__ == "__main__":
    main()
```

### **Evening (1 hour): Reading & OOP Practice**
**8:00-8:30 PM: Continue "Code"**
- [ ] **Resource:** "Code" by Charles Petzold
- [ ] **Read:** Chapter 8 (Alternatives to Ten) - pages 106-120
- [ ] **Focus:** Different number systems and their applications
- [ ] **Notes:** Add to `day08_notes.txt`

**8:30-9:00 PM: OOP Concepts Practice**
- [ ] **Practice:** Object-oriented design patterns:
```python
>>> # Practice class creation and inheritance
>>> class Animal:
...     def __init__(self, name):
...         self.name = name
...     def speak(self):
...         pass
...
>>> class Dog(Animal):
...     def speak(self):
...         return f"{self.name} says Woof!"
...
>>> class Cat(Animal):
...     def speak(self):
...         return f"{self.name} says Meow!"
...
>>> # Polymorphism demonstration
>>> animals = [Dog("Buddy"), Cat("Whiskers")]
>>> for animal in animals:
...     print(animal.speak())
```

### **Day 8 Deliverables:**
- [ ] `day08_oop_basics.py` - OOP fundamentals with Person, Student, Teacher classes
- [ ] `day08_bank_system.py` - Complete banking system with inheritance
- [ ] `day08_notes.txt` - Notes from "Code" chapter 8
- [ ] Understanding of classes, objects, inheritance, and polymorphism
- [ ] Experience with real-world OOP application design

---

**Continue with remaining 20 days following the same detailed pattern...**

---

# **MONTH 1 SUCCESS METRICS**

## **Week 1 Completion (Days 1-7):**
- [ ] 12+ Python programs running without errors
- [ ] Understanding of variables, data types, functions, control flow
- [ ] File operations and error handling
- [ ] Git workflow and GitHub portfolio setup
- [ ] Notes from "Code" chapters 1-7

## **Week 2 Completion (Days 8-14):**
- [ ] Object-oriented programming mastery
- [ ] Working with external libraries (requests, BeautifulSoup)
- [ ] Web scraping and automation scripts
- [ ] Database operations with SQLite
- [ ] Advanced Git workflow

## **Week 3 Completion (Days 15-21):**
- [ ] Command line and Linux proficiency
- [ ] Advanced Python concepts (decorators, generators)
- [ ] Testing and code quality practices
- [ ] API development basics
- [ ] Production deployment concepts

## **Week 4 Completion (Days 22-28):**
- [ ] 30+ GitHub repositories with quality code
- [ ] 6+ substantial projects deployed
- [ ] Professional portfolio website
- [ ] Strong Python fundamentals
- [ ] Ready for Month 2 web development

**By the end of Month 1, you'll have:**
- ✅ Comprehensive Python programming skills
- ✅ Professional development environment
- ✅ Impressive GitHub portfolio with real projects
- ✅ Understanding of computer science fundamentals
- ✅ Confidence to tackle web development
- ✅ Foundation for advanced topics in following months

**Continue reading:** "Code" by Charles Petzold (finish by Month 1 end)
**Prepare for Month 2:** Web development with Flask, HTML/CSS, JavaScript basics