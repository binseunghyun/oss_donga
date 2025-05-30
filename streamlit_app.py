import streamlit as st
import pandas as pd

st.title("교통사고 발생 위치 시각화")

# 예시 데이터
data = pd.DataFrame({
    '위도': [35.1796, 35.1668, 35.18],
    '경도': [129.0756, 129.0726, 129.08],
    '사고유형': ['차 대 사람', '차 대 차', '차 대 사람']
})

# ✅ 필수: st.map을 위해 컬럼명 변경
data = data.rename(columns={'위도': 'latitude', '경도': 'longitude'})

type_option = st.selectbox("사고유형 선택", data['사고유형'].unique())
filtered_data = data[data['사고유형'] == type_option]

# 지도 출력
st.map(filtered_data[['latitude', 'longitude']])
