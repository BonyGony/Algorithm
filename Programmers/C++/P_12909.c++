#include<string>
#include <iostream>
#include <vector>


using namespace std;

bool solution(string s)
{
    vector<char> arr;
    
    for(int i=0;i < s.length();i++){
        arr.push_back(s[i]);
        
        if(arr.size() >= 2){
            int leng = arr.size();
            
            if(arr[leng-2] == '(' && arr[leng-1] == ')'){
                arr.pop_back();
                arr.pop_back();
            }
        }
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    cout << arr.back() << endl;
    if(arr.size() > 0){
        return false;
    } else {
        return true;
    }
}