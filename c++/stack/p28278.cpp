/*
    p28278 스택 2 s4
    스택에 차있는걸 int변수로 하면 4ms 정도 더 빠름
    STL로 구현
*/

#include <iostream>
#include <stack>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    stack<int> stack;
    int N; // 1 <= N <= 1,000,000
    int command; // 명령
    int value; // push할 값

    cin >> N;

    for(int i = 0; i < N; i++){

        cin >> command;

        switch (command)
        {
        case 1:
            cin >> value;
            stack.push(value);
            break;
        case 2:
            if(stack.size() != 0){
                cout << stack.top() << "\n";
                stack.pop();
            }
            else{
                cout << -1 << "\n";
            }
            break;
        case 3:
            cout << stack.size() << "\n";
            break;
        case 4:
            if(stack.size() == 0){
                cout << 1 << "\n";
            }else{
                cout << 0 << "\n";
            }
            break;
        case 5:
            if(stack.size() == 0){
                cout << -1 << "\n";
            }else{
                cout << stack.top() << "\n";
            }
            break;
        }
    }
}