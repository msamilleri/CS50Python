import datetime as dt
import inflect
p = inflect.engine()

def date_control(input_date):
    if (input_date[0].isnumeric()):
        return True
    else:
        return False
def date_to_minutes(brith_day,is_date_ok):
    if is_date_ok:
        date_format = "%Y-%m-%d"
        brith_date = dt.datetime.strptime(brith_day, date_format)
        at_the_moment = dt.datetime.now()
        totral_days = at_the_moment - brith_date
        print(totral_days.days)
        return totral_days.days
    else:
        print("Wrong Date !!!")
        return False
def days2minutes(dayss):
    total_minutes = dayss*1440
    words1 = p.number_to_words(total_minutes, andword="").capitalize() + " minutes"
    print(words1)

def main(brith_day_input):
   is_date_ok = date_control(brith_day_input)
   if is_date_ok:
    days = date_to_minutes(brith_day_input,is_date_ok)
    days2minutes(days)
   else:
       print("Wrong Date of Brith")

if __name__ == "__main__":
    brith_day_input = input("Date of Birth: ")
    main(brith_day_input)

