def Enqueue(queue ,elements):
    queue.append(elements)
    return queue
def Dequeue(queue):
    if len(queue ) >0:
        queue =queue[1:]
        return queue
    else:
        print("Empty")
        return queue



def display(queue):
        print(queue)

queue = [1 ,2 ,3 ,4 ,5]
queue =Enqueue(queue ,6)
display(queue)
queue =Dequeue(queue)
display(queue)
