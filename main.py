from src.utils.file_config import *
from src.ui import launch_gradio_interface
from multiprocessing import Pool


def main():
    """

    You can simultaneously generate embeddings for different file types using multiprocessing,
    the system can concurrently process multiple files, significantly reducing the time required for embedding generation.

    Note: Ensure that the necessary parameters are passed to the embedding generation functions
    (process_pdf, process_excel, process_csv) to perform the embedding generation process effectively.


    """

    # emb_func = MiniLML6V2EmbeddingFunction()

    # def process_files(file):
    #     if file.endswith(".pdf"):
    #         result = process_pdf(file, "db/pdf")
    #     elif file.endswith((".xlsx", ".xls")):
    #         result = process_excel(file, "db/xcl")
    #     elif file.endswith(".csv"):
    #         result = process_csv(file, "db/csv")
    #     else:
    #         raise ValueError("Unsupported file format")
    #     return result

    pdf_vector_db = process_pdf("data/pdfs/paper_flowers.pdf", "db/pdf")
    excel_vector_db = process_excel("db/xcl")
    csv_vector_db = process_csv("db/csv")

    vector_dbs = [csv_vector_db, excel_vector_db, pdf_vector_db]

    launch_gradio_interface(vector_dbs)


if __name__ == "__main__":
    main()
