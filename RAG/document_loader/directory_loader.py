from langchain_community.document_loaders import TextLoader, DirectoryLoader

# Load a single text file
loader = TextLoader("requirement.txt")
documents = loader.load()

# print('documets:', documents)
# Load all files from a directory
directory_loader = DirectoryLoader("documents/", glob="*.txt")
all_documents = directory_loader.load()

print('all_documents:', all_documents)
# # Print loaded documents
# for doc in all_documents:
#     print(doc.page_content)
