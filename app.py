import folium
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_folium import st_folium

def main():

    st.title('서울시 문화예술')

    m = folium.Map(location=[37.5389, 127.0546], zoom_start = 14)
    m
    




if __name__=='__main__' :
    main()
