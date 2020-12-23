/*
    Name: Josh Norman 
    Date: Dec 23, 2020

    Course: TA Training 

    Objective: This is a primitive example of user input using Gradescope.
    This will be a simple echo program to repeat the users input to standard out.
    This file will represent the students submission. We will use this file 
    to Test our Autograder. 

*/

#include "iostream"
#include "string.h"

using namespace std; 

int main(){
    
    string input = "";
    cout<<"Please type a string to be repeated"<< endl; 

    cin>>input;
    cout<<"Echo: "<<input<<endl; 
    
    return 0; 
}