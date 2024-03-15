from dataclasses import dataclass

class EvaluationExample1:
# this prompt was my first attempt - it's main drawback saying if it "required content"
# evaluatin of the prompt type means if the the content was provided in the prompt
  interaction = """
  System:
  Your role is to evaluate a given input prompt in <prompt></prompt> tags and determine if it is the correct type.
  The types of prompts are:
  - Zero-Shot: a simple question or statement that does not require any context to answer
  - One-Shot: a question or statement that requires some context to answer
  - Multi-Shot: a question or statement that requires a lot of context to answer
  - Chain of Thought: a series of questions or statements that require a lot of context to answer

  For example, the prompt "What is the capital of France?" is a Zero-Shot prompt because it does not require any context to answer.
  For example, the prompt "What is the weather today?" is a One-Shot prompt because it requires some context to answer.

  Evaluate the following prompt and provide the type of prompt it inside of <type></type> tags.
  Then, evaluate if the prompt needs more content and should be expanded or if it is too long and should be shortened.
  Provide your evaluation in <evaluation></evaluation> tags.

  The prompt is:
  I have 10 apples. If I give my dad 5 apples, he eats one and gives the rest to his only son. How many apples do I have?
  """

  golden_answer = """
  <type>Zero-Shot</type>
  <evaluation>This prompt could be improved by providing more context or examples to make it a One-Shot or Multi-Shot prompt. Adding a similar example problem with the solution would help clarify the type of reasoning required to solve this problem.</evaluation>
  """

class EvaluationExample2:
  prompt: str = """
  Your role is to evaluate a given input prompt in <prompt></prompt> tags and determine what type of prompt it is. 
  The types of prompts are:
  - Zero-Shot: a prompt that does not provide any context or examples
  - One-Shot: a prompt that provides one contenxt or examples
  - Multi-Shot: a prompt that requires many examples or context
  - Chain of Thought: a series of questions or statements that require a lot of context to answer

  For example, the prompt "What is the capital of France?" is a Zero-Shot prompt because it does not require any context to answer.
  For example, the prompt "What is the weather today?" is a One-Shot prompt because it requires some context to answer.

  Evaluate the following prompt and provide the type of prompt it inside of <type></type> tags.
  Then, evaluate if the prompt needs more content or would perform better as a different type of prompt.
  Suggest which type of prompt the input prompt should be in <evaluation></evaluation> tags. 
  Responses inside of the tags should not contain any newlines.
  """