import unittest

try:
    from .evaluation import Params, evaluation_function
except ImportError:
    from evaluation import Params, evaluation_function


class TestEvaluationFunction(unittest.TestCase):
    """
    TestCase Class used to test the algorithm.
    ---
    Tests are used here to check that the algorithm written
    is working as it should.

    It's best practise to write these tests first to get a
    kind of 'specification' for how your algorithm should
    work, and you should run these tests before committing
    your code to AWS.

    Read the docs on how to use unittest here:
    https://docs.python.org/3/library/unittest.html

    Use evaluation_function() to check your algorithm works
    as it should.
    """

    def test_default_variables_for_resistance(self):
        response, answer, params = "535037", 0.0, {"api_endpoint": "resistance"}
        result = evaluation_function(response, answer, params)

        self.assertEqual(result.get("is_correct"), True)

    def test_default_variables_for_resistors_check(self):
        response, answer, params = "535037", [], {"api_endpoint": "resistors"}
        result = evaluation_function(response, answer, params)

        self.assertEqual(result.get("is_correct"), True)

    def test_response_length(self):
        response, answer, params = "5337", 0.0, {"api_endpoint": "resistance"}
        result = evaluation_function(response, answer, params)

        self.assertEqual(result.get("is_correct"), False)

if __name__ == "__main__":
    unittest.main()
