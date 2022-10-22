#include <iostream>
#include <cmath>



double returnSquare(double squareLength)
{
    return pow(squareLength,2);
}
double returnCube(double cubeLength)
{    
    return cubeLength*cubeLength*cubeLength;
}

void hypotenuse()
{
  
  double sideA;
  double sideB;
  std::cout<<"Please enter Side A's length: ";
  std::cin>>sideA;
  
  std::cout<<"Please enter Side B's length: ";
  std::cin>>sideB;
  
  double hyp=sqrt(pow(sideA,2) + pow(sideB,2)); //Hyp needs to be entered after input.
  std::cout<<"The Hypotenuse is: "<<hyp<<'\n';
  
    
}

void factorial()
{
    int result=1;
    int num;

    std::cout<<"Please enter a number to factorial from: ";
    std::cin>>num;
    for(int i=1;i<=num;i++){
        result=result*i;
    }
    std::cout<<"Factorial result is: "<<result<<'\n';
}
int main(){
  
    std::cout<<"**********************ReturnSquare**********************"<<'\n';
    double squareLength;
    std::cout<<"Please enter the length of a square side: ";
    std::cin>>squareLength;
    double area=returnSquare(squareLength);
    std::cout<<"Area: "<<area<< " cm^2"<<'\n';
    std::cout<<"***************************************************************"<<'\n';
 
    std::cout<<"**********************ReturnCube**********************"<<'\n';
    double cubeLength;
    std::cout<<"Please enter the length of a cube's side: ";
    std::cin>>cubeLength;
    double volume=returnCube(cubeLength);
    std::cout<<"Volume: "<<volume<< " cm^3"<<'\n';
    std::cout<<"************************************************************"<<'\n';
    
    hypotenuse();
    factorial();
  
  return 0;
}
