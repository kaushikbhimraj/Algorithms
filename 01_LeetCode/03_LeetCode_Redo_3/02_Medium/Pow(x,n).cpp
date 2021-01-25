#include <iostream>
#include <bits/stdc++.h>

class Solution {
public:
    double myPow(double x, int n) {
        bool isEven = false;
        
        if (n < 0){
            isEven = (n % 2 == 0) ? true : false;
            n = (n == INT_MIN) ? abs(n+1) : abs(n);
            
            double y = helper(x, n);
            if (x < 0 && isEven) y = abs(y); 
            
            return (double) 1/y;
        }
        else return helper(x, n);
    }
    
    double helper(double x, int n){
        if (n == 0) return 1;
        if (n % 2 == 0) {
            double y = helper(x, (int) n/2);
            return y * y;
        }
        else {
            return x * helper(x, n - 1);
        }
    }
};