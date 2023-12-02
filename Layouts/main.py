import streamlit as st

st.header("Layouts")

tab1, tab2, tab3 = st.columns(3)

with tab1:
   st.image("https://images.unsplash.com/photo-1698761879886-0ad922386193?auto=format&fit=crop&q=80&w=1974")

with tab2:
   st.image("https://images.unsplash.com/photo-1689001225123-05b8eb4769c3?auto=format&fit=crop&q=80&w=1970")

with tab3:
   st.image("https://images.unsplash.com/photo-1682687982502-b05f0565753a?auto=format&fit=crop&q=60&w=500")

expander = st.expander("See explanation")

with expander:
   st.header("This is an explanation")

   st.markdown('''
      Some explanation...
      - Point 1
      - Point 2
      - Point 3
   ''')