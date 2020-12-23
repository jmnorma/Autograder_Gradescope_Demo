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
        fib = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = fib.stderr.read().strip().decode('utf-8')
        fib.kill()

        # Standard unit test case with an associated error message 
        self.assertTrue( output == "", msg=output)
        fib.terminate()

    # Associated point value within GradeScope
    @weight(5)
    def test_RunOutput(self):
        #Title used by Gradescope 
        """Run: Output Matching"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "test2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        fib = subprocess.Popen(["./test2.out"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = fib.stdout.read().strip().decode('utf-8')
        
        fib.kill()
        cat.kill() 

        # Standard unit test case with an associated error message 
        self.assertTrue( "Echo: TestString123" in output,  msg=("Expected: Echo: TestString123\nFound: "+output))
        fib.terminate()
        cat.terminate() 

   