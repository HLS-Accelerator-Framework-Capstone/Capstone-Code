import pytest
import subprocess

# 1) Compile the assembly program
#currently, the plan is to use nasm because that is what was suggested by a quick google,
#but I'm not sure how to get it to work and there is not a lot of documentation
#for now, I'm just going to rely on already having the executable. This program works exactly
#the same as the C test script otherwise. Probably I'll make it into executable test script
#and separate the compilers and then make a parent script
# subprocess.run(["nasm", "-o", "program.exe", "program.c"], check=True)

# 2) Read in test cases
with open("test_cases.txt", "r") as test_cases_file:
    # creates an array of tuples for test cases as strings
    test_cases = []
    for line in test_cases_file:
        tokens = line.strip().split('"')
        cleaned_tokens = [token.strip() for token in tokens if token.strip()]
        test_cases.append(cleaned_tokens)


# 4) Run test Cases
# runs test for each tuple in test_cases
@pytest.mark.parametrize("input, expected", test_cases)
def test(input, expected):
    # gives the input to stdin
    input_str = " ".join(map(str, input))

    # runs the compiled program
    result = subprocess.run(["./program.exe"], input=input_str, text=True, capture_output=True)

    # gets the output from stdout
    output = result.stdout.strip()

    # tests if the output is equal to the expected for this tuple
    assert output == expected
