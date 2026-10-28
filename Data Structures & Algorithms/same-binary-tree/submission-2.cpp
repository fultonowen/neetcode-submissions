/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    bool identify(TreeNode* f, TreeNode* s) {
        if (f == nullptr && s == nullptr) {
            return true;
        }
        else if (f == nullptr || s == nullptr) {
            return false;
        }
        return f->val == s-> val && identify(f->left, s->left) && identify(f->right, s->right);
    }
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) return true;
        if (p == nullptr || q == nullptr) return false;
        if (identify(p, q)) return true;
        return isSameTree(p->left, q) || isSameTree(p->right, q);
    }
};
