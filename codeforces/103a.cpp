#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cin >> n;
    
    int min=101, max=-1, num;
    int b=0, s=0;
    
    for(int i = 0; i < n; i++){
		cin >> num;
        if(num > max){
            max = num;
            b = i;
        }
        if(num <= min){
            min = num; 
            s = i;
        }
    }

    if(s == b){
        cout << 0 << endl;
    }
    else if(b < s){ // swap small first
        cout <<  b + (n - 1 - s) << endl;            
    }
    else{
        cout << b + (n - 1 - s) - 1 << endl;
    }
    
    return 0;
}
