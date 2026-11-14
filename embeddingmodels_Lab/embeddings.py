 #this code wont work bcz no payment!
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model = 'text-embedding-3-large',
    dimensions=64
)


vector = embeddings.embed_query("my name is Paxton")

print(vector)


# OR

# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# embeddings = OpenAIEmbeddings(
#     model = 'text-embedding-3-large',
#     dimensions=64
# )


# texts = [
#     "Hello this is Akarsh Vyas",
#     "Hello your name is YouTube",
#     "And you all are very beautiful"
# ]

# vector = embeddings.embed_documents(texts)
# print(vector)
