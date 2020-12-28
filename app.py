import streamlit as st
import os
def main():
    st.write('hello')

    file_name = os.path.join("tmp", "demofile.txt")
    f = open(file_name, "w")
    f.write("Now the file has some content!")
    f.close()

    f = open(file_name, "r")
    st.write(f.read())

if __name__ == '__main__':
    main()