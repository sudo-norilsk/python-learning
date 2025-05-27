from datetime import date

# 1. Personal greeting
myName = "Vojtech Hlavaty"
message = f"Hello sir {myName}"
print(message)

# 2. Dates
birthday_date = date(2003, 4, 11)
today = date.today()

# 3. Calculate full years
age_years = today.year - birthday_date.year

# Check if birthday hasn't happened yet this year → subtract one year
if (today.month, today.day) < (birthday_date.month, birthday_date.day):
    age_years -= 1

# 4. Calculate last birthday (to get remaining days)
last_birthday = date(today.year, birthday_date.month, birthday_date.day)
if today < last_birthday:
    last_birthday = date(today.year - 1, birthday_date.month, birthday_date.day)

# 5. Remaining days since last birthday
remaining_days = (today - last_birthday).days

# 6. Output
print(f"You are {age_years} years and {remaining_days} days old.")
