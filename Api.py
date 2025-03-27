from Conversation import Conversation
from Generator import Generator
from Conversational import Conversational
from QA import QA
from pydantic import BaseModel

class SuggestFromResponseModel(BaseModel):
    conversation: list[list]
    aboutme: str    

# Load models (these are shared across routes)
generative_model = Generator()
conversational_model = Conversational()
qa_model = QA()

def suggest_next_word(conversation: list[list], suggestion_sizes: list = [1,1,2,2,4]):
    ''' Generate suggestions using Generative model '''
        
    # Parse Context to Conversation object
    conversation = Conversation(conversation_list=conversation)
    # Run Generative model on Conversation object
    suggestions = generative_model.generate_options(conversation, suggestion_sizes)    
    return suggestions
