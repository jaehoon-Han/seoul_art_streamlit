import folium
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_folium import st_folium

def main():
    df = pd.read_csv('data/seoul_art.csv')
 
    st.title('서울시 문화예술')

    x = []
    y = []
    for i in range(771) :
        if float(df['X좌표'][i]) == 0.0 or float(df['Y좌표'][i]) == 0.0 :
            pass
        else :
            x.append(df['X좌표'][i])
            y.append(df['Y좌표'][i])

    map_osm = folium.Map(location = [x[13],y[13]],zoom_start=14)

    for i in range(len(x)) :
        folium.Marker([x[i],y[i]], popup=df.iloc[i,1:3].values, icon=folium.Icon(color='red',icon='info-sign')).add_to(map_osm)

    folium.CircleMarker(location=[x[13],y[13]],popup='주소',radius = 300,color="#3186cc", fill_color="#3186cc").add_to(map_osm)
    map_osm.save('seoul_art.html')
    
    st_data = st_folium(map_osm, width = 725)



if __name__=='__main__' :
    main()
