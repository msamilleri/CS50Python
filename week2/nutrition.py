##########################################
#                                        #
#       author:@msamilleri               #
#       you can use in your project      #
#                                        #
##########################################

fruits ={"Appel":130,"Avocado":50,"Sweet Cherries":100,"banana":110}
fruit_input=input("Item :")

for key,value in fruits.items():
    if fruit_input == key:
        print("Calories :",value)

