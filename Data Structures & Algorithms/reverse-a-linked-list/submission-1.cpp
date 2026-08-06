/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void printNode(ListNode *node) {
        if (node) {
            cout << node->val;
        } else {
            cout << "NULL";
        }
    }
    ListNode* reverseList(ListNode* head) {
        ListNode *prev, *cur, *next;
        
        prev = NULL;
        cur = head;

        while (cur != NULL) {
            /* Save next pointer. */
            next = cur->next;

            /* Adjust next pointer of current node as prev. */
            cur->next = prev;

            /* Move ahead. */
            prev = cur;
            cur = next;
        }
        return prev;
    }
};
