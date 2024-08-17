/*
 *  p2563 색종이 s5
 */

#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int white_paper[101][101] = {-1,};
    int paper;
    int area = 0;
    int x, y;

    cin >> paper;

    for(int i = 0; i < paper; i++){
        cin >> x >> y;

        for(int j = x; j < x+10; j++){

            if(j >= 100)
                break;
            
            for(int k = y; k < y+10; k++){
                
                if(k >= 100)
                    break;
                
                if(white_paper[j][k] != 1){
                    white_paper[j][k] = 1;
                    area += 1;
                }
            }
        }
    }
    cout << area;

}