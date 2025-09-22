def add(a, b):
    result = a + b
    return result

def main():
    x = 10
    y = 20
    sum_result = add(x, y)
    print(f"{x} + {y} = {sum_result}")

main()

if __name__ == "__main__":
    print("這是pthon直接執行")
else:
    print("這不是python直接執行")