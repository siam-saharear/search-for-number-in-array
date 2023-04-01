num_list=[74,55,46,54,68,56,79]
def number_checking(num):
    statement="Number found boss."

    if num in num_list:
        print(statement)
    else:
        print("Number missing boss.")
confirmation=1
while confirmation==1:
    for i in range(3):
        num=int(input("Enter a number to check in array: "))
        number_checking(num)
    raw_confirmation=input("Search for number again: ")
    if raw_confirmation.lower()=="yes" or raw_confirmation.lower()=="y" or (raw_confirmation)=="1":
        confirmation=1
    else:
        confirmation=0
