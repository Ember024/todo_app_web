import streamlit as st
import functions

# Paste in terminal to run "streamlit run web.py"
# "pip freeze > requirements.txt" to create requirements file listing packages for server to install
# Refresh browser to rerun with updated code

todos = functions.get_todos()

def add_todo():
    todo =st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my to app.")
st.write("This app is to increase productivity.")

for index, todo in enumerate(todos):
   checkbox= st.checkbox(todo.capitalize(),key=todo)
   if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del st.session_state[todo]
       st.rerun()


st.text_input(label="",placeholder="Enter a todo",
              on_change=add_todo, key="new_todo")



# st.session_state