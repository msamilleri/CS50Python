def main():
    outdate()
def outdate():
    ### Date Type 1 ---->>> July 1, 1995
    ### Date Type 2 ---->>> 1/7/1995
    numbers = ( '1','2','3','4','5','6','7','8','9')
    mount_list =[
        "January","February","March","April","May","June","July",
        "August","September","October","November","December"]
    date_type = 0
    while True:
        try:
            date_text = input("Date:")
            how_date_type = date_text.startswith(numbers)

            if how_date_type :
                date_type = 2
            else:
                date_type = 1

            if date_type == 2:
                data_text_new = date_text.split('/')
                if (1 > int(data_text_new[0])) or (int(data_text_new[0]) > 12) :
                    raise Exception
                if (1 > int(data_text_new[1])) or (int (data_text_new[1]) > 31):
                    raise Exception
                print(data_text_new[2].zfill(4),data_text_new[1].zfill(2),data_text_new[0].zfill(2),sep='-')
                break

            if date_type == 1:
                text = date_text.split()
                mount_two = str((mount_list.index(text[0])+1))
                day_two=text[1].replace(',','')
                days = int(day_two)

                if (1 > days) or (days > 31):
                    raise Exception

                print(text[2].zfill(4), mount_two.zfill(2), day_two.zfill(2), sep='-')
                break

        except Exception:
            pass

main()