class Solution {
    public:
    vector<int> inorderNodes;

// 二分探索木のノードの有無の確認
    void inorderTraversal(TreeNode*root){
        if (root == NULL) {
            return;
        }
// 二分探索木
        inorderTraversal(root -> left);
        inorderNodes.push_back(root -> val);
        inorderTraversal(root -> right);
    }

    int minDiffInBST(TreeNode* root) {
        inorderTraversal(root);

        int minDistance = INT_MAX;

        // リストの隣同士の要素の差を求めていき、最小値を出力する。
    for (int i=1; i<inorderNodes.size(); i++) {
        minDistance = min(minDistance, inorderNodes[i] - inorderNodes[i-1]);
    }
    return minDistance;
    }

};g