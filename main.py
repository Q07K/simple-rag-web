import streamlit as st
from dotenv import load_dotenv


def main():
    print("Hello from simple-rag-web!")


if __name__ == "__main__":
    load_dotenv()
    main()
    st.switch_page("pages/login_page.py")
