def dfs_pre_order(self):
    results = []  # create an empty list to store the values of visited nodes
 
    def traverse(current_node):
        # append the value of the current node to the results list
        results.append(current_node.value)
 
        # if the current node has a left child, recursively traverse it
        if current_node.left is not None:
            traverse(current_node.left)
 
        # if the current node has a right child, recursively traverse it
        if current_node.right is not None:
            traverse(current_node.right)
 
    # start the pre-order traversal from the root of the tree
    traverse(self.root)
 
    # return the list of visited node values
    return results

def dfs_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results


#kth smallest Node,
#example, for tree contains the element [1,2,3,4,5], the 3rd smallest element returns 3

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def dfs_in_order(self):
        if self.root is None:
            return None
        
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
        
        
    def kth_smallest(self,k):
        results = self.dfs_in_order()
        if results is None:
            return None
        if k <= 0  or k > len(results):
            return None
        return results[k-1]
