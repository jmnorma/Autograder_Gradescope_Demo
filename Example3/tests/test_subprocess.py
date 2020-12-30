import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess


class TestDiff(unittest.TestCase):
    def setUp(self):
        pass 

    # Associated point value within GradeScope
    @weight(5)
    def test_Compile(self):
        #Title used by Gradescope 
        """Clean Compile"""

        # Create a subprocess to run the students make file to ensure it compiles 
        test = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stderr.read().strip().decode('utf-8')
        test.kill()

        # Standard unit test case with an associated error message 
        self.assertTrue( output == "", msg=output)
        test.terminate()

    # Associated point value within GradeScope
    @weight(5)
    def test_default(self):
        #Title used by Gradescope 
        """Default Constructor + WelcomeString Function"""

        # Create a subprocess to run the students make file to ensure it compiles 
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: Welcome Test Name to GradeScope Autograding\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "Welcome Test Name to GradeScope Autograding", msg=output)
        test.terminate()
    
    # Associated point value within GradeScope
    @weight(5)
    def test_case1(self):
        #Title used by Gradescope 
        """Test Case 1: String Constructor """

        # Create a subprocess to run the students make file to ensure it compiles 
        test = subprocess.Popen(["./test.out", "1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: Welcome Josh to GradeScope Autograding\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "Welcome Josh to GradeScope Autograding", msg=output)
        test.terminate()

    # Associated point value within GradeScope
    @weight(5)
    def test_case2(self):
        #Title used by Gradescope 
        """Test Case 2: String Constructor """

        # Create a subprocess to run the students make file to ensure it compiles 
        test = subprocess.Popen(["./test.out", "2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: Welcome Dr. Plaue to GradeScope Autograding\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "Welcome Dr. Plaue to GradeScope Autograding", msg=output)
        test.terminate()

  

   