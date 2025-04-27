# COMP 5710 Group Project

## Team Information

- **Team Name**: PENPALS-SQA2025-AUBURN
- **Team Members**: Aidan Miller, Jordyn Godsey, and Thomas Pohler

## Task Assignments

We split the work up between each team member as follows:

- **4a.** Aidan Miller
- **4b.** Thomas Pohler
- **4c.** Jordyn Godsey

After each task was completed, we worked together to push the files onto our GitHub Repo and tested them.

---

## Activities Completed

### 1. Unpacked Project
- Successfully unpacked `KubeSec.zip` to access the provided Python project files.

### 2. GitHub Repository Setup
- Created a shared GitHub repository following the naming convention and uploaded all project files to the repository.

### 3. Created README.md
- Added a README.md listing the team name and all team members at the top of the repository.

### 4. Software Quality Assurance Activities

#### 4a. Git Hook for Security Scanning
- Implemented a Git pre-commit hook that runs a security scan on all `.py` files.
- Used `bandit` to detect security vulnerabilities.
- Configured the hook to generate a report of findings into `bandit_report.csv`.
- The hook triggers automatically every time any Python file within the project is changed and committed.

#### 4b. Fuzz Testing (`fuzz.py`)
- Created a `fuzz.py` script that fuzzes 5 selected Python methods.
- The script generates random or edge case inputs and captures crashes or exceptions.
- Integrated `fuzz.py` with GitHub Actions to run automatically during CI.
- Documented bugs discovered:
  - **find_json_path_keys**: crashes on non-string dictionary keys (floats, None, frozenset).
  - **count_initial_comment_line**: crashes with `FileNotFoundError` when input file path doesn't exist.
  - **getValidTaints**: crashes with invalid input types (ValueError, TypeError).
  - **scanForResourceLimits**: crashes with `FileNotFoundError` on missing files.
  - **scanForSecrets**: error is caught properly, does not crash.

#### 4c. Forensics Integration (`forensics.py`)
- Selected 5 Python methods and added forensic logging to each.
- Logging includes timestamps, method execution results, and important variable states.
- Created `forensics.py` to run and verify forensic logging.
- Automated running of `forensics.py` via GitHub Actions.

---

## What We Learned

- **Python Scripting**: Gained hands-on experience modifying existing codebases.
- **Git and GitHub Workflow**: Strengthened version control skills and learned Git Hooks.
- **Static Analysis**: Understood the importance of early vulnerability detection.
- **Fuzz Testing**: Learned how random input testing can reveal hidden code bugs.
- **Forensics and Logging**: Practiced detailed event logging to support system audits.
- **Continuous Integration (CI) Pipelines**: Built automated workflows with GitHub Actions.
- **Collaboration and Teamwork**: Improved task distribution and team integration practices.

---

## Notes

- **Repository**: [GitHub Repository Link](https://github.com/amm0261/PENPALS-SQA2025-AUBURN)

- **Main Files**:
  - `forensics.py`
  - `fuzz.py`
  - `pre-commit`
  - `bandit_report.csv`
  - `.github/workflows/forensics.yml`
  - `.github/workflows/fuzz_testing.yml`
