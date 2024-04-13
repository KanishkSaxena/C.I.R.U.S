# C.I.R.U.S
Concurrent Information Retrieval Understanding System

## About

This project enables users to perform parallel semantic search on different types of documents(pdf, csv, excel) using gpt2 an open source model, allowing them to ask questions about the document and receive relevant answers based on the document's content. The system processes PDF documents, CSV documents and EXCEL documents into text, segments the text into chunks, and generates embeddings for each chunk. Users can then ask questions via Gradio interface, which triggers a semantic search process in all the vector db's concurrently enabling a faster response while traversing in all the db's. The system retrieves relevant text chunks from the document based on the user query and provides them as prompt to the llm. LLM compose's answers using the provided search results, with citation support for each reference.

## Usage

Use an existing venv or create a new venv with all the dependecies in 'requirements_venv.txt'.

```
pip intsall -r requirements_venv.txt
```

Run the project using python3 main.py and access the url generated in the terminal to enter the question.

## Contribution

Pull requests are welcome. Please create your own branch with your name from main branch.
