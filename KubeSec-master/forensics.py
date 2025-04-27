# COMP 5710 Group Project - 4c
# Jordyn Godsey, Aidan Miller, Thomas Pohler

import logging
import random

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock implementation of the methods for demonstration purposes
def method_1(input_param):
    try:
        if isinstance(input_param, int):
            return input_param * 2      # Return the multiple of the input and 2
        else:
            raise ValueError("Invalid input type for Method 1")
    except Exception as e:
        logging.error(f"Error in Method 1 with input {input_param}: {e}")
        raise

def method_2(input_param):
    try:
        if isinstance(input_param, str):
            return input_param.upper()      # Return the input string in all uppercase letters
        else:
            raise ValueError("Invalid input type for Method 2")
    except Exception as e:
        logging.error(f"Error in Method 2 with input {input_param}: {e}")
        raise

def method_3(input_param):
    try:
        if isinstance(input_param, list):
            return sorted(input_param)      # Return the list sorted from smallest to largest
        else:
            raise ValueError("Invalid input type for Method 3")
    except Exception as e:
        logging.error(f"Error in Method 3 with input {input_param}: {e}")
        raise

def method_4(input_param):
    try:
        if isinstance(input_param, float):
            return round(input_param, 2)        # Return the input rounded to the hundredths place
        else:
            raise ValueError("Invalid input type for Method 4")
    except Exception as e:
        logging.error(f"Error in Method 4 with input {input_param}: {e}")
        raise

def method_5(input_param):
    try:
        if isinstance(input_param, bool):
            return not input_param          # Return the opposite of the input boolean parameter
        else:
            raise ValueError("Invalid input type for Method 5")
    except Exception as e:
        logging.error(f"Error in Method 5 with input {input_param}: {e}")
        raise

# Define other modified methods with forensics enhancements as needed

# Sample data for testing
sample_int = random.randint(1, 100)
sample_str = "hello"
sample_list = [8, 2, 3, 1, 4, 5, 9, 7, 6]
sample_float = 3.14159
sample_bool = True

# Call and log each method with sample data
if __name__ == "__main__":
    logging.info("Starting forensics testing...")
    method_1_result = method_1(sample_int)
    logging.info(f"Method 1 result: {method_1_result}")

    method_2_result = method_2(sample_str)
    logging.info(f"Method 2 result: {method_2_result}")

    method_3_result = method_3(sample_list)
    logging.info(f"Method 3 result: {method_3_result}")

    method_4_result = method_4(sample_float)
    logging.info(f"Method 4 result: {method_4_result}")

    method_5_result = method_5(sample_bool)
    logging.info(f"Method 5 result: {method_5_result}")

    logging.info("Forensics testing completed.")
