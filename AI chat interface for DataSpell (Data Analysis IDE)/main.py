import pandas as pd
import json
from LLM.llm import LLM
from Transformations.transformation import Transformation
import os

def parse_llm_output(llm_response):
    try:
        transformations = json.loads(f"[{llm_response}]")  # Parse as a list of dictionaries
        return [Transformation(action=trans['action'], params=trans['params']) for trans in transformations]
    except (json.JSONDecodeError, KeyError) as e:
        raise ValueError(f"Invalid LLM response format: {llm_response}") from e

def main():
    llm = LLM()    
    data = None

    while data is None:
        file_name = input("Which dataframe would you like to use? (Example: housing.csv) ")
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, 'data', file_name)
        try:
            data = pd.read_csv(file_path)
        except FileNotFoundError:
            print("File not found. Please ensure the file exists.")

    
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)

    while True:
        # Get user input
        user_input = input("Enter a command: ")

        # Generate response from LLM
        llm_response = llm.generate_response(user_input)
        print("\nLLM Response:", llm_response)

        # Parse the LLM response into Transformation objects
        transformations = parse_llm_output(llm_response)

        # Apply each transformation sequentially
        transformed_df = df
        for transformation in transformations:
            transformed_df = transformation.apply(transformed_df)

        print("\nTransformed DataFrame:")
        print(transformed_df)

if __name__ == "__main__":
    main()
