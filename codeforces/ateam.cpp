#include <iostream> 
#include <string>

using namespace std;

int main() {
    int num_problems;
    cin >> num_problems; 
    cin.ignore(1, '\n');    
    int num_solved = 0;
    
    for (int i = 0; i < num_problems; i++){
        string line;
        getline(cin, line);
        int count = 0;
        for (int j = 0; j < line.size(); j++){
            if(line[j] == '1') count++; 
        } 
        if (count >= 2){
           num_solved ++; 
        }
    }

    cout << num_solved << endl;;
}

