# 1. Install dependencies
# !pip install --upgrade langchain langchain-openai

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 2. Set your OpenAI API key (best practice: env variable)
# NOTE: Make sure you've created a secret key from OpenAI dashboard
os.environ["OPENAI_API_KEY"] = "your_secret_api_key"

# 3. Initialize LLM
# temperature=0 means deterministic response (same output every time)
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# 4. Simple message invocation
messages = [
    ("system", "You are a helpful assistant that translates English to French."),
    ("human", "Translate this sentence from English to French: I love programming.")
]

response = llm.invoke(messages)
print(response.content)   # J'adore la programmation

# 5. Chaining the LLM with a prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translates input language to output language."),
        ("human", "{input}")
    ]
)

# 6. Create a chain: prompt → LLM
chain = prompt | llm   # vertical bar '|' is chaining operator

# 7. Invoke chain with variables
response = chain.invoke(
    {
        "input": "I love programming",
        "input_language": "English",
        "output_language": "German"
    }
)

# 8. Output the response
print(response.content)   # Ich liebe das Programmieren
Library: LangChain + OpenAI install ki (pip install langchain langchain-openai)
Secret key: Model ko env variable me diya → safe magic key
GPT Translator: GPT-4o banaya, English → French/German translate karega, temperature=0 → same output har bar
Roles: System = “helpful translator”, Human = input sentence
Example: “I love programming” → J'adore la programmation
PromptTemplate + Chain: Reusable template {input} ke saath, Chain = template → GPT-4o → output
Output: “I love programming” → Ich liebe das Programmieren
Chaining = Waiter ka workflow: Input → Rules → Action → Output
Reusable: Har order ke liye same workflow use hota hai
Dynamic Input: Tum pizza ya burger ya coke change kar do, chain same rahegi
Organized & Fast: Har step automatically execute hota hai
LangChain = simple wrapper jo tumhe manual roles define karne se bachata hai, bas input do aur output le lo.
-------------------------------END-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
