/*
    p9012 괄호 s4
    스택 2개를 통해서 스택에 남으면 통과하는 식으로 풀었다.
    어떤 사람은 처음부터 "("개수 ")"개수를 하나하나 세면서 풀었는데 그게 더 효율적이다. 
 */

#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    stack<char> stack1, stack2;
    int T;
    string p;

    cin >> T;

    for(int i = 0; i < T; i++){
        cin >> p;

        if(p.length() % 2 == 1){
            cout << "NO" << '\n';
            continue;
        }

        for(int j = 0; j < p.size(); j++){
            stack1.push(p.at(j));
        }

        while(!stack1.empty()){

            stack2.push(stack1.top());
            stack1.pop();

            while(true){
                if(stack2.empty() || stack1.empty())
                    break;
                
                if(stack1.top() == '(' && stack2.top() == ')'){
                    stack1.pop();
                    stack2.pop();
                }else{
                    break;
                }
            }
        }

        if(!stack2.empty()){
            cout << "NO" << '\n';
        }else{
            cout << "YES" << '\n';
        }

        while(!stack1.empty())
            stack1.pop();
        
        while(!stack2.empty())
            stack2.pop();
    }

}