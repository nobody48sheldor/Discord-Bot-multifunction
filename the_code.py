from io import StringIO
import sys
sys.stdout = buffer = StringIO()
a = 15
for i in range(10):
    a = a+10*i
    print(a)
def main():
    return(buffer.getvalue())