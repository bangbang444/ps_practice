/*
    p1193 분수찾기 s5
 */

#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int numerator = 1; // 분자
    int denominator = 1; // 분모
    int input;
    bool is_odd = true;

    cin >> input;

    if(input == 1){
        cout << numerator << "/" << denominator;
        return 0;
    }

    while(input != 1){
        if(denominator == 1){
            denominator = numerator + denominator;
            numerator = 1;
            is_odd = !is_odd;
        }else{
            denominator--;
            numerator++;
        }
        input--;
    }

    if(is_odd == false)
        cout << numerator << "/" << denominator;
    else
        cout << denominator << "/" << numerator;
    return 0;
}