import os

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import config
from utils.linkedin import scrape_linkedin_profile

# Prompt - text input to be processed by the LLM
# PromptTemplate - prompt that allows for parameters to be input into a prompt. Adds functionality to prompts to receive an input.

# Chat Models - wrapper around a large language model (text in, text out)

# LLM Chain - combine multiple components together for a single coherent application.


def main():
    summary_template = """
        given the Linkedin information {information} about this person, I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(
        openai_api_key=config.OPENAI_API_KEY, temperature=0, model_name="gpt-3.5-turbo"
    )  # temperature defines how creative the LLM will be

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(config.LINKEDIN_PROFILE_URL)

    result = chain.run(information=str(linkedin_data))
    breakpoint()
    print(result)



if __name__ == "__main__":
    main()
