from collections import deque

bank = deque(["x","y","z"])

print(bank)

bank.popleft()
print(bank)
bank.popleft()
bank.popleft()

if not bank:
    print("No person left")