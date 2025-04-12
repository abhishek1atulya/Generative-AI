from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\tbaka\OneDrive\Desktop\Generative_AI\documents\Building Machine Learning Systems with Python - Second Edition.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)