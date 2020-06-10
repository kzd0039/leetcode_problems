class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBlanced(self):
        pass

    def treeHeight(self,root, h=0):
        if not root:
            return h
        return max(self.treeHeight(root.left, h+1), self.treeHeight(root.right, h+1))


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # print(root.treeHeight(root))



if __name__ == '__main__':
    main()