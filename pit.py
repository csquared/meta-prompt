import argparse
import os
from dotenv import load_dotenv
load_dotenv()

from evaluation import evaluate_prompt_type, score_prompt

def main():
    parser = argparse.ArgumentParser(description='Prompt Improvement Tool')
    parser.add_argument('prompt_file', type=str, help='The file containing the prompt to evaluate and improve')
    parser.add_argument('--output', type=str, default='improved_prompt.txt', help='Output file for the improved prompt')
    
    args = parser.parse_args()
    
    # Load the prompt from the specified file
    with open(args.prompt_file, 'r') as f:
        prompt = f.read()

    print("Loaded prompt:")
    print(prompt)
    print()
    
    type, correct, evaluation, suggestion = evaluate_prompt_type(prompt)
    print(f"Prompt type: {type}")

    if correct == "Yes":
        print("Let's move on to scoring the prompt")
    else:
        print(f"Evaluation: \n {evaluation}")
        print(f"Here is a suggestion for how to improve the prompt: \n {suggestion}")
    
    scores = score_prompt(prompt)
    print(scores)

    # TODO: Generate suggestions for improvement
    suggestions = generate_suggestions(scores)
    
    # TODO: Refactor the prompt based on the suggestions
    improved_prompt = refactor_prompt(prompt, suggestions)
    
    # Save the improved prompt to the output file
    #with open(args.output, 'w') as f:
    #    f.write(improved_prompt)
    
    print(f"Improved prompt saved to {args.output}")

def generate_suggestions(scores):
    # TODO: Implement suggestion generation based on the rubric scores
    # Return a list of suggestions for improvement
    pass

def refactor_prompt(prompt, suggestions):
    # TODO: Implement prompt refactoring based on the suggestions
    # Return the improved prompt
    pass

if __name__ == '__main__':
    main()