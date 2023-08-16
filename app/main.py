import streamlit as st
import json
import requests
import base64

from pydantic import BaseModel
from datetime import datetime




class Condition(BaseModel):
    humidity: float
    date_str : str
    hour : int
    surface_sum: float
    building_type : str




date = st.sidebar.date_input("날짜를 입력해주세요 : ")
date_str = str(date)
hour = st.sidebar.selectbox("시간을 입력해주세요 (0시~23시)",(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23))
surface_sum = st.sidebar.number_input("연면적(m2)을 입력해주세요 : ")
# building_type = st.sidebar.selectbox("건물 유형을 선택해주세요",('건물유형_건물기타', '건물유형_공공', '건물유형_대학교', '건물유형_데이터센터', '건물유형_백화점및아울렛','건물유형_병원', '건물유형_상용', '건물유형_아파트', '건물유형_연구소', '건물유형_지식산업센터','건물유형_할인마트', '건물유형_호텔및리조트'))
building_type = "건물유형_건물기타"
humidity = st.sidebar.number_input("습도(%)를 입력해주세요 : ")

data = {"humidity":humidity,
        "date":date_str,
        "hour":hour,
        "surface_sum":surface_sum,
        "building_type":building_type}

dataJson = json.dumps(data)
# 입력된 데이터를 FastAPI 어플리케이션으로 post 요청
pred = requests.post(url="http://192.168.70.24:8121/get_power_use/",data=dataJson)

st.write(f"예측된 전력 소비량은 {pred.json()}kW 입니다.")




