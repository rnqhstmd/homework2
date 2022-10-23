from ctypes import sizeof
import queue
def isQueueFull():
    global size,queue,front,rear
    if((rear+1) % size == front):
        return True
    else:
        return False
def isQueueEmpty():
    global size,queue,front,rear
    if(front == rear):
        return True
    else:
        return False
def enQueue(data):
    global size,queue,front,rear
    if (isQueueFull()):
        print("큐가 꽉 찼습니다")
        return
    rear = (rear+1)%size
    queue[rear] = data
def deQueue():
    global size,queue,front,rear
    if(isQueueEmpty()):
        print("큐가 비었습니다")
        return None
    front = (front+1)%size
    data = queue[front]
    queue[front] = None
    return data
def peek():
    global size,queue,front,rear
    if(isQueueEmpty()):
        print("큐가 비었습니다")
        return None
    return queue[(front+1)%size]
def calcTime():
    global size,queue,front,rear
    tiemSum = 0
    for i in range((front+1)%size,(rear+1)%size):
        timeSum += queue[i][1]
        return tiemSum
size = 6
queue = [None for _ in range(size)]
front = rear = 0

if __name__=="__main__":
    Call = [('사용',9),('고장',3),('환불',4),('환불',4)('고장',3)]
    for call in Call:
        print("대기 예상시간은",calcTime(),"분입니다.")
        print("현재 대기 콜>>",queue)
        enQueue(call)
        print()
    print("최종 대기 콜>>",queue)
    print("프로그램 종료!")