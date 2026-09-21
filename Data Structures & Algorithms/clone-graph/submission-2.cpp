/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
private:
    unordered_map<Node *, Node *> old_map;
    set<Node *> visited;

public:
    void dfs(Node *node) {
        if (visited.find(node) != visited.end()) {
            return;
        }

        visited.insert(node);
        Node *n_node = new Node(node->val);
        old_map[node] = n_node;

        for (Node *n : node->neighbors) {
            dfs(n);
        }
    }

    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return nullptr;
        }

        dfs(node);

        for (auto &[old_node, n_node] : old_map) {
            for (Node *n : old_node->neighbors) {
                n_node->neighbors.push_back(old_map[n]);
            }
        }

        return old_map[node];
    }
};
