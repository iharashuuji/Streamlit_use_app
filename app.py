#%%
import streamlit as st
import numpy as np
import pandas as pd


st.title('My First Streamlit App')
st.write("Hello, World")

#%%
# App title name
st.title("Streamlit App")
# text input 
name = st.text_input("Error your name:")
if name:
    st.write(f"Hello, {name}!")
#%%

upload_file = st.file_uploader("Choose a file")

if upload_file is not None:
    
    st.write("Filename:", upload_file.name)
    
    file_content = upload_file.read().decode("utf-8")
    
    st.write(file_content)
#%%
# gragh display
data = pd.DataFrame({
    'x':np.random.randn(100),
    'y':np.random.randn(100),
})

st.line_chart(data)

#%%
# サンプルデータフレームを作成
df = pd.DataFrame( np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
# インタラクティブなテーブル
st.subheader('st.dataframeによる表示 (インタラクティブ)')
st.dataframe(df)
# 静的なテーブル
st.subheader('st.tableによる表示 (静的)')
st.table(df.head(10)) # 先頭10行だけ表示


#%%
# 評価指数の表示 metrics
import streamlit as st
st.subheader('st.metricによるKPI表示')
col1, col2, col3 = st.columns(3)
col1.metric("気温", "25 °C", "1.2 °C")
col2.metric("風速", "9 mph", "-8%")
col3.metric("湿度", "86%", "4%", delta_color="inverse")


#%%
st.radio("好きなマイケルは？", ('ジャクソン', 'ジョーダン', 'ホフマン'))

#%%