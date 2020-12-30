/*
    Name: Josh Norman 
    Date: Dec 23, 2020

    Course: TA Training 

    Objective: This is a primitive example of Class Unit Testing with 
    Gradescope. This is a simple class based program that will allow 
    for unit testing. This file will respresent the student's driver 
    file. While this file will not be used within this implementation 
    of the Autograder. It is important to ask students to submit this 
    file as proof of testing on their end.

*/

#include <iostream>
#include "example3.h"

using namespace std; 

int main(){
    
    example3 test;
    example3 test2("Josh");

    cout<<test.welcomeString()<<endl;
    cout<<test2.welcomeString()<<endl; 
    
    return 0; 
}