import os

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Prompt - text input to be processed by the LLM
# PromptTemplate - prompt that allows for parameters to be input into a prompt. Adds functionality to prompts to receive an input.

# Chat Models - wrapper around a large language model (text in, text out)

# LLM Chain - combine multiple components together for a single coherent application.

INFORMATION = """
Haruki Murakami (Japanese: 村上 春樹) is a popular contemporary Japanese writer and translator. His work has been described as 'easily accessible, yet profoundly complex'. He can be located on Facebook at: https://www.facebook.com/harukimuraka...

Since childhood, Murakami has been heavily influenced by Western culture, particularly Western music and literature. He grew up reading a range of works by American writers, such as Kurt Vonnegut and Richard Brautigan, and he is often distinguished from other Japanese writers by his Western influences.

Murakami studied drama at Waseda University in Tokyo, where he met his wife, Yoko. His first job was at a record store, which is where one of his main characters, Toru Watanabe in Norwegian Wood, works. Shortly before finishing his studies, Murakami opened the coffeehouse 'Peter Cat' which was a jazz bar in the evening in Kokubunji, Tokyo with his wife.

Many of his novels have themes and titles that invoke classical music, such as the three books making up The Wind-Up Bird Chronicle: The Thieving Magpie (after Rossini's opera), Bird as Prophet (after a piano piece by Robert Schumann usually known in English as The Prophet Bird), and The Bird-Catcher (a character in Mozart's opera The Magic Flute). Some of his novels take their titles from songs: Dance, Dance, Dance (after The Dells' song, although it is widely thought it was titled after the Beach Boys tune), Norwegian Wood (after The Beatles' song) and South of the Border, West of the Sun (the first part being the title of a song by Nat King Cole).
"""


def main():
    summary_template = """
        given the information {information} about this person, I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY, temperature=0, model_name="gpt-3.5-turbo"
    )  # temperature defines how creative the LLM will be

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    result = chain.run(information=INFORMATION)
    print(result)
    breakpoint()


if __name__ == "__main__":
    print("Hello Langchain!")

    main()
