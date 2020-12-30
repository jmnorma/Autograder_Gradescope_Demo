/*
    Name: Josh Norman 
    Date: Dec 23, 2020

    Course: TA Training 

    Objective: This is a primitive example of Unit Testing C++ Code using Gradescope.
    This will be a simple class will represent a students submission. This Autograder 
    will use a common driver file test each function individually. Therefore, the 
    students do not to need to include a driver unless to show addition features or 
    show their testing methods.

*/

#ifndef EXAMPLE3_H
#define EXAMPLE3_H

#include <stdio.h>
#include <iostream>

using namespace std;

class example3{
    public: 
        example3(); // Default Constructor 
        example3( string name ); // Parameter Based Constructor 
        string welcomeString(); // Return the private variable 

    private: 
        string exampleName; 

};

#endif