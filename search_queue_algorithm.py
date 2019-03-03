from collections import deque
search_queue=deque()
graph={"you":['alice','bob','claire'],"bob":['anuj','peggy'],"alice":['peggy'],
       "claire":['thom','jonny'],"anuj":[],"peggy":[],"thom":[],"jonny":[]}

search_queue+=graph["you"]
searched=[]
while search_queue:
    person=search_queue.popleft()
    if person not in searched:
        if person[-1]=="m":
            print("朋友%s是你要找的人"%person)
        else:
            searched.append(person)
            search_queue+=graph[person]


