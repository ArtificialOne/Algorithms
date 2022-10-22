#include <iostream>
    
    int main(){
    
    double temp;
    char unit;

    std::cout<<"***************TEMPERATURE CONVERSION***************"<<'\n';
    std::cout<<"F = Fahrenheit"<<'\n';
    std::cout<<"C = Celsius"<<'\n';
    std::cout<<"Please enter unit to convert to: ";
    std::cin>>unit;

    if(unit=='F' || unit=='f'){
        std::cout<<"Enter temperature in Celsius: ";
        std::cin>>temp;
        temp=(1.8*temp)+32;
        std::cout<<"Your converted temp is: "<<temp<<"F"<<'\n';
    }
    else if(unit=='C' || unit=='c'){
        std::cout<<"Enter temperature in Fahrenheit: ";
        std::cin>>temp;
        temp=(9/5*temp)-32;
        std::cout<<"Your converted temp is: "<<temp<<"C"<<'\n';
    }
    else{
        std::cout<<"Please enter only in C or F"<<'\n';
    }
    std::cout<<"******************************"<<std::endl;

    return 0;
    
}
