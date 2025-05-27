from datetime import date
import datetime
# 1 task
myName = "Vojtech Hlavaty"
message = f"Hello sir {myName}"
print (message)

# 2 task

# getting year
birtday_date = date(2003, 4, 11)
year_my = birtday_date.year
today = date.today()
year_today = today.year

age_year = year_today - year_my 

print(age_year)

# converting months into days

age_days = today - birtday_date
pure_days = age_days - (365 * age_year)
print (pure_days)
# age_years = age_days / 365
# print(age_days)
# print(age_years)

# 3 task
daily_hours = 6
yearly_hours = daily_hours * 365
months_to_job = 12

# print(f"🚀 Welcome to my Programming Journey!")
# print(f"Hi, I'm {myName}!")
# print(f"I'm {age_years} years old ({age_days:,} days)")
# print(f"Goal: Land Python developer job in {months_to_job} months")
# print(f"Commitment: {daily_hours} hours/day = {yearly_hours:,} hours/year")
# print(f"Starting date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
# print("Let's build amazing things! 💻")