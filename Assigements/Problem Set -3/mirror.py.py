class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
        
    return (root1.value == root2.value) and isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)

def isSymmetric(root):
    if root is None:
        return True
    return isMirror(root.left, root.right)

def buildTree(nodes):
    if not nodes:
        return None
        
    root = TreeNode(int(nodes[0]))
    queue = [root]
    i = 1
    
    while queue and i < len(nodes):
        node = queue.pop(0)
        
        if nodes[i] != 'None':
            node.left = TreeNode(int(nodes[i]))
            queue.append(node.left)
        i += 1
            
        if i < len(nodes) and nodes[i] != 'None':
            node.right = TreeNode(int(nodes[i]))
            queue.append(node.right)
        i += 1
                
    return root

def read_input(file_name):
    with open(file_name, 'r') as f:
        nodes = f.read().split()
    return nodes

def write_output(file_name, result):
    with open(file_name, 'w') as f:
        f.write(result)

if __name__ == "__main__":
    input_nodes = read_input('input.txt')
    root = buildTree(input_nodes)
    result = "True" if isSymmetric(root) else "False"
    write_output('output.txt', result)


