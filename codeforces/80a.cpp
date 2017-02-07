#include <iostream>
using namespace std;


int main(){
    int n;
    cin >> n;
    
    int diff = n - 10; 

    if(diff <= 0 || diff > 11){
        cout << 0 << endl;
    }
    else if (diff == 10){
        cout << 15 << endl;
    }
    else{
        cout << 4 << endl;
    }

}


