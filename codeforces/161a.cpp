#include <iostream>

using namespace std;

int main(){
    int row = 0;
    int dig;
    for(int i = 0; i < 25; i ++){
        if (i % 5 == 0 && i > 0) row++;
        cin >> dig;
        if (dig == 1){
            cout << abs(2 - row) + abs((i % 5) - 2) << endl;
            return 0;
        }
    }
}
