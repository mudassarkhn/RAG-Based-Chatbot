from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import get_buffer_string
from langchain_classic.memory import ConversationBufferMemory
from VectorStores.Vectorstores import get_vectorstore
from LLM.LLM import llm
from Prompt.Prompt import prompt

def join_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

memory = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history"
)

def create_rag_chain(memory):
    retriever = get_vectorstore().as_retriever(
        search_type="mmr",
        search_kwargs={"k": 3, "fetch_k": 10}
    )

    return (
        RunnableParallel({
            "context": retriever | RunnableLambda(join_docs),
            "question": RunnablePassthrough(),
            "chat_history": RunnableLambda(
                lambda _: get_buffer_string(memory.chat_memory.messages)
            )
        })
        | prompt
        | llm

    )

chain=create_rag_chain(memory)
# while True:
#         user_input = input("Enter your query (or 'exit' to quit): ")
#         print("User:", user_input)
#         if user_input.lower() in ['q', 'exit']:
#             break

#         # .invoke() returns the final state dictionary directly
#         result = create_rag_chain(memory).invoke(
#             user_input
#         )
#         memory.chat_memory.add_user_message(user_input)
#         memory.chat_memory.add_ai_message(result)
#         AI_msg=result
#         print("Bot:", AI_msg)
            