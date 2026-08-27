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
private:
    ListNode *res = nullptr;
    ListNode *res_tail = nullptr;

public:
    void addNodeToRes(ListNode *node) {
        if (res == nullptr) {
            res = res_tail = node;
        } else {
            res_tail->next = node;
            res_tail = res_tail->next;
        }
    }

    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        if (list1 == nullptr) {
            return list2;
        }        
        if (list2 == nullptr) {
            return list1;
        }

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                addNodeToRes(list1);
                list1 = list1->next;
            } else {
                addNodeToRes(list2);
                list2 = list2->next;
            }
        }

        if (list1) {
            res_tail->next = list1;
        } else {
            res_tail->next = list2;
        }

        return res;
    }
};
