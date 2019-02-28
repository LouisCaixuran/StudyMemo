class Node():
    def __init__(self,value=None,lchild=None,rchild=None):
        self.value=value
        self.lchild=lchild
        self.rchild=rchild


class BTree():
    def __init__(self,root=Node()):
        self.root=root
        self.lists=[]

    def add(self,new):
        if self.root.value==None:
            self.root=Node(new)
        else:
            stack=[]
            stack.append(self.root)
            while stack:
                node=stack.pop(0)
                if node.lchild==None:
                    node.lchild=Node(new)
                    return
                elif node.rchild==None:
                    node.rchild=Node(new)
                    return
                else:
                    stack.append(node.lchild)
                    stack.append(node.rchild)

    def front_digui(self,root):
        if root==None or root.value==None:
            return
        else:
            self.lists.append(root.value)
            self.front_digui(root.lchild)
            self.front_digui(root.rchild)

    def mid_digui(self,root):
        if root==None or root.value==None:
            return
        else:
            self.mid_digui(root.lchild)
            print(root.value)
            self.mid_digui(root.rchild)


    def back_digui(self,root):
        if root==None or root.value==None:
            return
        else:
            self.back_digui(root.lchild)
            self.back_digui(root.rchild)   
            print(root.value)

    def show(self):
        self.front_digui(self.root)
        i=1
        j=0
        k=1
        l=[]
        while i<=len(self.lists):
            l.append(self.lists[i-1])
            if k ==2**j:
                j+=1
                print l
                l=[]
                k=0
            k+=1
            i+=1
        print l



                



        
t=BTree()
t.add(8)
t.add(9)
t.add(15)
t.add(20)
t.add(2)
t.add(13)
t.add(14)
t.add(25)
t.show()


