import streamlit as st

st.header("Input Elements")

st.subheader("Buttons")

button_clicked = st.button("Click Me")

if button_clicked:
    st.markdown("The button has been clicked")

st.divider()
st.subheader("Checkboxes")

checkbox_selected = st.checkbox("Select me!")

if checkbox_selected:
    st.markdown("The checkbox has been selected")
else:
    st.markdown("The checkbox has not been selected")

st.divider()
st.subheader("Text Inputs")

text_entered = st.text_input("Enter some text: ")

st.markdown("The text you entered is: " + text_entered)
