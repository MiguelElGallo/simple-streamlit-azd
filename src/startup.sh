#!/bin/bash
set -e
python3 -m pip install --upgrade pip
pip3 install streamlit
python3.9 -m streamlit run stlitapp.py --server.port 8000 --server.address 0.0.0.0
