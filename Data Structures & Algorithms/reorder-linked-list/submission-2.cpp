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
    void reorderList(ListNode* head) {
        ListNode *slow = head;
        ListNode *fast = head->next;

        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode *head1, *head2;
        head2 = slow->next;
        slow->next = nullptr;

        ListNode *prev, *cur, *next;
        prev = nullptr;
        cur = head2;
        while (cur != nullptr) {
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }

        head1 = head;
        head2 = prev;

        while (head2 != nullptr) {
            ListNode *h1_next, *h2_next;
            h1_next = head1->next;
            h2_next = head2->next;

            head1->next = head2;
            head2->next = h1_next;

            head1 = h1_next;
            head2 = h2_next;
        }
    }
};
