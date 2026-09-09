/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node *, Node *> hash;
        hash[nullptr] = nullptr;

        Node *tmp = head;
        while (tmp != nullptr) {
            Node *new_node = new Node(tmp->val);
            new_node->val = tmp->val;
            hash[tmp] = new_node;

            tmp = tmp->next;
        }

        tmp = head;

        while (tmp != nullptr) {
            Node *new_node = hash[tmp];
            new_node->next = hash[tmp->next];
            new_node->random = hash[tmp->random];

            tmp = tmp->next;
        }

        return hash[head];
    }
};
