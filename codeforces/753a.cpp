/*What is the maximal number of children for whose he can give candies if Santa Claus want each kid should get distinct positive integer number of candies. Santa Class wants to give all n candies he has.

Input
The only line contains positive integer number n (1 ≤ n ≤ 1000) — number of candies Santa Claus has.

Output
Print to the first line integer number k — maximal number of kids which can get candies.

Print to the second line k distinct integer numbers: number of candies for each of k kid. The sum of k printed numbers should be exactly n.

If there are many solutions, print any of them
*/


#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    int n;
    cin >> n;
    cin.ignore(1, '\n');

    if (n == 2){
        cout << 1 << endl;
        cout << 2 << endl;
        return 0;
    }

    int sum = 0;
    vector<int> nums_used;
    
    for (int i = 1; i < n + 1; i ++){
        if (sum + i > n){
            int diff = n - sum;
            int last = nums_used.back();
            nums_used.pop_back();
            nums_used.push_back(last + diff);
            break;
        }     
        else if (sum + i == n){
            nums_used.push_back(i);
            break;
        }
        else{
            nums_used.push_back(i);
            sum+= i;
        }
            
    }

    cout << nums_used.size() << endl;
    for (auto x; nums_used){
        cout << x << " ";
    }

    cout << endl;
}
