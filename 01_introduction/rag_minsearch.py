from ollama import chat
from ollama import ChatResponse
import minsearch 
import json


def prepare_document(document_path: str):
    with open(document_path, "r") as f_in:
        raw_documents = json.load(f_in)

    documents = []

    for course_dict in raw_documents:
        for doc in course_dict["documents"]:
            doc["course"] = course_dict["course"]
            documents.append(doc)

    return documents

def search(documents: list, query: str, num_results: int = 5, filter_dict: dict = {"course": "data-engineering-zoomcamp"}):
    index = minsearch.Index(
        text_fields=["question", "text", "section"], 
        keyword_fields=["course"]
    )
    index.fit(documents)

    boost = {
        "question": 3.0, "section": 0.5,
        # "text": 1.0,  "course": 0.5
    }   

    results = index.search(
        query=query, 
        boost_dict=boost, 
        num_results=num_results,
        filter_dict=filter_dict
    )

    return results

def llm(question, results):
  
  prompt_template = """
  you're a course teaching assistant. answer the QUESTION based on the context below. 
  use only the facts in the context to answer the question. 
  if you don't know the answer, say "I don't know".

  QUESTION: {question}

  CONTEXT: {context}
  """

  context = "" 

  for doc in results:
      context = context + f"\nsection: {doc['section']}\n" + \
          f"question: {doc['question']}\n" + \
          f"text: {doc['text']}\n\n"
  prompt = prompt_template.format(question=question, context=context).strip()

  response: ChatResponse = chat(model="llama3.2", messages=[
    {
      "role": "user",
      "content": prompt,
    },
  ])

  return (response.message.content)

def rag(question: str, num_results: int = 5, filter_dict: dict = {"course": "data-engineering-zoomcamp"}):
    documents = prepare_document("documents.json")
    results = search(documents, question, num_results, filter_dict)
    
    if len(results) == 0:
        return "I don't know"

    answer = llm(question, results)

    return answer

question = "the course already started, can I still join?"

rag(question)


