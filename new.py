while True:
        num1=int(input("Enter a number:"))
        num2=int(input("Enter another number:"))

        action=str(input("choose action: Add(a),Sub(s),Mul(m),Div(d)->"))
        print("The result is",end="")
        if action=="a":
                print(num1+num2)
        elif action=="s":
                 print(num1-num2)
        elif action=="m":
                print(num1*num2)
        else:
            print(num1/num2)
            break
