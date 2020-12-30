/*
    Name: Josh Norman 
    Date: Dec 30, 2020

    Course: TA Training 

    Objective: This is a primitive example of Class Unit Testing with 
    Gradescope. This is a simple class based program that will allow 
    for unit testing. This file will respresent the Autograders Driver 
    file. This file should be within the zip file and is used by run_test.py

*/

#include <iostream>
#include "example3.h"

using namespace std; 

int main( int argc, char *argv[]){
    
    if( atoi( argv[1]) == 0){
        example3 test;
        cout<<test.welcomeString()<<endl;
    }
    else if( atoi( argv[1]) == 1){
        example3 test2("Josh");
        cout<<test2.welcomeString()<<endl; 
    }
     else if( atoi( argv[1]) == 2){
        example3 test3("Dr. Plaue");
        cout<<test3.welcomeString()<<endl; 
    }  

    return 0; 
}