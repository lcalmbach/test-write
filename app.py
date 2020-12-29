import streamlit as st
import os
import json




file_name = os.path.join("tmp", "scenarios.json")
    
def read_file():
    with open(file_name, 'r') as myfile:
        data=json.loads(myfile.read())
        st.write("after read")
        st.write(data)
    return data
    
def change_file(data):
    scenario = data["default"]
    scenario["num_people"] = 1
    st.write("after change")
    st.write(data)
    return data

def write_file(data):
    with open(file_name, 'w') as myfile:
        json.dump(data, myfile)

def main():
    st.title("test write on share.streamlit.io")
    data = read_file()
    data = change_file(data)
    write_file(data)
    data = read_file()
    
if __name__ == '__main__':
    main()