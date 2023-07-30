##########################################
#                                        #
#       author:@msamilleri               #
#       you can use in your project      #
#                                        #
##########################################
price = 50
while price>0:
    amount_due = int(input('Amount Due : '))
    if amount_due == 25 or amount_due == 10 or amount_due == 5 :
        price = price-amount_due
        if price == 0:
            print("Change Owned :", price)
        else:
            print("Inser Coin :", price)
    else:
        pass


