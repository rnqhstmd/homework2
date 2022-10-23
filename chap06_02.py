def isStackFull():
    global size,stack,top
    if(top >= size-1):
        return True
    else:
        return False
def isStackEmpty():
    global size,stack,top
    if(top == -1):
        return True
    else:
        return False
def push(data):
    global size,stack,top
    if(isStackFull()):
        return
    top += 1
    stack[top] = data
def pop():
    global size,stack,top
    if (isStackEmpty()):
        return
    data = stack[top]
    stack[top] = None
    top = -1
    return data
def peek():
    global size,stack,top
    if(isStackEmpty()):
        return None
    return stack[top]
size = 100
stack = [None for _ in range(size)]
top = -1

if __name__=="__main__":
    with open("진달래꽃.txt",'r',encoding='UTF8')as rfp:
        lineAry = rfp.readlines()

    print("---원본---")
    for line in lineAry:
        push(line)
        print(line,end='')
    print()

    print("거꾸로 처리된 결과---")
    while True:
        line = pop()
        if line ==None:
            break
        miniStack = [None for _ in range(len(line))]
        miniTop = -1

        for ch in line:
            miniTop += 1
            miniStack[miniTop] = ch
        while True:
            if miniTop == -1:
                break
            ch = miniStack[miniTop]
            miniTop -= 1
            print(ch,end='')