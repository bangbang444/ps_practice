// 아직 못 풂
#include <iostream>
#include <map>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    int card;
    map<int, int> map;

    cin >> N;

    for(int i = 0; i < N; i++){
        cin >> card;
        if(map.find(card) != map.end()){
            continue;
        }
        map.insert(card, 1);
    }

    cin >> M;

    for(int i = 0; i < M; i++){
        cin >> card;
        if(map.find(card) != map.end()){
            cout << 1 << ' ';
        }else{
            cout << 0 << ' ';
        }
    }

    return 0;
}