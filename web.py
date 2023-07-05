import streamlit as st
import function
todos = function.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    function.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate (todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
        #st.experimental_rerun() reruns the function

st.text_input(label="", placeholder="Add new todo", on_change=add_todo, key="new_todo")
print("Hello")

""" when hosting the app
    we shall first create a new project with only the files we need to host
then install the streamlit packagess by streamlit run name of the file then check if its working 
then stop by control Z then we do pip freeze > requirement.txt to create a requirement file that 
will be shown on the host
and host
"""