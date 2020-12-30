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

#include "example3.h"

example3::example3(): exampleName("Test Name") {}

example3::example3( string name): exampleName(name) {}

string example3::welcomeString(){
    
    return "Welcome "+exampleName+" to GradeScope Autograding";
}