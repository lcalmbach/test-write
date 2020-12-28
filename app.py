import streamlit as st

def main():
    st.write('hello')
    f = open("./tmp/demofile.txt", "w")
    f.write("Now the file has some content!")
    f.close()

    f = open("./tmp/demofile.txt", "r")
    st.write(f.read())

if __name__ == '__main__':
    main()