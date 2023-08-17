from pydantic import BaseModel
from datetime import datetime
import streamlit as st
import requests
import json


date = st.date_input("날짜를 입력해주세요 : ")
hour = st.selectbox("시간을 입력해주세요 (0시~23시)",(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23))
surface_sum = st.number_input("연면적(m2)을 입력해주세요 : ")
humidity = st.number_input("습도(%)를 입력해주세요 : ",min_value=0)
temperature = st.number_input("온도(°C)를 입력해주세요 : ",min_value=0.0)
rain_sum = st.number_input("강수량(mm)를 입력해주세요 : ",min_value=0.0)
building_type = st.selectbox("건물 유형을 선택해주세요",('건물유형_건물기타', '건물유형_공공', '건물유형_대학교', '건물유형_데이터센터', '건물유형_백화점및아울렛','건물유형_병원', '건물유형_상용', '건물유형_아파트', '건물유형_연구소', '건물유형_지식산업센터','건물유형_할인마트', '건물유형_호텔및리조트'))
power_use = st.number_input("전력 사용량(kWh)을 입력해주세요",min_value=0.0)

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
day = date.day

extra_data = {
    "humidity":humidity,
    "year":year,
    "month":month,
    "day":day, 
    "hour":hour,
    "surface_sum":surface_sum,
    "building_type":building_type_db,
    "power_use":power_use,
    "feedback_datetime":str(datetime.today()),
    "rain_sum":rain_sum,
    "temperature":temperature
    }

extra_dataJson = json.dumps(extra_data)
button = st.button("데이터 제공")
if button:
    headers = {
    'accept': '*/*',
    'Content-Type': 'application/json',
    }
    requests.post(url="http://192.168.70.35:5600/send_feedback",headers=headers,data=extra_dataJson)
