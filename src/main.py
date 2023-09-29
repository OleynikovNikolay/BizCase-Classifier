
import argparse
import logging
from your_classification_module import classify_email_function

# setting up the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Email Classification CLI")
    parser.add_argument("--input", required=True, help="Email text to classify")
    parser.add_argument("--output", help="Output XML file for classification result")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

    args = parser.parse_args()

    # loading the model
    _MODEL_PATH = None
    email_text = args.input
    classification_result = classify_email_function(email_text, _MODEL_PATH)

    # outputting the classification result
    if args.output:
        with open(args.output, "w") as output_file:
            output_file.write(classification_result)
    else:
        print(classification_result)

if __name__ == "__main__":
    main()