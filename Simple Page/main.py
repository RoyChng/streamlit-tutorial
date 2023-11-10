import streamlit as st

st.header("This is a header", divider="rainbow")
st.subheader("This is a subheader")

st.markdown('''
    This is some paragraph text This is some paragraph text This is some paragraph text
    This is some paragraph text
            
    - Item one
    - Item two
    - Item three
            
    This text is **bold**
    
    [Subscribe](https://www.youtube.com/@turbinethree)
''')

st.image("https://images.unsplash.com/photo-1535930749574-1399327ce78f?q=80&w=1936&auto=format&fit=crop")