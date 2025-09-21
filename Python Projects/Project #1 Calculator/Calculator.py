
# PROJECT 1
## Calculator

Cal_n = 0 # Counter Use

def User_input():
    global Cal_n
    Cal_n += 1

    print("#"*10, "Calculator #", Cal_n, "#"*10, "\n#")
    Input = input("#  Type Number :") # Input Number

    Calculate(Input)

def Calculate(U_input):
        global Cal_n

        result = eval(U_input)
        print("# ", result)

        Next = input("#  Continue? Yes / No: ") # Input Continue or not
        print("#")
        
        if Next.lower == "yes":
            User_input()
        elif Next.lower == "no":
            print("#"*8, "Close Calculator", "#"*8, "\n\n\n")
            Cal_n = 0

print("\n\n")
User_input()