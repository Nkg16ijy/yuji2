import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import japanize_matplotlib
%matplotlib inline

data_csv_path = "kakeibo.csv"
df_kakeibo_data = pd.read_csv(data_csv_path, encoding="shift-jis")

st.title("＊家計簿＊")
st.write("最終更新日: 2022/12/21")
st.write("")

#合計支出
st.subheader('1. 合計支出')
df_part = pd.DataFrame(
    [[170470],[119326]],
    index = ['2022/11', '2022/12'],
    columns = ['合計支出']
)   

st.dataframe(df_part)
df_kakeibo_data.plot.barh("koumoku", {"22-Nov", "22-Dec"}, color={"BM": "gray", "22-Nov": "blue", "22-Dec": "red"})
st.write("")



#項目別支出
st.subheader('2. 項目別支出')
df_part = pd.DataFrame(
    [[75930],[75930],[18088],[0],[8012],[8538],[2802],[0],[46325],[24620],[19313],[9638],[0],[600]],
    index = ['家賃/11月', '家賃/12月','ガス代/11月','ガス代/12月','電気代/11月','電気代/12月','水道代/11月','水道代/12月','食費/11月','食費/12月','日用品費/11月','日用品費/12月','交際費/11月','交際費/12月',],
    columns = ['項目別支出']
)   

st.dataframe(df_part)
data_csv_path2 = "kakeibo2.csv"
df_kakeibo2_data = pd.read_csv(data_csv_path2, encoding="shift-jis")

df_kakeibo2_data
df_kakeibo2_data.plot.barh("food", {"22-Nov", "22-Dec"}, color={"22-Nov": "blue", "22-Dec": "red"})
st.write("")

#食費内訳
st.subheader('3. 食費内訳')
df_part = pd.DataFrame(
    [[5599],[2515],[3732],[2087],[3020],[0],[6552],[2701],[9063],[3175],[3339],[1627],[1543],[2606],[4400], [2290],[7000],[6999],[2077],[620]],
    index = ['食材(野菜・くだもの類)/11月', '食材(野菜・くだもの類)/12月','食材(肉・魚介類)/11月','食材(肉・魚介類)/12月','食材(米類)/11月','食材(米類)/12月','食材(その他)/11月','食材(その他)/12月','軽食/11月','軽食/12月','調味料/11月','調味料/12月','飲み物/11月','飲み物/12月','お菓子・アイス/11月','お菓子・アイス/12月','外食/11月','外食/12月','外税/11月','外税/12月'],
    columns = ['食費内訳']
)   

st.dataframe(df_part)
data_csv_path2 = "kakeibo2.csv"
df_kakeibo3_data = pd.read_csv(data_csv_path2, encoding="shift-jis")

df_kakeibo3_data
df_kakeibo3_data.plot.barh("food", {"22-Nov_unit", "22-Dec_unit"}, color={"22-Nov_unit": "blue", "22-Dec_unit": "red"})
st.write("")

#食費日割り
st.subheader('4. 食費日割り')
df_part = pd.DataFrame(
    [[1544.2],[1538.8]],
    index = ['2022/11', '2022/12'],
    columns = ['食費日割り']
)   

st.dataframe(df_part)
st.bar_chart(df_part)