import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
import plotly.express as px
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial'; 
        font-size: 10px; 
        color: black;
        bold:True;
        direction: rtl;
        text-align: right; 
    }
    p{
        font-family: 'Arial'; 
        font-size: 24px; 
        direction: rtl;
        text-align: right;   
    }
    h4{
        text-align: center;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

df = pd.read_csv("Jadarat_data_after.csv")
df1 = df["region"].value_counts().head(10)

st.title("وضع الوظائف في المملكة العربية السعودية.")
st.markdown("<hr>",unsafe_allow_html=True)
st.markdown("بحكم اني تخرجت من الجامعة قبل شهرين كان ودي اشوف وش وضع سوق العمل السعودي ومتطلباته فا رحت لاحد اشهر مواقع التوظيف في السعودية ومن جهه حكوميه الي هو جدارات ولقيت بيانات للوظائف في جدارات للسنة 2023.")
st.markdown("https://www.kaggle.com/datasets/moayadalkhozayem/job-postings-in-saudi-arabia")
st.markdown("<hr>",unsafe_allow_html=True)
st.markdown("أول شي كنت اريد ان اعرفة وين تتركز الوظائف المعروضه فيه وهل هي قريبه مني بحكم اني ساكن بمحافظة ثادق؟.")
st.markdown("#### نسبة الوظائف لكل منطقة 🏙️")
fig = px.pie(df1 , values=df1.values,names=df1.index,width=800,height=500,hole=.5,title=" ",color_discrete_sequence=px.colors.sequential.Mint)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(
    title={
        'x': 0.43,
        'xanchor': 'center' 
    })
st.plotly_chart(fig)
st.markdown("<hr>",unsafe_allow_html=True)
st.markdown("بحكم الرياض كالعادة هي الاعلى ودي اعرف  كم عدد الوظائف الموجوده والى اي قطاع تنتمي خاص او حكومي ؟")
df2 = df[df["region"] == "الرياض"]
df3 = df2["comp_type"].value_counts()
fig2 = px.bar(df3,x=df3.index, y=df3.values ,title = "عدد الوظائف لكل قطاع",width=800,height=700,color_discrete_sequence=px.colors.sequential.Mint)
fig2.update_layout( title={
        'x': 0.53,
        'xanchor': 'center' 
    },xaxis_title="نوع القطاع",
                     yaxis_title="العدد الكلي")
fig2
st.markdown("<hr>",unsafe_allow_html=True)
st.markdown("عدد الوظائف في القطاع الخاص عالي جدا مقارنة بالباقي ,هذا يطرح سؤال لدي هل اغلب الوظائف المعروضه تتطلب خبره ؟ ام العكس صحيح؟ ")
fig3 = px.bar(df2,x = df2["exper"].value_counts().index, y=df2["exper"].value_counts().values ,title = "عدد الوظائف بناء على الخبرة",width=800,height=700,color_discrete_sequence=px.colors.sequential.Mint)
fig3.update_layout( title={
        'x': 0.53,
        'xanchor': 'center' 
    },xaxis_title="الخبرة المطلوبه",
                     yaxis_title="العدد الكلي")
fig3

st.markdown("<hr>",unsafe_allow_html=True)
st.markdown("عدد جميل من الوظائف يطلب حديثي تخرج وهذا يطرح سؤال جديد لدي , لو توظفت كم بيكون معدل راتبي تقريبا ؟ 🤔 ")
df4 = df2[df2["exper"] == "0 Years"]
fig4 = px.histogram(df4, x="benefits",color_discrete_sequence=px.colors.sequential.Mint)
fig4
df5 = df4["gender"].value_counts()
st.markdown("<hr>",unsafe_allow_html=True)
st.markdown("الوظائف الموجوده هل محدد جنس معين او الكل , وماهي النسبه الاكبر؟")
fig5= px.pie(df5 , values=df5.values,names=df5.index,width=800,height=500,hole=.5,title="تصنيف الوظائف بناء على الجنس",color_discrete_sequence=px.colors.sequential.Mint)
fig5.update_layout( title={
        'x': 0.45,
        'xanchor': 'center' 
})
fig5.update_traces(labels=("كلاهما", "انثى","ذكر"),textposition='inside', textinfo='percent+label')
fig5
st.markdown("<hr>",unsafe_allow_html=True)