#include <iostream>
#include <stack>
#include <string>

class BrowserHistory {
public:
    std::stack<std::string> prev;
    std::stack<std::string> next;

    BrowserHistory(std::string homepage) {
        prev.push(homepage);
        next = std::stack<std::string>();
    }
    
    void visit(std::string url) {
        prev.push(url);
        next = std::stack<std::string>();
    }
    
    std::string back(int steps) {
        while(steps > 0 && prev.size() > 1){
            next.push(prev.top());
            prev.pop();
            steps--;
        }
        return prev.top();
    }
    
    std::string forward(int steps) {
        while(steps > 0 && next.size() > 0){
            prev.push(next.top());
            next.pop();
            steps--;
        }
        return prev.top();
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */