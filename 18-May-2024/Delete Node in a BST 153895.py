# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,cur):
        if cur:
            ans = []
            ans.extend(self.inorder(cur.left))
            ans.append(cur.val)
            ans.extend(self.inorder(cur.right))

            return ans
        return []
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        inorder_arr =  self.inorder(root)
        def dele(root,key):
            if root:
                # print(root.val,key)
                if root.val > key:
                    res = dele(root.left,key)
                    root.left = res
                    return root
                elif root.val < key:
                    res = dele(root.right,key)
                    root.right = res
                    return root
                else:
                    # print("hi")

                    if not root.left and not root.right:
                        return None
                        # print("hio")
                    elif not root.left or not root.right:
                        if root.left:
                            return root.left
                        else:
                            return root.right
                    else:
                        for i in range(len(inorder_arr) - 1 ):
                            if inorder_arr[i] == root.val:
                                root.val = inorder_arr[i+1]
                                # print("hi")
                                break
                        # print(root.val)
                        val = dele(root.right,root.val)
                        root.right = val
                        return root
            return root
        ans = dele(root,key)
        return ans