def calculate(num1, num2, op):
    """根据运算符计算结果，返回结果字符串。"""
    match op:
        case "+":
            return f"{num1} + {num2} = {num1 + num2}"
        case "-":
            return f"{num1} - {num2} = {num1 - num2}"
        case "*":
            return f"{num1} * {num2} = {num1 * num2}"
        case "/":
            if num2 == 0:
                return "错误：除数不能为 0"
            return f"{num1} / {num2} = {num1 / num2}"
        case _:
            return "无法计算：仅支持 + - * /"

while True:
    try:
        num1 = float(input("请输入第一个数："))
        op = input("请输入运算符号（+ - * /）：")
        num2 = float(input("请输入第二个数："))
        break                      # 全部成功才离开循环
    except ValueError:
        print("输入错误，请输入数字，请重新输入。\n")

print(calculate(num1, num2, op))
