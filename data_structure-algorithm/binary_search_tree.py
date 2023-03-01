class Node:
    def __init__ (self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None

class binary_search_tree:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        if self.root == None:
            self.root=Node(value)
            return
        else:
            self._insert(value,self.root)
    
    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=Node(value)
                cur_node.left_child.parent=cur_node
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
            if(cur_node.right_child ==None):
                cur_node.right_child=Node(value)
                cur_node.right_child.parent=cur_node
            else:
                self._insert(value,cur_node.right_child)
    
    def display(self):
        if(self.root != None):
            self._display(self.root)
    
    def _display(self,cur_node):
        if(cur_node != None):
            self._display(cur_node.left_child)
            print(str(cur_node.value),end=" ")
            self._display(cur_node.right_child)

    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,cur_node,cur_height):
        if cur_node == None: return cur_height
        left_height=self._height(cur_node.left_child,cur_height+1)
        right_height=self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)

    def find(self,value):
        if self.root!=None:
            return self._find(value,self.root)
        else:
            return None

    def _find(self,value,cur_node):
        if value==cur_node.value:
            return cur_node
        elif value<cur_node.value and cur_node.left_child != None:
            return self._search(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child != None:
            return self._search(value,cur_node.right_child)
        return None

    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,cur_node):
        if value==cur_node.value:
            return True
        elif value<cur_node.value and cur_node.left_child != None:
            return self._search(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child != None:
            return self._search(value,cur_node.right_child)
        return False

    def delete_value(self,value):
        return self.delete_node(self.find(value))
    
    def delete_node(self,node):
        #return the node with the minimum value
        def min_value_node(n):
            cur=n
            while cur.left_child!= None:
                cur=cur.left_child
            return cur

        #return the number of children in a specificed node
        def num_children(n):
            num_children=0
            if n.left_child!= None:
                num_children+=1
            if n.right_child!= None:
                num_children+=1
            return num_children

        node_parents=node.parent
        node_children=num_children(node)

        #break the number of cases based on the structure of the tree and node to be deleted
        #CASE 1 (Node without children):
        if node_children==0:
            if node_parents.left_child==node:
                node_parents.left_child=None
            else:
                node_parents.right_child=None

        #CASE 2(Node with only 1 child):
        if node_children==1:
            #get the single child node
            if node.left_child!=None:
                child=node.left_child
            else:
                child=node.right_child
            
            #replace the node to be deleted with its child
            if node_parents.left_child==node:
                node_parents.left_child=child
            else:
                node_parents.right_child=child
            
            #correct the parent pointer in node
            child.parent=node_parents
        
        #CASE 3(Node with 2 children):
        if node_children==2:
            #get the inorder sucessor of the deleted node:
            successor=min_value_node(node.right_child)
            
            #copy the inorder sucessor's value to the node formerly holding the value we wished 
            #to delete
            node.value=successor.value

            #delete the inorder sucessor now that it's value was copied into the other node 
            self.delete_node(successor)

def fill_tree(tree,num_elements=100,max_int=1000):
    from random import randint
    for _ in range(num_elements):
        cur_elem=randint(0,max_int)
        tree.insert(cur_elem)
    return tree

tree=binary_search_tree()
tree=fill_tree(tree)
tree.insert(10)

print("the tree is:")
tree.display()

print()
print("\nthe result for search 10 and search 30 consecutively are:",end="\n")
print(tree.search(10))
print(tree.search(30))

print("\ntree hight:%s" %str(tree.height()))