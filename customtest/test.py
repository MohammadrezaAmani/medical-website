import requests
import json


class TestCase:
    """
    A class to represent a test case.

    Attributes
    ----------
    url : str
        The URL to send the request to.
    headers : dict
        The headers to include in the request.
    data : dict
        The data to include in the request.
    results : list
        The expected results of the request.

    Methods
    -------
    test()
        Sends a request to the specified URL with the specified headers and data,
        and compares the response to the expected results.
    __str__()
        Returns a string representation of the test case.
    __repr__()
        Returns a string representation of the test case.
    """

    def __init__(self, url=None, headers=None, data=None, results=None):
        """
        Parameters
        ----------
        url : str, optional
            The URL to send the request to. Default is an empty string.
        headers : dict, optional
            The headers to include in the request. Default is an empty dictionary.
        data : dict, optional
            The data to include in the request. Default is an empty dictionary.
        results : list, optional
            The expected results of the request. Default is an empty list.
        """
        self.url = url if url else ""
        self.headers = headers if headers else {}
        self.data = data if data else {}
        self.results = results if results else []

    def test(self):
        """
        Sends a request to the specified URL with the specified headers and data,
        and compares the response to the expected results.

        Returns
        -------
        bool
            True if the response matches the expected results, False otherwise.
        """
        if self.data:
            response = requests.post(self.url, headers=self.headers, data=self.data)
            print(response.text)
            if json.loads(response.text) == self.results:
                return True
            return False

    def __str__(self) -> str:
        """
        Returns a string representation of the test case.

        Returns
        -------
        str
            A string representation of the test case.
        """
        return f"URL: {self.url}\nHeaders: {self.headers}\nData: {self.data}\nResults: {self.results}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the test case.

        Returns
        -------
        str
            A string representation of the test case.
        """
        return f"URL: {self.url}\nHeaders: {self.headers}\nData: {self.data}\nResults: {self.results}"


class Test:
    def __init__(self, test_cases: list = None) -> None:
        self.passed = []
        self.feilures = []

        for test_case in test_cases:
            if test_case.test():
                self.passed.append(test_case)
            else:
                self.feilures.append(test_case)

    def __str__(self) -> str:
        return f"Passed: {len(self.passed)}\nFeilures: {len(self.feilures)}\n\nPassed:\n{str(self.passed)}\n\nFeilures:\n{str(self.feilures)}"
