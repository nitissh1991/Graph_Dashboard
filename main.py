import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def set_axis_colors(ax, color):
    ax.spines['left'].set_color(color)
    ax.tick_params(axis='y', colors=color)
    ax.yaxis.label.set_color(color)

def plot_graph(df_data, x_column_name, y_param):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlabel(x_column_name)
    ax.set_xlim(y_param['x_min'], y_param['x_max'])
    ax.set_xticks(np.arange(y_param['x_min'], y_param['x_max'] + y_param['x_increment'], y_param['x_increment']))

    ax.plot(df_data[x_column_name], df_data[y_param['column']], color=y_param['color'], label=y_param['column'])

    ax.set_ylabel(y_param['column'], color=y_param['color'])
    ax.set_ylim(y_param['y_min'], y_param['y_max'])
    ax.set_yticks(np.arange(y_param['y_min'], y_param['y_max'] + y_param['y_increment'], y_param['y_increment']))
    set_axis_colors(ax, y_param['color'])

    ax.legend(loc='upper left')
    fig.tight_layout()
    ax.grid(True, which='major', axis='both', color='grey')

    st.pyplot(fig)

st.title('Dynamic Data Plotter')

excel_file = st.file_uploader("Upload your data file", type=['xlsx'])
if excel_file:
    df_data = pd.read_excel(excel_file, sheet_name='Sheet1', skiprows=3)
    x_column_name = st.selectbox('Select X-axis', df_data.columns)

    y_column_name = st.selectbox('Select Y-axis', df_data.columns)
    y_color = st.color_picker('Pick a color for Y-axis', '#00f900')
    y_min = st.number_input('Min value for Y-axis', value=float(df_data[y_column_name].min()))
    y_max = st.number_input('Max value for Y-axis', value=float(df_data[y_column_name].max()))
    y_increment = st.number_input('Increment for Y-axis', value=1.0)

    x_min = st.number_input('Min value for X-axis', value=float(df_data[x_column_name].min()), key='x_min')
    x_max = st.number_input('Max value for X-axis', value=float(df_data[x_column_name].max()), key='x_max')
    x_increment = st.number_input('Increment for X-axis', value=1.0, key='x_increment')

    y_param = {
        'column': y_column_name,
        'color': y_color,
        'y_min': y_min,
        'y_max': y_max,
        'y_increment': y_increment,
        'x_min': x_min,
        'x_max': x_max,
        'x_increment': x_increment
    }

    if st.button('Plot Graph'):
        plot_graph(df_data, x_column_name, y_param)
