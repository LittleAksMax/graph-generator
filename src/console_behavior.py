import generation
import draw
import algorithm

funcs = {
    "Breadth First Search (BFS)": algorithm.bfs,
    "Depth First Search (DFS)": algorithm.dfs,
    "Dijkstra's": algorithm.dijkstra,
    "A*": algorithm.astar
}

def visualizeBtnClicked(console, chosenAlgorithm):
    console.hide()
    funcs[chosenAlgorithm](draw.visualize)
    console.show()

def generateBtnClicked(nodeCount, edgeCount):
    generation.generate(nodeCount, edgeCount) 

def nodeSliderValueChanged(slider, edgeSlider, valueLabel):
    edgeSlider.setMaximum(slider.value() * (slider.value() - 1) / 2) # this is important, so the edge slider stays in bounds

    newValue = str(slider.value())
    valueLabel.setText(newValue)

def edgeSliderValueChanged(slider, valueLabel):
    newValue = str(slider.value())
    valueLabel.setText(newValue)
