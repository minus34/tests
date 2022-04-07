import time

start_time = time.time_ns()

# standard iteration approach : 0.23 ms
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
