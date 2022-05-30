import folium
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_folium import st_folium


def run_map() :
    pd.read_csv('data/seoul_art.csv')
    