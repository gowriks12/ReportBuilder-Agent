import streamlit as st
from streamlit_chat import message
from customAgent import agent
from utilFuncs import *
from PIL import Image

from generateReport import createDoc
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# print(OPENAI_API_KEY)

st.header("Data EDA Assistant")
if (
    "chat_answers_history" not in st.session_state
    and "user_prompt_history" not in st.session_state
    and "chat_history" not in st.session_state
    and "num_images_generated" not in st.session_state
    and "report" not in st.session_state
    # and "chain" not in st.session_state
):
    st.session_state["chat_answers_history"] = []
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_history"] = []
    st.session_state["num_images_generated"] = 0
    st.session_state["report"] = ""
    st.session_state["prompt"] = ""
    # st.session_state.chain = None

# with st.sidebar:
#     st.subheader("Upload your Documents Here: ")
#     pdf_files = st.file_uploader("Choose your PDF Files and Press OK", type=['pdf'], accept_multiple_files=True)
#
if st.button("Generate Report"):
    with st.spinner("Generating a report..."):
        report_path = createDoc(text=st.session_state.report)
        st.session_state["chat_answers_history"] = []
        st.session_state["num_images_generated"] = 0
        st.session_state["user_prompt_history"] = []
        st.session_state["report"] = ""
        st.session_state.prompt = ""
        with open(report_path, "rb") as rpt:
            # byte = rpt.read()
            st.download_button(label="Download report",data=rpt,file_name="report.docx",)
        # st.session_state.prompt = st.text_input("Prompt",
        #                                         placeholder="Ask anything about titanic passenger data...") or st.button(
        #     "Submit"
        # )

else:
    st.session_state.prompt = st.text_input("Prompt", placeholder="Ask anything about titanic passenger data...") or st.button(
        "Submit"
    )
    
    if st.session_state.prompt:
        with st.spinner("Generating response..."):
            generated_response = agent.query(st.session_state.prompt)
            generated_response = generated_response.__str__()
            images_generated, most_recent_image = get_most_recent_image()
            if st.session_state.num_images_generated < len(images_generated):
                image = Image.open(most_recent_image)
                st.image(image, caption=generated_response)
                print(most_recent_image)
                st.session_state.num_images_generated = len(images_generated)
                st.session_state.chat_answers_history.append("Image: "+most_recent_image)

            st.session_state.chat_history.append((st.session_state.prompt, generated_response))
            st.session_state.user_prompt_history.append(st.session_state.prompt)
            generated_response = generated_response + '\n'
            st.session_state.report += generated_response
            st.session_state.chat_answers_history.append(generated_response)


    if len(st.session_state["chat_answers_history"]) >= 1:
        j = 0
        for i in range(len(st.session_state["user_prompt_history"])):
            generated_response = st.session_state["chat_answers_history"][j]
            user_query = st.session_state["user_prompt_history"][i]
            if generated_response.startswith("Image: "):
                most_recent_image = generated_response.split("Image: ")[1]
                image = Image.open(most_recent_image)
                message(
                    user_query,
                    is_user=True,
                )
                st.image(image)
                message(st.session_state["chat_answers_history"][j+1])
                j += 2
            else:
                message(
                    user_query,
                    is_user=True,
                )
                message(generated_response)
                j += 1

    # for generated_response, user_query in zip(
    #     st.session_state["chat_answers_history"],
    #     st.session_state["user_prompt_history"],
    # ):
    #     print(generated_response)
    #     if generated_response.startswith("Image: "):
    #         most_recent_image = generated_response.split("Image: ")[1]
    #         image = Image.open(most_recent_image)
    #         message(
    #             user_query,
    #             is_user=True,
    #         )
    #         st.image(image)
    #         # message()
    #     else:
    #         message(
    #             user_query,
    #             is_user=True,
    #         )
    #         message(generated_response)
