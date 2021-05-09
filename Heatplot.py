import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import time 
import numpy as np
from datetime import datetime
matplotlib.style.use('bmh')



def heat_plot(c1, m1):
  
  # excel_data_df = pd.read_excel('/home/anna/Downloads/story.xls', usecols=[1, 4], names=['Time', 'Heat'], )
  # # введите массу
  # m1 = m_entry.get()
  # # # введите теплоемкость
  # c1 = c_entry.get()

  global excel_data_df

  time_list = excel_data_df['Time']
  temp_list = excel_data_df['Heat']

  # количество теплоты
  sizeoflist = len(temp_list)
  for i in range(sizeoflist-1):
    temp_list[i] = (temp_list[i+1]-temp_list[i])*c1*m1

  temp_list1 = temp_list.copy()
  temp_list1.drop(index=[0, 1], inplace=True)
  time_list.drop(index=[0, 1], inplace=True)
  temp_list = temp_list1

  excel_data_df['Heat'] = temp_list
  excel_data_df['Time'] = time_list
  plot = excel_data_df.plot('Time', 'Heat')
  #plt.show()
  plt.savefig('Test_plot.png')
  print(temp_list)





st.title('Построение графика количества теплоты')


# File uploader
st.subheader("Выберите файл с данными")
uploaded_file = st.file_uploader('')

st.subheader("Введите удельную теплоёмкость, Дж/кг*С")
c = st.number_input('')
st.write('Удельная теплоемкость: ', c)

st.subheader("Введите массу, кг")
m = st.number_input('  ')
st.write('Масса: ', m)

if uploaded_file is not None:
  excel_data_df = pd.read_excel(uploaded_file, usecols=[1, 4], names=['Time', 'Heat'])
  st.sidebar.write(excel_data_df)


if st.button("Построить график"):
  heat_plot(c, m)
  st.pyplot(plt)


# # Download line
# latest_iteration = st.empty()
# bar = st.progress(0)
# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.05)






