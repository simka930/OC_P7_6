import streamlit as st
import time

with st.spinner('reloading ...'):
    time.sleep(1)

st.sidebar.title("Pages")

radio = st.sidebar.radio(label="", options=["Set A", "Set B", "Add them"])

session_state = st.session_state  # Pick some initial values.
if "a" not in session_state:
    session_state["a"] =0
# if "b" not in session_state:
if "b" not in session_state:
    session_state["b"] =0


if radio == "Set A":
    input_a = st.text_input(label="What is a?")

    if input_a:
        session_state.a = float(input_a)
        st.write(f"You set a to {session_state.a}")


elif radio == "Set B":
    input_b = st.text_input(label="What is b?")

    if input_b:
        session_state.b = float(input_b)
        st.write(f"You set a to {session_state.b}")
# elif radio == "Set B":
#     if st.text_input(label="What is b?"):
#         session_state.b = float(st.text_input(label="What is b?"))
#         st.write(f"You set b to {session_state.b}")
elif radio == "Add them":
    st.write(f"a={session_state.a} and b={session_state.b}")
    button = st.button("Add a and b")
    if button:
        st.write(f"a+b={session_state.a+session_state.b}")

session_state
"a" in session_state
"b" in session_state
