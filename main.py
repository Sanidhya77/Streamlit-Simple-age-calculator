import streamlit as st
from datetime import date
import calendar

st.title("Age Finder App")
st.subheader("Find out your age in years, months, and days")

# Allow dates from 1900-01-01 to today
dob = st.date_input("Select your date of birth", min_value=date(1900, 1, 1), max_value=date.today())

def calculate_age(birth_date, current_date):
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    if days < 0:
        months -= 1
        # get number of days in the previous month
        if current_date.month == 1:
            prev_month = 12
            prev_year = current_date.year - 1
        else:
            prev_month = current_date.month - 1
            prev_year = current_date.year
        days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

if dob:
    today = date.today()
    years, months, days = calculate_age(dob, today)
    st.write(f"You are {years} years, {months} months, and {days} days old.")
    st.success("Age calculation complete!")





# import streamlit as st
# from datetime import datetime, date
# import calendar
# # from dateutil.relativedelta import relativedelta

# st.title("Age finder App")

# st.subheader("Find out your age in years, months, and days")

# dob = st.date_input("Select your date of birth", min value=date(1900, 1, 1), max_value=date.today())

# def agecalculator(dob):
#     today = date.today()
#     age_years = today.year - dob.year
#     age_months = today.month - dob.month
#     age_days = today.day - dob.day

#     if age_days < 0:
#         age_months -= 1
#         age_days += calendar.monthrange(today.year, today.month)[1]

#     if age_months < 0:
#         age_years -= 1
#         age_months += 12

#     return age_years, age_months, age_days

# st.write(f"Your date of birth is: {dob}")
# if dob:
#     age_years, age_months, age_days = agecalculator(dob)
#     st.write(f"You are {age_years} years, {age_months} months, and {age_days} days old.")
#     st.success("Age calculation complete!")
# if dob:
#    today = date.today()
#    age = relativedelta(today, dob)
#    st.write(f"You are {age.years} years, {age.months} months, and {age.days} days old.")
#    st.success("Age calculation complete!")