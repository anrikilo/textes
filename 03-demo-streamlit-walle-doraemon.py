import streamlit as st
import os
from fastai.vision.all import *
import pathlib
import sys
import pandas as pd
import random

data_df = pd.read_excel('transformed_jester_data.xlsx')
jokes_df = pd.read_excel('Dataset4JokeSet.xlsx')

import numpy as np  

  

  
# 读取包含笑话的 Excel 文件  
jokes_df = pd.read_excel('Dataset4JokeSet.xlsx')  
  
# 假设 jokes_df 有一个名为 'joke' 的列，存储了笑话文本  
random_index = np.random.choice(jokes_df.index, 3, replace=True)[0]  # 获取随机行的索引  
random_joke = jokes_df.loc[random_index, 'joke']  # 从 'joke' 列中获取该行的笑话文本  
  
st.title("推荐系统给笑话打分")  
st.write("随机生成的笑话:")  
st.text(random_joke)  # 显示随机生成的笑话  
  
level = st.slider("Select your level", 1, 5)  
st.write("You selected: ", level)  
  
# 假设 jokes_df 有一个名为 'joke' 的列，存储了笑话文本  
random_index = np.random.choice(jokes_df.index, 3, replace=True)[0]  # 获取随机行的索引  
random_joke = jokes_df.loc[random_index, 'joke']  # 从 'joke' 列中获取该行的笑话文本  
  
st.text(random_joke)  # 显示随机生成的笑话  
  
level1 = st.slider("Select your level1", 1, 5)  
st.write("You selected: ", level1)  

# 假设 jokes_df 有一个名为 'joke' 的列，存储了笑话文本  
random_index = np.random.choice(jokes_df.index, 3, replace=True)[0]  # 获取随机行的索引  
random_joke = jokes_df.loc[random_index, 'joke']  # 从 'joke' 列中获取该行的笑话文本  
  
st.text(random_joke)  # 显示随机生成的笑话  
  
level2 = st.slider("Select your level2", 1, 5)  
st.write("You selected: ", level2)  

st.header("推荐的笑话")

data_df.columns = ["user_id","joke_id" ,"rating"]
data_df['user_id']=data_df.index
jokes_df.columns=['joke']
jokes_df['joke_id']=jokes_df.index
ratings = data_df.merge(jokes_df,on = 'joke_id')
train_ratings = ratings
test_ratings = ratings

joke_id1='107'
joke_id2='149'
joke_id3='34'
new_user_id = ratings['user_id'].max() + 1
new_ratings_df = pd.DataFrame({
    'user': [new_user_id, new_user_id,new_user_id],
    'joke': [joke_id1,joke_id2,joke_id3],
    'rating': [19,9,2],
    
})
ratings = pd.concat([ratings, new_ratings_df])
joke_ids = ratings['joke_id'].unique()  # 获取所有电影ID列表
joke_ids_new_user = ratings.loc[ratings['user_id'] == new_user_id, 'joke']  # 获取新用户评分的电影ID列表
joke_ids_to_pred = np.setdiff1d(joke_ids, joke_ids_new_user)  # 获取新用户未评分的电影ID列表
top10_jokes = data_df[data_df['joke_id'].isin(joke_ids_to_pred)].sort_values(by='rating', ascending=False).head(10)[['joke_id', 'rating']]


  # 假设你有一个基于1的列号  
excel_row_number1 = 73 
pandas_row_index1 = excel_row_number1 - 1  
row_data1 = jokes_df.iloc[pandas_row_index1]  
print(row_data1)
st.text(row_data1)
level11 = st.slider("Select your level11", 1, 5)  
st.write("You selected: ", level11)  

excel_row_number2= 20
pandas_row_index2 = excel_row_number2 - 1 
row_data2 = jokes_df.iloc[pandas_row_index2]  
print(row_data2)
st.text(row_data2)
level12 = st.slider("Select your level12", 1, 5)  
st.write("You selected: ", level12)  

excel_row_number3 = 108
pandas_row_index3 = excel_row_number3 - 1  
row_data3 = jokes_df.iloc[pandas_row_index3]  
print(row_data3)
st.text(row_data3)
level13 = st.slider("Select your level13", 1, 5)  
st.write("You selected: ", level13)  

excel_row_number4 = 30
pandas_row_index4 = excel_row_number4 - 1  
row_data4 = jokes_df.iloc[pandas_row_index4] 
print(row_data4) 
st.text(row_data4)
level14 = st.slider("Select your level14", 1, 5)  
st.write("You selected: ", level14) 

excel_row_number5 = 132
pandas_row_index5 = excel_row_number5 - 1  
row_data5 = jokes_df.iloc[pandas_row_index5]  
print(row_data5)
st.text(row_data5)
level15 = st.slider("Select your level15", 1, 5)  
st.write("You selected: ", level15) 

# 根据不同的操作系统设置正确的pathlib.Path
if sys.platform == "win32":
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath
else:
    temp = pathlib.WindowsPath
    pathlib.WindowsPath = pathlib.PosixPath

# 获取当前文件所在的文件夹路径
path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(path,"jokes.pkl")

# 加载模型
learn_inf = load_learner(model_path)

# 恢复pathlib.Path的原始值
if sys.platform == "win32":
    pathlib.PosixPath = temp
else:
    pathlib.WindowsPath = temp

  

