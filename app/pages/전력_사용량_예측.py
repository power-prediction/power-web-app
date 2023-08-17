import streamlit as st
import json
import requests
# import base64

from pydantic import BaseModel
from datetime import datetime




class Condition(BaseModel):
    temperature : float
    rain_sum : float
    humidity : int
    date_str : str
    hour : int
    surface_sum : float
    building_type : str

col1, col2 = st.columns([3,2])

with col2:
    date = st.date_input("날짜를 입력해주세요 : ")
    date_str = str(date)
    hour = st.selectbox("시간을 입력해주세요 (0시~23시)",(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23))
    surface_sum = st.number_input("연면적(m2)을 입력해주세요 : ",min_value=0.0)
    building_type = st.selectbox("건물 유형을 선택해주세요",('건물유형_건물기타', '건물유형_공공', '건물유형_대학교', '건물유형_데이터센터', '건물유형_백화점및아울렛','건물유형_병원', '건물유형_상용', '건물유형_아파트', '건물유형_연구소', '건물유형_지식산업센터','건물유형_할인마트', '건물유형_호텔및리조트'))    
    # building_type = "건물유형_건물기타"
    humidity = st.number_input("습도(%)를 입력해주세요 : ",min_value=0)
    temperature = st.number_input("온도(°C)를 입력해주세요 : ",min_value=0.0)
    rain_sum = st.number_input("강수량(mm)를 입력해주세요 : ",min_value=0.0)


building_type_db = ""
if building_type == "건물유형_건물기타":
    building_type_db = "etc"
if building_type == "건물유형_공공":
    building_type_db = "public"
if building_type == "건물유형_대학교":
    building_type_db = "university"
if building_type == "건물유형_데이터센터":
    building_type_db = "data_center"
if building_type == "건물유형_백화점및아울렛":
    building_type_db = "department&outlet"
if building_type == "건물유형_병원":
    building_type_db = "hostpital"
if building_type == "건물유형_상용":
    building_type_db = "general"
if building_type == "건물유형_아파트":
    building_type_db = "apartment"
if building_type == "건물유형_연구소":
    building_type_db = "lab"
if building_type == "건물유형_지식산업센터":
    building_type_db = "knowledge_center"
if building_type == "건물유형_할인마트":
    building_type_db = "market"
if building_type == "건물유형_호텔및리조트":
    building_type_db = "hotel"

year = date.year
month = date.month
day = date.month

data = {
    "temperature":temperature,
    "rain_sum":rain_sum,
    "humidity":humidity,
    "date":date_str,
    "hour":hour,
    "surface_sum":surface_sum,
    "building_type":building_type
    }

dataJson = json.dumps(data)
# 입력된 데이터를 FastAPI 어플리케이션으로 post 요청
with col2:
    button = st.button("적용")
if button:
    pred = requests.post(url="https://192.168.70.35/get_power_use/",data=dataJson)

    db_data = {
        "temperature":temperature,
        "rain_sum":rain_sum,
        "humidity":humidity,
        "year":year,
        "month":month,
        "day":day, 
        "hour":hour,
        "surface_sum":surface_sum,
        "building_type":building_type_db,
        "power_pred":pred.json(),
        "log_datetime":str(datetime.now())
    }
    db_dataJson = json.dumps(db_data)

    headers = {
    'accept': '*/*',
    'Content-Type': 'application/json',
    }
    requests.post(url="http://192.168.70.35:5600/send_log",headers=headers,data=db_dataJson)
    with col1:
        st.write(f"예측된 전력 소비량은 {pred.json()}kWh 입니다.")




