/*
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs 
in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers 
in the array and their absolute difference is k.

Example 1:

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
*/


// time: O(n^2)
// space: O(m) -> m: # of unique value in nums.

class Solution{
    public int findPairs(int[] nums, int k){
        
        // count k-diff pairs.
        // count repeats and store in hashmap. 
        int count = 0;
        HashMap<Integer, Integer> cache = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            if (cache.containsKey(nums[i])){
                int temp = cache.get(nums[i]);
                cache.put(nums[i], temp+1);
            }
            else{
                cache.put(nums[i], 1);
            }
        }
        
        // traverse hashmap and check two conditions k == 0 and k > 0.
        // if k == 0 check if duplicates exists for key. 
        for (int num: cache.keySet()){
            if (k > 0 && cache.containsKey(num - k)) count ++;
            else if (k == 0 && cache.get(num) > 1){
                int temp = cache.get(num);
                cache.put(num, temp-1);
                count++;
            }
        }
        return count;
    }
}