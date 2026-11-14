from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model("openai/gpt-oss-120b",  model_provider="groq" , temperature = 0.9,max_tokens = 50)

response = model.invoke("If you could travel anywhere in the universe, where would you go and why? Describe your journey in an interesting way in one para")

print(response.content)