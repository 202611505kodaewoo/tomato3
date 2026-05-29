import streamlit as st
import pandas as pd
import joblib

# 1. 모델 읽어오기
model = joblib.load("tomato_model.pkl")

# 2. 앱 제목과 입력창
st.title("🌱 토마토 착과율 예측")

temp = st.number_input("내부 온도 (°C)", value=25.0)
humidity = st.number_input("내부 습도 (%)", value=60.0)
soil_temp = st.number_input("지온 (°C)", value=18.0)

# 3. 예측 버튼 및 결과 출력
if st.button("예측하기", type="primary"):
    # 입력 데이터를 데이터프레임으로 변환
    input_data = pd.DataFrame([[temp, humidity, soil_temp]], columns=['내부온도', '내부습도', '지온'])
    
    # 예측 및 출력
    predicted = model.predict(input_data)
    st.success(f"🎯 예상 착과율: {predicted[0]:.1f}%")