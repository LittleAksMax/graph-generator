
def astar(drawFunction):
    print("A*")
    if len(processes) != 0: # already a process running
        processes[0].terminate() # kill process
        processes.pop() # remove from processes

    #drawFunction()

def bfs(drawFunction):
    print("bfs")
    if len(processes) != 0: # already a process running
        processes[0].terminate() # kill process
        processes.pop() # remove from processes

    #drawFunction()

def dfs(drawFunction):
    print("dfs")
    if len(processes) != 0: # already a process running
        processes[0].terminate() # kill process
        processes.pop() # remove from processes

    #drawFunction() 

def dijkstra(drawFunction):
    print("dijkstra's")
    if len(processes) != 0: # already a process running
        processes[0].terminate() # kill process
        processes.pop() # remove from processes

    #drawFunction()