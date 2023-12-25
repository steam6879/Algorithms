from stack import Stack     # import Stack class from stack.py

def recur(n):
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n - 1
            continue    # repeat the while loop

        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n - 2
            continue
        
        break

