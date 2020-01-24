while True:
    response = input("What say you? ")
    if (response.isnumeric()):
        response = int(response)
        if (response > 3 and response < 5):
            break
        else:
            print('hello' * response)
    else:
        print("You say", response, "????")
print("goodbye")            
