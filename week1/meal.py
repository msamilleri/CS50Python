##########################################
#                                        #
#       author:@msamilleri               #
#       you can use in your project      #
#                                        #
##########################################
def main():
    time_req = input('What time is it ?')
    time = convert(time_req)
    if (7 <= time) and (time <=8):
        print('breakfast time ')
    elif (12 <= time) and (time <= 13):
        print('lunch time')
    elif (18 <= time) and (time <= 19):
        print('dinner time')
    else:
        print('its not food time')
def convert(time):
    hours, minutes = time.split(":")
    return int(hours)


if __name__ == "__main__":
    main()
