import ast
from textwrap import indent
NodeID = 0
class Node:
    def __init__(self) -> None:
        self.statements = None
        self.outGoingEdges = list()
        NodeID+=1
        self.NodeNumber = NodeID
NodeList = list()

pythonFile = str(open ('./conditionalStatement.py','r').read())
program = ast.parse(pythonFile)
for node in ast.walk(program):
    print(ast.dump(node,indent=4))
print()