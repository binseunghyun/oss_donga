import streamlit as st
import pandas as pd

st.title("부산시 교통사고 지도 (연도 + 사고유형 필터)")

# 데이터 불러오기
df = pd.read_excel("교통사고_GIS정보_20231231.xlsx")

# 날짜 파싱
df['발생일'] = pd.to_datetime(df['발생일'], errors='coerce')
df['연도'] = df['발생일'].dt.year

# 필수 컬럼 전처리
df = df.rename(columns={'위도': 'latitude', '경도': 'longitude'})

# 부산시만 필터
df = df[df['시도'].str.contains("부산", na=False)]

# 연도 필터 (2023, 2024만 허용)
df = df[df['연도'].isin([2023, 2024])]

# --- 위젯 입력 ---
year = st.selectbox("연도 선택", sorted(df['연도'].unique()))
accident_types = df['사고유형'].unique()
selected_types = st.multiselect("사고유형 선택", accident_types, default=accident_types)

# --- 필터링 ---
filtered = df[(df['연도'] == year) & (df['사고유형'].isin(selected_types))]

# 지도 출력
st.map(filtered[['latitude', 'longitude']])

# 데이터 개수 표시
st.write(f"사고 건수: {len(filtered)}건")
