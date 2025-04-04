import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns
import streamlit as st

st.title("Plotly 튜토리얼")

#tips 데이터셋 가져오기
tips = sns.load_dataset('tips')

#데이터 미리보기
st.subheader('데이터 미리보기')
st.dataframe(tips.head())

#기본 막대 그래프
st.subheader("1. 기본 막대 그래프")
fig = px.bar(tips, 
             x ='day', 
             y = 'tip', 
             title = '요일별 지불 금액',
             labels = {'day' : '요일', 'tip' : '평균 Tip($)'})
st.plotly_chart(fig, use_container_width=True)

# 산점도
st.subheader("2. 산점도")
fig1 = px.scatter(tips, 
                  x = 'total_bill',
                  y = 'tip',
                  color = "sex",
                  size = "size",
                  hover_data=["day","time","smoker","size"],
                  title = '요일별 지불 금액',
                  labels = {'total_bill' : '총합', 'tip' : '평균 Tip($)'})
st.plotly_chart(fig1)