import intcode
import sys
code = [int(i) for i in sys.stdin.read().split(",")]

print(intcode.intcode(code, [1]))
print(intcode.intcode(code, [2]))
