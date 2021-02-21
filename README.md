# graph-generator
A graph generator using the Erdős-Rényi random graph generation model - made in pygame, and a console in pyqt5.

Sources:
* <https://youtu.be/PvYwkFsHFg8> 
* <http://www.sciweavers.org/free-online-latex-equation-editor>
  * This is for the mathematical equations 

## Generation

### The Erdős-Rényi random graph generation model
* completely unbiased randomization
* You are given the following parameters:
  * The number of nodes (***n***)
  * The probability threshold of an edge (***p***)
* randomly create ***n*** nodes (possibly by assigning a random *(x, y)* co-ordinate to each node)
* join up every node with every other node in the network, creating a full mesh
  * there are *n(n-1)* possible edges, but we must divide by *2!* (which is just *2*) to remove the duplicate connections

![equation](https://bit.ly/3qH8pcF)

* go through every single edge, and generate a random number (***r***) where *0 ≤ **r** ≤ 1*

* if ***r < p***, the edge is ignored, else, the edge is kept
* this should leave us with a graph with ***n*** nodes, and approximately

![equation](http://www.sciweavers.org/tex2img.php?eq=p%20%5Ctimes%20%20%5Cfrac%7Bn%28n-1%29%7D%7B2%7D%20%3D%20%5Cfrac%7Bpn%28n-1%29%7D%7B2%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

##### NOTE: maybe the number of edges (***e***) is given instead, however ***p*** can be calculated by using the maximum number of edges, however some compensation will have to be done, as doing the method will not necessarily give you exactly ***e*** edges
![equation](https://bit.ly/3bqIgIL)

##### NOTE: when generating, it would be more efficient to go through and check whether the edge is kept if you generate a random number and compare it to ***p*** there when considering the edge, rather than creating a full mesh and then going through the edges again

## Algorithms 

### Breadth First Search (DFS)

### Depth First Search (DFS)

### Dijkstra's

### A*

## Graphics
* OpenGL and Pygame
  * Allows client to pan around the plane 

### Console
* made in PyQt5
* Will have 2 menu bars
  * graph controller (generate new graph, visualize/run, algorithm dropdown)
  * visualization controls (skip, end, reset)
* Will be hidden during visualization, and reappear after it is finished

### Pathfinding Visualization
* each algorithm will have an *open set* and a *closed set*
* the start node will be <span style="color:orange">*orange*</span>
* the end node will be <span style="color:cyan">*cyan*</span>
* unvisited nodes will be a *white* (on a *black* background)
* nodes on the front (*open set*) will be <span style="color:green">*green*</span>
* nodes that have already been considered/visited (*closed set*) will be <span style="color:red">*red*</span>
* at the end, the nodes that consist of the path from start to end will be <span style="color:purple">*purple*</span>

* during visualization, the client can:
  * skip (only draw at the end)
  * end (exit the current visualization)
  * reset (go back to untouched graph)
* once the visualization is complete, the client can press *Enter*, to exit the visualization and show the console again 
