#%%
import tests.scoring
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

comparison_template_system = """
Assume the role of a prompt engineer.
You will be given two prompts, a reference prompt and a candidate prompt.
You will also be given two outputs, a reference output and a candidate output.

Your role is to compare the reference and candidate prompts and outputs in the following ways and provide
a response as a valid json object:

(1) How does the candidate prompt compare to the reference prompt according to the following rubrics:
- Be clear and direct (clarity)
- Be concise (conciseness)
- Provide examples or context (examples)
- Give the system a role (role)
- Use XML tags (xml)
- Avoid negation (negation)
- Avoid redundancy (redundancy)
- Avoid ambiguity (ambiguity)

(2) How does the candidate output compare to the reference output according to the following rubrics:
- Similarity to the reference output (similarity)
- Relevance to the prompt (relevance)
- Correct formatting of the output (format)

(3) Provide a summary of the comparison. If the candidate prompt and output are better than the reference,
provide a summary of the improvements. If the candidate prompt and output are worse than the reference,
provide a summary of the deficiencies.

Inside of each object, include a correct score from 1-5 (score) and a reason for the score (reason).
Place answers for the question (1) inside of an "input" key,
 answers for question (2) inside of an "output" key
 and the summary inside of a "summary" key.

Always output correct, well-formatted json without any markup.
"""

comparison_template_user = """
Reference Prompt: 
{reference_prompt}

Reference Output:
{reference_output}

Candidate Prompt:
{candidate_prompt}

Candidate Output:
{candidate_output}
"""

comparison_prompt = prompt = ChatPromptTemplate.from_messages([
    ("system", comparison_template_system),
    ("user", comparison_template_user)
])

llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.2, max_tokens=1024)

def compare_prompts(reference_prompt, reference_output, candidate_prompt, candidate_output):
  chain = comparison_prompt | llm | StrOutputParser() 
  result = chain.invoke({
    "reference_prompt": reference_prompt,
    "reference_output": reference_output,
    "candidate_prompt": candidate_prompt,
    "candidate_output": candidate_output
  })
  return result

#%%
result = compare_prompts(
  tests.scoring.ScoringExample1.reference_input,
  tests.scoring.ScoringExample1.reference_output,
  tests.scoring.ScoringExample1.candidate_input,
  tests.scoring.ScoringExample1.candidate_output
)

#%%
result2 = compare_prompts(
  tests.scoring.ScoringExample1.candidate_input,
  tests.scoring.ScoringExample1.candidate_output,
  tests.scoring.ScoringExample1.reference_input,
  tests.scoring.ScoringExample1.reference_output
)
print(result2)