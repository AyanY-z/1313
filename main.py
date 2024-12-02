import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# === 1. Подготовка данных ===
# Данные о локациях кампуса
data = [
    {"name": "Главное здание", "purpose": "Учебный корпус", "description": "Здесь проходят лекции", "latitude": 51.187317, "longitude": 71.409006},
    {"name": "Биокорпус", "purpose": "Асхана", "description": "Лучший препод Елубаев Дастан Рамазанович", "latitude": 51.187888, "longitude": 71.409773},
    {"name": "Кафе", "purpose": "Кафетерий", "description": "Кофе и закуски", "latitude": 51.187673, "longitude": 71.408765}
]

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# === 2. Создание карты с кластеризованными маркерами ===
campus_center = [51.187911, 71.409788]
campus_map = folium.Map(location=campus_center, zoom_start=16, tiles="OpenStreetMap")
marker_cluster = MarkerCluster().add_to(campus_map)

# Цветовая схема для разных типов зданий
color_map = {
    "Учебный корпус": "blue",
    "Кафетерий": "orange",
    "Асхана": "red"
}

# Добавление маркеров
for _, row in df.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"<b>{row['name']}</b><br>{row['purpose']}<br>{row['description']}",
        icon=folium.Icon(color=color_map.get(row["purpose"], "gray"), icon="info-sign")
    ).add_to(marker_cluster)

# === 3. Отображение карты в Streamlit ===
st.title("Карта кампуса")
st_folium(campus_map, width=800, height=600)
