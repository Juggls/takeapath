#include <string>
#include <iostream>

using namespace std;

int main(){
    string num1, num2, new_num;
    cin >> num1;
    cin >> num2;
    for(int i = 0; i < num1.length(); i++){
        if ((int) (num1.at(i) - '0') + (int)(num2.at(i) - '0') == 1) new_num+="1"; 
        else new_num+="0";
    }
    cout << new_num << endl;
}
