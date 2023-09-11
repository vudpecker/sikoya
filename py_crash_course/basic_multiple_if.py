import string

passwords = ["jiperBlr1", "jiper@Blr1" , "jiper@#Blr144$$"]


for password in passwords:
    count = 0
    ch = ""
    message = "The password has "

    for c in password:
        if c in string.punctuation:  ## Return all sets of punctuation
            #print(c, end="")
            ch += c
            count += 1

    message += str(count) + " "

    if count == 0:
        message += f"special character."
    elif count == 1:
        message += f"special character, which is {ch}."
    elif count > 1:
        message += f"special characters, which are {ch}."

    print(message)

#print(password,end='') ##Debug
print(f"The password has {count} special character" + ("s" if count > 1 else "") + \
      ". Which + ("is" if count == 1 else "are") + f"{ch}.")