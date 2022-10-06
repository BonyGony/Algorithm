#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    
    sort(phone_book.begin(), phone_book.end());
    
    for(int i=1;i<phone_book.size();i++){
        if(phone_book[i].compare(0,phone_book[i-1].size(), phone_book[i-1]) == 0){
            answer = false;
        }
    }
    
    return answer;
}