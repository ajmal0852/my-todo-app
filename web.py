import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    print('add to do called')
    todo = st.session_state['newtodo'] +'\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title('my todo app')
st.subheader('this is my to do app')

for index,todo in enumerate(todos):
    checkbox= st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input('',placeholder='add new todo',on_change=add_todo,key="newtodo")

print('hello')
st.session_state