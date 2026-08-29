num1=float(input("请输入第一个数："))

opener=input("请输入运算符号（‘+’‘-’‘*’‘/’）")
num2=float(input("请输入第二个数："))
match opener:
    case "+":
        print(f"{num1}+{num2}={num1+num2}")
    case "-":
        print(f"{num1}-{num2}={num1-num2}")
    case "*":
        print(f"{num1}*{num2}={num1*num2}")
    case "/" if num2!=0:
        print(f"{num1}/{num2}={num1/num2}")
    case _:
        print("符号输入错误")
