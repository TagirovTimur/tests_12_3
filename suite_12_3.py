import unittest
import  tests_12_2

TestST= unittest.TestSuite()
TestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.RunnerTest))
TestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestST)