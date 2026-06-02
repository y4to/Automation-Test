import pytest

if __name__ == '__main__':
    pytest_args = [
        "Test",
        "q",
        "--tb=short",
        #"--maxfail=1"
    ]

    pytest.main(pytest_args)