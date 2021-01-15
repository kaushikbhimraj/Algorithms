#include <iostream>
#include <string>
#include <stack>

class Solution{

public:

	struct data {
		char val;
		int count;
	};

	std::string removeDuplicate(std::string s, int k){
		//Create a new stack. 
		std::stack <data> duplicates;
		data newChar;

		newChar.val = s.at(0);
		newChar.count = 1;
		duplicates.push(newChar);

		for (int i = 1; i < s.size(); i++){
			
			if (duplicates.empty() or duplicates.top().val != s.at(i)){
				newChar.val = s.at(i);
				newChar.count = 1;
				duplicates.push(newChar);
			}
			else {
				duplicates.top().count++;
				if (duplicates.top().count == k){
					duplicates.pop();
				}
			}
		}

		std::string res = "";
		while (!duplicates.empty()){
			data temp = duplicates.top();
			std::string substring(temp.count, temp.val);
			res += substring;
			duplicates.pop();
		}
		return res;
	}
};

int main(){
	Solution LC1209;
	std::string s = "deeedbbcccbdaa";
	int k = 3;
	std::cout << LC1209.removeDuplicate(s, k) << std::endl;

}