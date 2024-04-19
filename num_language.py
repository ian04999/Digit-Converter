#Number to Words Translator.
#must be non-negative number
#start with 0~X000 -> zero to thouthan
#10,000 -> 10 thxxx and 000 

        
def singleDigit(number):
    if number == 1:
        return "one"
    if number == 2:
        return "two"
    if number == 3:
        return "three"
    if number == 4:
        return "four"
    if number == 5:
        return "five"
    if number == 6:
        return "six"
    if number == 7:
        return "seven"
    if number == 8:
        return "eight"
    if number == 9:
        return "nine"
    else:
        return "invalid input"
    
def twoDigit(number):
    #if number%10 == 0:
    #    digitS = "ty"
        # if eighty, str.replace()
    # 10~19
    #elif number < 20:
    digitS = "teen"
    
    if number == 10:
        return "ten"
    elif number == 11:
        return "eleven"
    elif number == 12:
        return "twelve"
    elif number == 13:
        return "thir"+digitS
    elif number == 15:
        return "fif" +digitS
    elif number == 18:
        return "eigh"+digitS
    elif number < 20:
        front = singleDigit(number%10)
        return front+digitS
    # 20~29
    elif number < 30: 
        front = "twenty "
        if number%10 == 0:
            return front
        else:
            return front + singleDigit(number%10)
    # 30~39
    elif number < 40:
        front = "thirty "
        if number%10 == 0:
            return front
        else:
            return front + singleDigit(number%10)
    # 40~49
    elif number < 50: 
        front = "forty "
        if number%10 == 0:
            return front
        else:
            return front + singleDigit(number%10)
    # 50~59
    elif number < 60:
        front = "fifty "
        if number%10 == 0:
            return front
        else:
            return front + singleDigit(number%10)
    # 60~69
    elif number < 70:
        front = "sixty "
        if number%10 == 0:
            return front
        else:
            return front + singleDigit(number%10)
    # 70~79
    elif number < 80:
        front = "seventy "
        if number%10 == 0:
            return front
        else:
            return front + singleDigit(number%10)
    # 80~89
    elif number < 90:
        front = "eighty "
        if number%10 == 0:
            return front
        else:
            return front + singleDigit(number%10)
    # 90~99
    elif number < 100:
        front = "ninty "
        if number%10 == 0:
            return front
        else:
            return front + singleDigit(number%10)
                
                
def threeDigit(number):
    nHundred = int(number/100)
    front = str(singleDigit(nHundred)) + " hundred"
    two_digit = number - nHundred*100
    if two_digit >= 10:
        return front + " " + twoDigit(two_digit)
    elif two_digit < 10 and two_digit > 0:
        return front + " " + singleDigit(two_digit)
    return front
    
#4-6 digit, ten, hundred thousand...
def thousand(number):
    nThousand = int(number/1000)
    num_digits = len(str(nThousand))
    #check if num_digits = 1 => thousand
    if num_digits == 1:
        front = str(singleDigit(nThousand)) + " thousand "
    
    #if num_digits = 2 => ten/twenty/thirty/fourty... thousand
    if num_digits == 2:
        front = str(twoDigit(nThousand)) + " thousand "
    
    #if num_digits = 3 => hundred thousand
    if num_digits == 3:
        front = str(threeDigit(nThousand)) + " thousand "
        
    three_digit = number - nThousand*1000
    if three_digit < 1000 and three_digit > 99:
        return front + str(threeDigit(three_digit))
    elif three_digit < 100 and three_digit > 9:
        return front + str(twoDigit(three_digit))
    elif three_digit < 10 and three_digit > 0:
        return front + str(singleDigit(three_digit))
    else:
        return front

#7-9 digit, ten, hundred million...
def million(number):
    nMillion = int(number/1000000)
    num_digits = len(str(nMillion))
    #check if num_digits = 1 => million
    if num_digits == 1:
        front = str(singleDigit(nMillion)) + " million "
    
    #if num_digits = 2 => ten/twenty/thirty/fourty... million
    if num_digits == 2:
        front = str(twoDigit(nMillion)) + " million "
    
    #if num_digits = 3 => hundred million
    if num_digits == 3:
        front = str(threeDigit(nMillion)) + " million "
        
    if num_digits >= 4 and num_digits <= 6:
        front = str(thousand(nMillion)) + " million "
        
    n_digit = number - nMillion*1000000
    if n_digit < 1000000 and n_digit > 9999:
        return front + str(thousand(n_digit))
    elif n_digit < 1000 and n_digit > 99:
        return front + str(threeDigit(n_digit))
    elif n_digit < 100 and n_digit > 9:
        return front + str(twoDigit(n_digit))
    elif n_digit < 10 and n_digit > 0:
        return front + str(singleDigit(n_digit))
    else:
        return front

#10-12 digit?, ten, hundred billion...


#13-15 digit?, ten, hundred trillion...

def run(digit, number):
    if digit == 1:
        return singleDigit(number)
    elif digit == 2:
        return twoDigit(number)
    elif digit == 3:
        return threeDigit(number)
    elif digit >= 4 and digit <= 6:
        return thousand(number)
    elif digit >= 7 and digit <= 9:
        return million(number)
    else:
        return "Over Billion"

    
#num can be int or float
def userInput():
    # Get user input as an integer
    user_input = input("Enter an integer: ")

    # Convert the integer to a string
    #user_input_str = str(user_input)

    # Calculate the number of digits
    num_digits = len(user_input)

    print(f"The number of digits in {user_input} is: {num_digits}")
    return user_input, num_digits

# pytest use
def testing(uin):
    if int(uin) < 0:
        print("Input = ", uin, "Output = Not Support Negative Number")
        return "Not Support Negative Number"
    if int(uin) == 0:
        print("Input = ", uin, "Output = Zero")
        return "Zero"
    num_dig = len(str(uin))
    num_str = run(num_dig, int(uin))
    print("Input = ", uin, "Output = ", num_str)
    return num_str

def main():
    uin, num_dig = userInput()
    if int(uin) < 0:
        print("Not Support Negative Number")
        return 
    if int(uin) == 0:
        print("Zero")
        return

    output = run(num_dig, int(uin))
    #output = testing(uin)
    print("Output = ", output)


if __name__ == "__main__":
    main()

