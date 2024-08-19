/*
    p10773 제로 s4
    STL 써서 풀기
*/

#include <iostream>
#include <stack>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    stack<int> stack;

    int N;
    int K;
    int sum = 0;
    int size;

    cin >> N;

    for(int i = 0; i < N; i++){
        cin >> K;
        if(K == 0){
            stack.pop();
        }else{
            stack.push(K);
        }
    }

    size = stack.size();

    for(int i = 0; i < size; i++){
        sum += stack.top();
        stack.pop();
    }

    cout << sum;
}