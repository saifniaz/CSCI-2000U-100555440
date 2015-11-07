reader = open("gadsby_stripped.txt", "r")
temp = reader.readlines()
reader.close()
def has_no_e(String):
    for line in String:
        index = True
        for has_e in line:    
            if(has_e == 'e'):
                index = False
        print(index)
has_no_e(temp)