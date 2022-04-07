
# Objective:
# 1. If the number is divisible by 3, print Fizz instead of the number
# 2. If the number is divisible by 5, print Buzz instead of the number
# 3. If the number is divisible by 3 and 5 both, print FizzBuzz instead of the number

import time


def main():
    start_time = time.time_ns()

    # iteration approach : 0.23 ms
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if len(output) > 0:
            print(output)
        else:
            print(f"{i}")

    # lambda approach : 0.23 ms
    # print(*map(lambda i: 'Fizz'*(not i % 3)+'Buzz'*(not i % 5) or i, range(1, 101)), sep='\n')

    time_taken = float(time.time_ns() - start_time) / 1000000.0

    print(f"\nTime taken: {time_taken} ms")


if __name__ == '__main__':
    main()
