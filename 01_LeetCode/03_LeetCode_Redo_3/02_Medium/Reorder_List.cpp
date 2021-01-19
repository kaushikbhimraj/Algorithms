#include <iostream>

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

struct ListNode{
    int val;
    ListNode *next;
    ListNode(): val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void reorderList(ListNode* head) {
        // Find the mid value of list. 
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast and fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }

        // From the mid point, reverse the list. 
        ListNode* curr = slow;
        ListNode* prev;
        ListNode* temp;
        while (curr){
            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        // Merge first and second half of the list to get the proper output. 
        ListNode* first = head;
        ListNode* second = prev;
        while (second->next){
            ListNode* temp = first->next;
            first->next = second;
            first = temp;

            temp = second->next;
            second->next = first;
            second = temp;
        }
    }
};