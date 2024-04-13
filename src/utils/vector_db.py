from db.chroma_utils import ChromaWithUpsert
"""
NOT being used currently. Can be used to make code more modularised
"""
class VectorDB(ChromaWithUpsert):
    def __init__(self, name, embedding_function, persist_directory):
        self.name = name
        self.embedding_function = embedding_function
        self.persist_directory = persist_directory

    def upsert_texts(self, documents, metadata=None):
        chroma_instance = ChromaWithUpsert(
            name=self.name,
            embedding_function=self.embedding_function,
            persist_directory=self.persist_directory,
        )
        if chroma_instance.is_empty():
            _ = chroma_instance.upsert_texts(
                texts=documents.indextext.tolist(),
                metadata=[{'title': title, 'id': id} for (title, id) in zip(documents.title, documents.id)],
                ids=[str(i) for i in documents.id],
            )

# Usage example
# pdf_vector_db = VectorDB(
#     name="pdf_minilm6v2",
#     embedding_function=emb_func,
#     persist_directory=persist_directory,
# )
# pdf_vector_db.upsert_texts(chunks)

# csv_vector_db = VectorDB(
#     name="csv_minilm6v2",
#     embedding_function=emb_func,
#     persist_directory=persist_directory,
# )
# csv_vector_db.upsert_texts(
#     texts=documents.indextext.tolist(),
#     metadata=[{'title': title, 'id': id} for (title, id) in zip(documents.title, documents.id)],
#     ids=[str(i) for i in documents.id],
# )
        # else:
        #     print("ChromaDB is not empty. Skipping insertion.")


# import pandas as pd
# from langchain.text_splitter import CharacterTextSplitter
# from langchain_community.vectorstores import chroma
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.document_loaders import TextLoader, PyPDFLoader
# from langchain_community.embeddings import HuggingFaceEmbeddings

# embedding = HuggingFaceEmbeddings(model_name='intfloat/multilingual-e5-large')

# class VectorDBCreator:
#     def __init__(self, separator=" separate ", chunk_size=0, chunk_overlap=0, persist_directory="./chroma_db"):
#         self.separator = separator
#         self.chunk_size = chunk_size
#         self.chunk_overlap = chunk_overlap
#         self.persist_directory = persist_directory

#     def dataframe_to_vector_list(self, dataframe, include_columns=None):
#         # List of known ID patterns
#         id_patterns = ['ID_', 'ID', 'id' , 'Id']  # You can add more patterns here

#         # Find a column that matches the ID pattern
#         id_column = None
#         for column in dataframe.columns:
#             if any(column.endswith(pattern) for pattern in id_patterns):
#                 id_column = column
#                 break

#         if id_column is None:
#             raise ValueError("No recognized ID column found.")
        
#         # Rename the found ID column to a standard "ID"
#         dataframe['ID'] = dataframe[id_column]

#         if include_columns is None:
#             include_columns = dataframe.columns

#         # Ensure the new "ID" column is included, if not explicitly specified
#         if 'ID' not in include_columns:
#             include_columns = list(include_columns) + ['ID']

#         content_to_vector = []
#         for _, row in dataframe.iterrows():
#             formatted_text = "\n".join([f"{col}:{row[col]}" for col in include_columns if col in row])
#             content_to_vector.append(formatted_text)

#         return content_to_vector

#     def create_vdb(self, content):
#         db_txt = self.separator.join(content)
#         with open("db.txt", "w") as text_file:
#             text_file.write(db_txt)
        
#         loader = TextLoader('db.txt')
#         documents = loader.load()


#         text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#             separator=self.separator,
#             chunk_size=self.chunk_size,
#             chunk_overlap=self.chunk_overlap
#         )
        
#         texts = text_splitter.split_documents(documents)
#         db = chroma.from_documents(texts, embedding, persist_directory=self.persist_directory)
#         db.persist()
#         print(self.persist_directory)
#         return self.persist_directory  