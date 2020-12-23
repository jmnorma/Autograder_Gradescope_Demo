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
    def test_RunOutput(self):
        #Title used by Gradescope 
        """Run: Output Matching"""

        # Create a subprocess to run the students code to obtain an output 
        test = subprocess.Popen(["./test1.out"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        # Standard unit test case with an associated error message 
        self.assertTrue( output == "Hello World", msg=("Expected: Hello World\nFound: "+output))
        test.terminate()

     # Associated point value within GradeScope
    @weight(5)
    def test_RunCharCount(self):
        #Title used by Gradescope 
        """Run: Character Count"""

        # Create a subprocess to run the students code to obtain an output 
        test = subprocess.Popen(["./test1.out"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        # Standard unit test case with an associated error message 
        self.assertTrue( len(output) == 11, msg=("Expected: 11 characters\nFound: "+str(len(output))))
        test.terminate()
   