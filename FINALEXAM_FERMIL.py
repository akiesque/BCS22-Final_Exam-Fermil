## STEPHANIE FERMIL | BCS22
## creates a class that symbolizes each node
class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

## defines left to right vertical traversal function
def VOrder_LR(root, column, n):
    ## checks for roots
    if root is None:
        return

    ## appends node
    try:
        n[column].append(root.key)
    except:
        n[column] = [root.key]

    ## recursively calls function for left and right nodes
    ## if node is on the left, subtract one to horizontal distance
    ## if node is on the right, adds one to its horizontal distance
    VOrder_LR(root.left, column - 1, n)
    VOrder_LR(root.right, column + 1, n)

## defines right to left vertical traversal function
def VOrder_RL(root, column, n):
    if root is None:
        return
    try:

        n[column].append(root.key)
    except:
        n[column] = [root.key]

    ## recursively calls function for left and right nodes
    ## if node is on the left, adds one to its horizontal distance
    ## if node is on the right, subtracts one to its horizontal distance
    VOrder_RL(root.right, column - 1, n)
    VOrder_RL(root.left, column + 1, n)

## reverses the order of the functions
def printreverseRL(root):
    lis1 = {}
    rlis2 = []
    dist = 0
    VOrder_LR(root, dist, lis1)

    print("Output:")
    for x, value in enumerate(sorted(lis1)):
        for i in lis1[value]:
            rlis2.append(i)

    print((' \n'.join(str(x) for x in rlis2[::-1])))

def res(root):
    printreverseRL(root)

## defines the main tree
def main():
    ## defines nodes
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    res(root)

## calls main function
main()

