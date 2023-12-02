import unittest
import sys
from io import StringIO


class BaseTestStdout(unittest.TestCase):
    def setUp(self):
        self.original_stdout = sys.stdout
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self) -> None:
        sys.stdout = self.original_stdout
