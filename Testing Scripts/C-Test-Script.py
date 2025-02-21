import pytest
import subprocess
import time
# 1) Read in C code
# 3) Compile C code

#Not sure why this isn't working, getting an error calling GCC, but it works in command line
#I'll check again when I have some more time
#compile the C program given
#subprocess.run(["gcc", "-o", "program.exe", "program.c"], check=True)

# 2) Read in test cases
with open("test_cases.txt", "r") as test_cases_file:
    #creates an array of tuples for test cases as strings
    test_cases = []
    for line in test_cases_file:
        tokens = line.strip().split('"')
        cleaned_tokens = [token.strip() for token in tokens if token.strip()]
        test_cases.append(cleaned_tokens)

# 4) Run test Cases

#starting point to measure throughput
startTime = time.time()

#counter for number of test cases
count = 0

#runs test for each tuple in test_cases
@pytest.mark.parametrize("input, expected", test_cases)
def test(input, expected):
    global count

    #timer to measure latency
    TestStartTime = time.time()

    #prepares an input for stdin as a string
    input_str = " ".join(map(str, input))
    #runs the compiled program
    result = subprocess.run(["./program.exe"], input=input_str, text=True, capture_output=True)

    #check end time
    endTime = time.time()

    #print latency
    print(f"\nLatency for test case {count} : {endTime - TestStartTime}")
    count += 1

    #gets the output from stdout
    output = result.stdout.strip()

    #tests if the output is equal to the expected for this tuple
    assert output == expected

@pytest.fixture(scope="session", autouse=True)
def print_after_tests(request):
    yield  # Tests run here
    endTime = time.time()
    print("\nAverage throughput = ",(endTime - startTime)/count," for ",count, " test cases")