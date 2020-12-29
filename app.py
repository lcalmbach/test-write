import streamlit as st
import os
import json

file_name = os.path.join("tmp", "scenarios.json")
file_name2 = os.path.join("tmp", "scenarios2.json")
    
def read_file(f):
    with open(f, 'r') as myfile:
        data=json.loads(myfile.read())
    return data
    
def change_content(data):
    scenario = data["default"]
    scenario["num_people"] = 1
    return data

def write_file(data, f):
    with open(f, 'w') as myfile:
        json.dump(data, myfile)

def main():
    st.title("test write on share.streamlit.io")
    data = read_file(file_name)
    st.write("after read")
    st.write(data)
    data = change_content(data)
    write_file(data, file_name2)
    data = read_file(file_name2)
    st.write("after write")
    st.write(data)
    
if __name__ == '__main__':
    main()