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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *tmp = head;

        while (tmp && (n > 0)) {
            tmp = tmp->next;
            n = n - 1;
        }

        ListNode *tmp_head = head;
        ListNode *prev = nullptr;
        while (tmp != nullptr) {
            prev = tmp_head;
            tmp_head = tmp_head->next;
            tmp = tmp->next;
        }

        if (prev != nullptr) {
            prev->next = tmp_head->next;
        } else {
            head = head->next;
        }

        return head;
    }
};
