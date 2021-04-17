import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


image = Image.open('search.jpg')
st.sidebar.image(image,width=120)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
	bytes_data = uploaded_file.getvalue()
	st.write(bytes_data)
	stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
	st.write(stringio)
	string_data = stringio.read()
	st.write(string_data)
	dataframe = pd.read_csv(uploaded_file)
	st.write(dataframe)

#uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

st.sidebar.subheader("SELECT SEARCH METHOD")
add_selectbox = st.sidebar.radio("  ",
    ("Cosine Similarity", "FAISS","Spotify Annoy")
)


if add_selectbox == 'Cosine Similarity' :
 st.title("Similar Products using Cosine Similarity Search")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
     return pd.read_csv('image_csv.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 #images1 = df['second']
 
 st.subheader("Select from uploaded :")
 uploaded_files = st.file_uploader("Choose image file", accept_multiple_files=True)
 st.write("**You selected:**")
 for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.getvalue()
    st.image(bytes_data,width=None)
    st.write("-------------------------------------------------------------------------------------------------")
    st.subheader("Output:")
    st.write('Similar Products: ')
    for index, row in df.iterrows():
      if row['0']==bytes_data:
          while n < z+1:      
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1
 st.subheader("Select a Product :")
 pic = st.selectbox('Choices:', images)
 st.write("**You selected:**")
 st.image(pic,width=None)


 z = st.slider('Select Number of Similar Product:', 1, 10, 5)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("Output:")
 st.write('Similar Products: ')
 for index, row in df.iterrows():
     if row['0']==pic:
         while n < z+1:
            
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1

elif add_selectbox == 'FAISS':
 st.title("Similar Products using Faiss - Facebook AI Similarity Search")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
     return pd.read_csv('df.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 st.subheader("Select a Product :")
 pic = st.selectbox('Choices:', images)
 st.write("**You selected:**")
 st.image(pic,width=None)


 z = st.slider('Select Number of Similar Products:', 1, 10, 5)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("Output:")
 st.write('**Similar Products:**')
 for index, row in df.iterrows():
     if row['0']==pic:
         while n < z+1:
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1

elif add_selectbox == 'Spotify Annoy' :
 st.title("Similar Products using Spotify Annoy Search")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
     return pd.read_json('nearest_neighbors.json')
 n=1
 df = get_data()
 images = df['master_pi'].unique()
 images+=df['similar_pi'].unique()

 st.subheader("Select a Product :")
 pic = st.selectbox('Choices:', images)
 st.write("**You selected:**")
 st.write(str(int(pic)))


 z = st.slider('Select Number of Similar Product:', 1, 10, 5)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("Output:")
 st.write('Similar Products: ')
 for index, row in df.iterrows():
     if row['similar_pi']==pic:
         while n < z+1:
            
             st.write(row[n])
             n+=1