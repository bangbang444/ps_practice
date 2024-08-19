// 아직 못 풂

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int check(string row){
    
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); 

    int count = 0;
    int row, column;
    string chess_row;
    char standard, other;
    
    cin >> row >> column;

    cin >> chess_row;
    if(chess_row.at(0) == 'B'){
        standard = 'B';
        other = 'W';
    }else{
        standard = 'W';
        other = 'B';
    }

    for(int j = 0; j < column; j++){
        if(j%2 == 0 && chess_row.at(j) == standard)
            continue;
        if(j%2 == 1 && chess_row.at(j) == other)
            continue;
        count++;
    }

    swap(standard, other);


    for(int i = 1; i < row; i++){
        cin >> chess_row;
        for(int j = 0; j < column; j++){
            if(j%2 == 0 && chess_row.at(j) == standard)
                continue;
            if(j%2 == 1 && chess_row.at(j) == other)
                continue;
            count++;
        }
        swap(standard, other);
    }

    cout << count;

}