import pandas as pd
from src.embedding.model_loader import MiniLML6V2EmbeddingFunction
from db.chroma_utils import ChromaWithUpsert
from src.utils.data_loader import load_data_v1
from src.utils.pdf_utils import *


def process_excel(persist_directory):
    print("----Processing Excel File----", "\n")

    print("Loading Excel file, Accessing correct sheet")

    excel_path = "data/excel/a.xlsx"
    excel_data = pd.read_excel(excel_path, sheet_name="Sheet1")

    print("Fetching columns")
    questions = excel_data["Question"].tolist()
    answers = excel_data["Answer"].tolist()

    content_to_vector = [f"{question}: {answer}" for question, answer in zip(questions, answers)]

    emb_func = MiniLML6V2EmbeddingFunction()

    print("Creating Embeddings")

    excel_chroma = ChromaWithUpsert(
        name="excel_minilm6v2",
        embedding_function=emb_func,
        persist_directory=persist_directory,
    )

    if excel_chroma.is_empty():
        _ = excel_chroma.upsert_texts(
            texts=content_to_vector,
            metadata=[{'file_info': 'excel', 'question': question, 'answer': answer} for (question, answer) in
                      zip(excel_data['Question'], excel_data['Answer'])]

        )
    print("Embeddings Stored in Vector DB", "\n")
    print("----Excel Processing Complete----", "\n")
    return excel_chroma


def process_csv(persist_directory):
    print("----PROCESSING CSV FILE---- ", "\n")

    print("Loading Dataset")
    datasets = ['LongNQ', 'nq910']
    dataset_name = datasets[0]
    data_root = "data"

    documents, questions = load_data_v1(dataset_name, data_root)
    documents['indextext'] = documents['title'].astype(str) + "\n" + documents['text']

    print("Dataset Loaded: ", dataset_name)

    print("Creating Embeddings")

    emb_func = MiniLML6V2EmbeddingFunction()

    csv_vector_db = ChromaWithUpsert(
        name="csv_minilm6v2",
        embedding_function=emb_func,
        persist_directory=persist_directory,
    )

    if csv_vector_db.is_empty():
        _ = csv_vector_db.upsert_texts(
            texts=documents.indextext.tolist(),
            metadata=[{'file_info': 'csv', 'title': title, 'id': id} for (title, id) in
                      zip(documents.title, documents.id)],
            ids=[str(i) for i in documents.id],
        )

    print("Embeddings Stored in Vector DB", "\n")

    print("----CSV Processing Complete----", "\n")

    return csv_vector_db


def process_pdf(file_path, persist_directory):
    emb_func = MiniLML6V2EmbeddingFunction()

    print("\n", "----PROCESSING PDF FILE----", "\n")

    print("Transforming PDF to text")

    text_list = transform_pdf_to_text(file_path)

    print("Text transformation successful")

    print("Converting text to chunks")

    chunks = text_to_chunks(text_list)

    print("Text successfully converted to chunks")

    print("Creating Embeddings")

    pdf_chroma = ChromaWithUpsert(
        name="pdf_minilm6v2",
        embedding_function=emb_func,
        persist_directory=persist_directory,
    )

    if pdf_chroma.is_empty():
        metadata = [{'file_info': 'pdf', 'file': file_path}] * len(chunks)
        _ = pdf_chroma.upsert_texts(
            texts=chunks,
            metadata=metadata,
            ids=[str(i) for i in range(len(chunks))],
        )

    print("Embeddings Stored in Vector DB", "\n")

    print("----PDF Processing Complete----", "\n")

    return pdf_chroma
