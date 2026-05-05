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
    bool hasCycle(ListNode* head) {
        std::unordered_set<ListNode*> set1;
        ListNode* temp = head;
        while (temp != nullptr) {
            if (set1.find(temp) != set1.end()) {
                return true;
            }
            else {
                auto f = set1.insert(temp);
            }
            temp = temp->next;
        }
        return false;
    }
};
