import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from dotenv import load_dotenv
from file_handling import FileHandler

class ChatBot:
    def __init__(self):
        """Initialize the ChatBot with specific model parameters."""
        load_dotenv()
        self.llm = ChatOpenAI(
            model_name='gpt-4',
            temperature=0.5,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

    def setup_chat_model(self):
        """Set up the chat model with a template for processing resumes."""
        prompt = ChatPromptTemplate(
            input_variables=['resume_text'],
            messages=[
                SystemMessage(content="You are an elite AI consultant with expertise in psychometric evaluations and career trajectory analytics. You possess profound capabilities to assess complex professional histories and delineate strategic career development plans."),
                HumanMessagePromptTemplate.from_template(
                    "Proceed with an in-depth analysis of the submitted resume. Evaluate the candidate's educational and professional timeline, "
                    "identify pivotal skills and distinguishing achievements. Synthesize this data to construct a nuanced summary of potential career pathways. "
                    "Recommend refined strategies for career advancement considering emerging industry trends. Here is the resume content:\n\n{resume_text}"
                )
            ]
        )

        chain = LLMChain(
            llm=self.llm, 
            prompt=prompt, 
            verbose=True
        )

        return chain

    def get_resume_insights(self, resume_text):
        """Generate insights from the resume by running the chat model."""
        chain = self.setup_chat_model()
        try:
            response = chain.run({'resume_text': resume_text})
            return response
        except Exception as e:
            print(f"Error processing the resume: {e}")
