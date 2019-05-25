while True:
    roman = {'I': 1, 'V': 5, 'X': 10, 'i':1, 'v':5, 'x':10}
    integer = 0
    s=input()
    try:
        if len(s)<=4:
            for i in range(len(s)):
                if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                    integer += roman[s[i]] - 2 * roman[s[i - 1]]
                else:
                    integer += roman[s[i]]
            print(integer)
        else:
            print("Check input")
    except:
        print("Give valid input")
