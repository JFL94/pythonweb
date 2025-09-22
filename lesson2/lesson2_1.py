def add(a, b):
    result = a + b
    return result   #回傳值至呼叫add function位置

def main():
    x = 10
    y = 20
    sum_result = add(x, y)  #呼叫add function 
    print(f"{x} + {y} = {sum_result}") #回傳值至呼叫mian function位置

if __name__ == "__main__":
    main()  #呼叫mian function (程式起始點)
else:
    print("這不是python直接執行")