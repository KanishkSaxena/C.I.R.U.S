import gradio as gr
from functools import partial
from src.utils.vector_db import *
from src.utils.query_utils import *
from src.utils.prompt_builder import make_prompt
from langchain.globals import get_llm_cache,set_llm_cache
from src.utils.similarity_score import get_top_5_chunks
from langchain.cache import InMemoryCache
from config import generate_response


def process_question(vector_dbs, question, slider):

    set_llm_cache(InMemoryCache())
    cache = get_llm_cache()
    cached_response = cache.lookup(question, "")
    if cached_response is not None:
        print("Response found in cache.")
        return cached_response

    combined_results = []
    metadatas = []
    with ThreadPoolExecutor() as executor:
        results = executor.map(partial(query_vector_db, question=question), vector_dbs)

    for documents, metadata in results:
        combined_results.extend(documents)
        metadatas.extend(metadata)

    flat_metadatas = [metadata for metadata_list in metadatas for metadata in metadata_list if 'file_info' in metadata]

    top_15_results = combined_results[:15]

    all_chunks = [chunk for top_15_results in top_15_results for chunk in top_15_results]

    document_texts = get_top_5_chunks(question, all_chunks, flat_metadatas)
    print("Top 5 Chunks:")
    for i, (chunk, metadata, similarity) in enumerate(document_texts, start=1):
        print(f"Chunk {i}:")
        print(chunk)
        print(similarity)
        print("\nFile Info:", metadata['file_info'])
        print()

    document_texts = [chunk_text for chunk_text, _, _ in document_texts]

    context = "\n\n\n".join(document_texts)

    prompt = make_prompt(context, question)

    print("PROMPT-----------------", prompt)

    response = generate_response(prompt)

    cache.update(question, "", response)

    return response


def launch_gradio_interface(vector_dbs):
    iface = gr.Interface(
        fn=partial(process_question, vector_dbs),
        inputs=[gr.Textbox(lines=4, label="Question")],
        outputs=[gr.Textbox(lines=4, label="Response")],
        title="C.I.R.U.S",
        description="<span style = 'size: 24px'>Enter your question and get the answer.</span>",
        css="./src/custom_styles.css",
        theme=gr.themes.Soft(),
        examples=[
            ["What is the capital of France?"],
            ["Author of 'To Kill a Mockingbird'?"]
        ]
    )
    return iface