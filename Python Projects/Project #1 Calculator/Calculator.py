
# PROJECT 1
## Calculator

Cal_n = 0

def User_input():
    global Cal_n
    Cal_n += 1

    print("#"*10, "Calculator #", Cal_n, "#"*10, "\n#")
    Input = str(input("#  Type Number :"))

    Calculate(Input)

def Calculate(Uinput):
        global Cal_n

        result = eval(Uinput)
        print("# ", result)

        Next = input("#  Continue? Yes / No: ")
        print("#")
        
        if Next == "Yes" or Next == "yes":
            User_input()
        elif Next == "No" or Next == "no" or Next == "NO":
            print("#"*8, "Close Calculator", "#"*8, "\n\n\n")
            Cal_n = 0

print("\n\n")
User_input()