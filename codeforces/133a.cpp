#include <iostream>
#include <string>


int main(){
    std::string input;
    std::getline(std::cin, input);
    if(input.find("H") != -1 || input.find("Q") != -1 || input.find("9") != -1) 
        std::cout << "YES" << std::endl;
    else 
        std::cout << "NO" << std::endl;
}
