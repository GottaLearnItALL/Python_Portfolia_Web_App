import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/21.jpg", width=480)

with col2:
    st.title("Aryan Bhat")
    content = """
    Hi I am Aryan!, I am upcoming python programmer, and student at Rutgers University.
    """
    st.info(content)

content2 = """
            Below you can find some of the apps I have built. Feel Free to contact me!!
            """
st.text(content2)


col3, col5, col4 = st.columns([1.5, 0.5, 1.5])


data = pandas.read_csv("data.csv",sep=";")
with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])