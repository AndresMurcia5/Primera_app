import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt 
import streamlit as st

st.title("Esto es una app")

df_m = gpd.read_file('hombres.geojson')
df_f = gpd.read_file('mujeres.geojson')

fig, ax = plt.subplots(1, 2, figsize=(10, 6))

df_m.plot(column='FT', ax=ax[0], legend=True, vmin=0.2,vmax=1)
ax[0].set_title('TGP = Hombres')
ax[0].axis('off')

df_f.plot(column='FT', ax=ax[1], legend=True,vmin=0.2,vmax=1)
ax[1].set_title('TGP = Mujeres')
ax[1].axis('off')


st.pyplot(fig)
