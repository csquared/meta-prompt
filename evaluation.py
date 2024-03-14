import re
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.2, max_tokens=1024)

type_inference_template = """
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
Provide a "Yes" or "No" if the prompt is the correct type inside of <correct></correct> tags.
If the answer is "No", rewrite a suggestion for how to improve the prompt inside of <suggestion></suggestion> tags. 
If the answer is "Yes", include the <suggestion></suggestion> tags but leave them empty. 
If the prompt needs more examples, do not make them up inside of the suggestion and instead include placeholder text like "Example 1" and "Example 2" inside of the suggestion.
Responses inside of the tags should not contain any newlines.
Always include the tags.
"""

scoring_tempalate = """
Your role is to evaluate a given input prompt in <prompt></prompt> tags and provide a score for each rubric.
The rubrics are:
- Be clear and direct (<clarity></clarity>)
- Be concise (<conciseness></conciseness>)
- Provide examples or context (<examples></examples>)
- Give the system a role (<role></role>)
- Use XML tags (<xml></xml>)
- Avoid negation (<negation></negation>)
- Avoid redundancy (<redundancy></redundancy>)
- Avoid ambiguity (<ambiguity></ambiguity>)

For each of these rubrics, provide a score from 1 to 5, where 1 is the worst and 5 is the best. 
Include the score inside of the tags and always incldue the tags.
"""

type_inference_prompt = prompt = ChatPromptTemplate.from_messages([
    ("system", type_inference_template),
    ("user", "The prompt is: {input}")
])

scoring_prompt = prompt = ChatPromptTemplate.from_messages([
    ("system", scoring_tempalate),
    ("user", "The prompt is: {prompt}")
])

def evaluate_prompt_type(prompt):
  chain = type_inference_prompt | llm | StrOutputParser()
  result = chain.invoke({'input': prompt})
  type = re.findall(r'<type>(.*?)</type>', result)[0]
  evaluation = re.findall(r'<evaluation>(.*?)</evaluation>', result)[0]
  correct = re.findall(r'<correct>(.*?)</correct>', result)[0]
  suggestion = re.findall(r'<suggestion>(.*?)</suggestion>', result)[0]
  return (type, correct, evaluation, suggestion)

def score_prompt(prompt):
  chain = scoring_prompt | llm | StrOutputParser()
  result = chain.invoke({'prompt': prompt})
  return result