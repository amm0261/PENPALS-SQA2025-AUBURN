COMP 5710 Group Project
Team Information
Team Name: PENPALS-SQA2025-AUBURN
Team Members: Aidan Miller, Jordyn Godsey, and Thomas Pohler
Task Assignments
We split the work up between each team member as follows:
4a. Aidan Miller
4b. Thomas Pohler
4c. Jordyn Godsey
After each task was completed, we worked together to push the files onto our GitHub Repo and tested them.
Activities Completed
1. Unpacked Project
Successfully unpacked KubeSec.zip to access the provided Python project files.
2. GitHub Repository Setup
Created a shared GitHub repository following the naming convention and uploaded all project files to the repository.
3. Created README.md
Added a README.md listing the team name and all team members at the top of the repository.
4. Software Quality Assurance Activities
4.a Git Hook for Security Scanning
Implemented a Git pre-commit hook that runs a security scan on all .py files.
Used bandit to detect security vulnerabilities.
Configured the hook to generate a report of all findings in bandit_report.csv. The results of the hook running on a known “bad” vulnerability are shown both in the screenshots of the warning provided from the terminal and the bandit_report.csv file below.


By nature, the hook automatically triggers every time any Python file within the entire project is changed and committed.
4.b Fuzz Testing (fuzz.py)
Created a fuzz.py script that fuzzes 5 selected Python methods.
The script generates random or edge case inputs for these methods, and it captures and logs any crashes or exceptions encountered.
Integrated fuzz.py with GitHub Actions to automatically run the fuzzer during CI.
Found and documented any bugs or unexpected behaviors triggered by fuzzing.

find_json_path_keys: The fuzzer shows that this function crashes with a TypeError when encountering dictionary keys that aren't strings. In particular, the tests show that it fails on floats, None, or a frozenset. Ideally, it should fail gracefully rather than terminating the process.
count_initial_comment_line: The fuzzer shows that this function crashes with a FileNotFoundError when given a file path that doesn't exist. As above, it propagates the error upwards rather than failing gracefully, potentially preventing the execution of any subsequent logic.
getValidTaints: The fuzzer shows that getValidTaints assumes every element in its input list is a two-tuple and attempts to unpack without validation, leading to ValueErrors for tuples of the wrong length and TypeErrors for non-iterable items (such as integers).
scanForResourceLimits: Similar to count_initial_comment_line, the fuzzer shows that scanForResourceLimits does not catch missing file errors and similarly fails with a propagating FileNotFoundError.
scanForSecrets: Finally, scanForSecrets actually worked extremely well, and none of the tested inputs crashed execution. While the console does show that an error occurs, this error is caught and execution continues, rather than the error propagating upwards and terminating the overall process.
4.c Forensics Integration (forensics.py)
Selected 5 Python methods and added forensic logging into them.
Logging included timestamps, method execution results, and state of important variables.
Created a forensics.py file to run and verify forensic logging.
Automated execution of forensics.py through GitHub Actions.

What We Learned
Python Scripting
Gained hands-on experience modifying existing codebases by inserting logging and making functions more auditable.
Git and GitHub Workflow
Strengthened skills in using Git for version control and GitHub for collaboration.
Learned how to use Git Hooks to automate pre-commit security checks.
Static Analysis
Understood the importance of static code analysis in detecting potential vulnerabilities early in the development process.
Fuzz Testing
Learned how fuzzing can be used to identify hidden bugs by providing random, unexpected, or invalid inputs to methods.
Forensics and Logging
Understood the role of forensic logging in tracking system behavior and supporting incident investigations.
Continuous Integration (CI) Pipelines
Gained practical knowledge of setting up and configuring GitHub Actions to automate quality assurance tasks such as fuzz testing and forensics testing.
Collaboration and Teamwork
Improved our skills in collaborative project management, task distribution, and integrating work through GitHub Pull Requests.
Notes
Repository: https://github.com/amm0261/PENPALS-SQA2025-AUBURN 
Main Files:
forensics.py
fuzz.py
pre-commit
bandit_report.csv
.github/workflows/forensics.yml
.github/workflows/fuzz_testing.yml
