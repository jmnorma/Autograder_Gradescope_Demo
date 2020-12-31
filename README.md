


# Autograder_Gradescope_Demo

### This is a tutorial for how to Autograde C++ Code using Gradescope, along with helpful tips from using it for CPSC 1071 during Fall 2020. This Repository has three different examples showing some of our most common uses for a autograder. 

<br/><br/>

<center>
<img src="GradeScopeLogo.jpg" alt="GradescopeLogo">
</center>

<br/><br/>

## Table of contents
1. Coding the Autograder
    - Getting Started 
    - Providing User Input 
    - Unit Testing ( Testing Classes )
2. Creating the Gradescope Assignment
 

<br/><br/>

## Coding the Autograder
___
### Getting Started 
1. Download the sample code from this Repository. We will demonstrate using the Example1 Files. 

        Every Autograder using Gradescope must include the following Files:

        1. requirements.txt
        2. run_autograder 
        3. run_test.py
        4. setup.sh
        5. tests/test_subprocess.py 

<br/><br/>

 Your students' code is stored in a separate directory within the Gradescope container. You will need to locate with **Submissions** and copy those files into the **Source** directory for this implementation. This is already done using BASH within the run_autograder file 


2. Open the run_autograder BASH Script and edit the copy commands to your assignments submission specifications.
>if you require a zipped submission you will to unzip the file here

<center>
<img src="CopyCommand.png" alt="CopyCommand">
</center>

3. Next we need to compile your students code within the source folder. Within this example our students submitted a makefile so the make command is ran with our script. 

<center>
<img src="RunCommand.png" alt="CopyCommand">
</center>

4. We now need to create our test cases. We will be using gradescope's python library along with python's unittest libary. This inital set up is shown within test_subprocess.py. 
    
>This uses a multithreaded approach to run our C++ code within python and test the output. 

    Each Test Case has Five Main Parts:
        1. Weight
        2. Name  
        3. Subprocess
        4. Python Unit Test
        5. Error Message  

<center>
<img src="PythonRun.png" alt="CopyCommand">
</center>

**Weight**: This is how many points the test case is worth and is defined using a precondition before the function 

**Name**: There are two names for every test case. A Python unit test name and Gradescope test name (Shown to the students). The Python function name must start with test_ to indictate that it is to be tested. **Every Test Case must have a different name.**

**Subproccess**: This is the multithreaded component. Here we use Popen to create a new thread running our students code. Denote the parameter requires a list of strings therefore any command line input must be placed within their own string. 

**Python Test Case**: Compare the students output to an expected output using python operators. 
>I prefer to use the contains function because you can be less strict output matching. 

**Error Message** (Optional but Recommended): This allows you to give your students more descriptive feedback based on their output or give them common troubleshooting techniques

5. Finally zip up all of your files excluding the solution code. 
 