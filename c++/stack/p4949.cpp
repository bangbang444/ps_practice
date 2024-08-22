/*
    p4949 균형잡힌 세상 s4
    두 개의 스택으로 top만 비교해서 해결
    주의 - continue할 때 스택 비우기
*/

#include <iostream>
#include <stack>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    stack<char> stack1, stack2;
    string input;
    char ch;

    while(true){
        getline(cin, input);
        if(input.compare(".") == 0){
            break;
        }

        for(int i = 0; i < input.length(); i++){
            
            ch = input.at(i);
            
            if(ch == '(' || ch == ')' || ch == '[' || ch == ']'){ // 괄호들만 stack에 push
                stack1.push(ch);
            }
        }

        if(stack1.size() == 0){ // stack1에 괄호들이 없는 경우
            cout << "yes" << '\n';
            continue;
        }
        
        if(stack1.size() % 2 != 0){ // 괄호 개수가 홀수인 경우
            cout << "no" << '\n';

            while(!stack1.empty())
                stack1.pop();

            continue;
        }

        do{
            
            stack2.push(stack1.top());
            stack1.pop();

            while(!stack1.empty() && !stack2.empty()){
                if(stack1.top() == '(' && stack2.top() == ')'){
                    stack1.pop();
                    stack2.pop();
                    continue;
                }
                else if(stack1.top() == '[' && stack2.top() == ']'){
                    stack1.pop();
                    stack2.pop();
                    continue;
                }
                break;
            }
        }while(stack1.size() > stack2.size());

        if(stack1.empty() && stack2.empty()){ // 두 개의 크기가 0일 때
            cout << "yes" << '\n';
        }else{
            cout << "no" << '\n';
        }
        
        while(!stack1.empty())
            stack1.pop();
    
        while(!stack2.empty())
            stack2.pop();

    }

    return 0;
}