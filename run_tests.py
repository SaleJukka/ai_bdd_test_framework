from utils.openai_utils import generate_text, load_prompt

def generate_scenarios():
    # Load the prompt for Contact Us form
    prompt = load_prompt("contact_us_form") # Use the key directly since prompts are now in prompts.py

    # Generate Gherkin scenarios
    scenarios = generate_text(prompt)
    print("Generated Gherkin Scenarios:\n", scenarios)

    # Save the scenarios to a feature file
    feature_file_path = "features/contact_form.feature"

    # Prevent overwriting an existing feature file
    try:
        with open(feature_file_path, "x") as f: # Use "x" mode to ensure file is only created if it doesn't exist
            f.write(scenarios)
            print(f"Scenarios saved to {feature_file_path}")
    except FileExistsError:
        print(f"{feature_file_path} already exists. Skipping overwrite...")        


if __name__ == "__main__":
    generate_scenarios()