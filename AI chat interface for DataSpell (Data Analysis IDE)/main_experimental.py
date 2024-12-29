import os
import pandas as pd
from LLM.llm import LLM
import importlib


def write_generated_code(code):
    code = code.replace('```python', '').replace('```', '')
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'experimental', 'transform.py')
    with open(file_path, "w") as file:
        file.write(code)

def import_transform_module():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'experimental', 'transform.py')
    spec = importlib.util.spec_from_file_location("transform", file_path)
    transform = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transform)
    return transform


def main():
    # Initialize LLM
    llm = LLM(prompt_file="experimental_prompt_template.txt")

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
        # Get the generated Python code from LLM
        user_input = input("Enter a command: ")
        generated_code = llm.generate_response(user_input)
        print("\nGenerated Code:")
        print(generated_code)

        write_generated_code(generated_code)
        
        # Import the transform module
        transform_module = import_transform_module()

        # Use the transform function from the imported module
        try:
            transformed_df = transform_module.transform(df)
            print("\nTransformed DataFrame:")
            print(transformed_df)
        except Exception as e:
            print("Something went wrong. Please try again.")
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
