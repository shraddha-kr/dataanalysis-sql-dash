import streamlit as st
import pandas as pd
import sys
import chone as one
import chtwo as two



def main():
    # Introduction Page
    st.title('Data Analysis Using SQL & Excel By Wiley')
    st.markdown('My Interpretation Using Dash in place of Excel')

    # A Dictionary of Topics
    ch_dict = {"1-SQL Queries & Concepts": "one",
                "2-Data Exploration": "two"}

    # SideBar Options for selecting Topics
    st.sidebar.checkbox("Topics", True, key=1)
    select = st.sidebar.selectbox('Select a Topic',df_topics)

    # Call the spesific chapter code and content
    sel_ch = ch_dict.get(select)
    #st.markdown(sel_ch)
    class_obj = str_to_class(sel_ch)
    class_obj.content()

# To convert the selected topic str to class obj to call it's content
def str_to_class(str):
    return getattr(sys.modules[__name__], str)

@st.cache(persist=True)
def fetch_data():
    df = pd.read_csv('orders.csv')
    return df


if __name__ == '__main__':
    main()
