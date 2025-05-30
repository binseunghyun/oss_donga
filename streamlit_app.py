import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🚗 부산시 교통사고 통계 분석 (2023~2024)")

# 데이터 불러오기
df = pd.read_excel("사고분석-지역별.xlsx")

# 연도 파싱
df['연도'] = df['발생년월'].astype(str).str[:4].astype(int)

# 필터링: 차대사람/차대차만
df = df[df['사고유형'].str.contains('차대사람|차대차')]

# --- 입력 위젯 ---
year = st.selectbox("연도 선택", sorted(df['연도'].unique()))
type_option = st.selectbox("사고유형 선택", df['사고유형'].unique())

filtered = df[(df['연도'] == year) & (df['사고유형'] == type_option)]

st.markdown("---")
st.header(f"📊 {year}년 {type_option} 사고 분석 결과")

# --- 1. 사고 목록 출력 ---
st.subheader("사고 데이터 표")
st.dataframe(filtered)

# --- 2. 시군구별 사고건수 ---
st.subheader("📍 시군구별 사고 건수 (Bar Chart)")
st.bar_chart(filtered['시군구'].value_counts())

# --- 3. 사고유형별 전체 건수 비교 ---
st.subheader("📌 전체 사고유형별 건수 (Bar Chart)")
st.bar_chart(df[df['연도'] == year]['사고유형'].value_counts())

# --- 4. 사망자, 중상자 합계 표시 ---
st.subheader("☠️ 사고 심각도 지표")
col1, col2 = st.columns(2)
col1.metric("사망자 총합", int(filtered['사망자수'].sum()))
col2.metric("중상자 총합", int(filtered['중상자수'].sum()))

# --- 5. 노면상태 / 기상상태 분포 ---
st.markdown("### 🌧️ 환경 요인 통계")
col3, col4 = st.columns(2)
with col3:
    st.write("기상상태별 사고 수")
    st.dataframe(filtered['기상상태'].value_counts())
with col4:
    st.write("노면상태별 사고 수")
    st.dataframe(filtered['노면상태'].value_counts())
