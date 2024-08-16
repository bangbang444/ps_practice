#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*
    풀이 2
    vector로 풀어보기
    문제가 됐던 부분은 length()의 타입이 int가 아니었기 때문에 int형하고 비교가 되지 않았다. 
*/

int main()
{
    vector<string> V(5);
    string input;
    int max_length = -1;

    for(int i = 0; i < 5; i++){
        cin >> V[i];
        
        if(max_length < int(V[i].length())){
            max_length = int(V[i].length());
        }        
    }

    for(int i = 0; i < max_length; i++){
        for(int j = 0; j < 5; j++){ 
            if(i < int(V[j].length()))
                cout << V[j].at(i);
        }
    }
}


/*
    풀이 1
    배열을 미리 하나하나 -1로 초기화 한 후
    한 줄 입력 할 때마다 최대 길이 저장
    그 후 -1 만나면 패스, 아니면 출력하는 식으로 했다.
 */

// int main()
// {
//     char arr[5][15];
//     string input;

//     int input_length;
//     int max_length = 0;

//     fill_n(&arr[0][0], 5 * 15, -1);

//     for(int i = 0; i < 5; i++){
//         for(int j = 0; j < 15; j++){
//             arr[i][j] = -1;
//         }
//     }

//     for(int i = 0; i< 5; i++){
//         cin >> input;
        
//         input_length = input.length();

//         if(max_length < input_length){
//             max_length = input_length;
//         }

//         for(int j = 0; j < input_length; j++){
//             arr[i][j] = input[j];
//         }
//     }

//     for(int i = 0; i < max_length; i++){
//         for(int j = 0; j < 5; j++){
//             if(arr[j][i] == -1 || arr[j][i] == '\0'){
//                 continue;
//             }
//             cout << arr[j][i];

//         }
//     }

// }