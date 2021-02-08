#include <iostream>
#include <algorithm>
#include <vector>

#include <algorithm>

class Solution{
    public:
    std::vector<std::vector<int>> intervalIntersection(std::vector<std::vector<int>>& firstList, std::vector<std::vector<int>>& secondList){
        std::vector<std::vector<int>> output;
        std::vector<int> temp(2);
        
        int m = firstList.size();
        int n = secondList.size();

        int one = 0;
        int two = 0;

        // Array 1: first value, second value
        // Array 2: frist value, second value
        // when array1 -> first value < array2 -> second value and array1 -> second value > array2 -> first value then we have an intersection. 
        while (one < m && two < n){
            if (secondList[two][0] <= firstList[one][1] && secondList[two][1] >= firstList[one][0]){
                temp[0] = std::max(firstList[one][0], secondList[two][0]);
                temp[1] = std::min(firstList[one][1], secondList[two][1]);
                output.push_back(temp);
            }
            
            if (firstList[one][1] < secondList[two][1]) 
                one++;
            else 
                two++;
        }
        return output;
    }
};

int main(){

}