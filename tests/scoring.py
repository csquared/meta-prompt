from dataclasses import dataclass

class ScoringExample1:
  reference_input = """
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

  The prompt is:
  I have 10 apples. If I give my dad 5 apples, he eats one and gives the rest to his only son. How many apples do I have?
  """

  reference_output = """
  <prompt>Your role is to evaluate a given input prompt in <prompt></prompt> tags and determine what type of prompt it is.</prompt>

  <type>Zero-Shot</type>
  <evaluation>One-Shot</evaluation>
  <correct>No</correct>
  <suggestion>Your role is to evaluate a given input prompt in <prompt></prompt> tags and determine what type of prompt it is. Example 1. Example 2.</suggestion>

  <clarity>4</clarity>
  <conciseness>5</conciseness>
  <examples>2</examples>
  <role>5</role>
  <xml>5</xml>
  <negation>5</negation>
  <redundancy>5</redundancy>
  <ambiguity>4</ambiguity>
  """

  candidate_input = """
  Assume the role of a prompt engineer.
  Your role is to score a given input prompt according to the following rubrics.
  For each of these rubrics, provide a score from 1 to 5, where 1 is the worst and 5 is the best. 
  The rubrics are:
  - Be clear and direct (<clarity></clarity>)
  - Be concise (<conciseness></conciseness>)
  - Provide examples or context (<examples></examples>)
  - Give the system a role (<role></role>)
  - Use XML tags (<xml></xml>)
  - Avoid negation (<negation></negation>)
  - Avoid redundancy (<redundancy></redundancy>)
  - Avoid ambiguity (<ambiguity></ambiguity>)

  Include the score inside of the tags and always incldue the tags.
  Only reply with the tags and the scores in them.

  The prompt is:
  I have 10 apples. If I give my dad 5 apples, he eats one and gives the rest to his only son. How many apples do I have?
  """

  candidate_output = """
  <clarity>5</clarity>
  <conciseness>5</conciseness>
  <examples>5</examples>
  <role>5</role>
  <xml>5</xml>
  <negation>5</negation>
  <redundancy>5</redundancy>
  <ambiguity>5</ambiguity>
  """