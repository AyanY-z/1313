import streamlit as st
from curses import color_pair
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# Создание карты
map = folium.Map(location=[51.187911, 71.409788], zoom_start=16)

# Отображение карты
st.title("Карта кампуса")
st_folium(map, width=800, height=600)

# === 1. Подготовка данных ===
# Данные о локациях кампуса
data = [
    {"name": "Главное здание", "purpose": "Учебный корпус", "description": "Здесь проходят лекции", "latitude": 51.187317, "longitude": 71.409006},
    {"name": "Биокорпус", "purpose": "Асхана", "description": "Лучший препод Елубаев Дастан Рамазанович", "latitude": 51.187888, "longitude": 71.409773},
    {"name": "Кафе", "purpose": "Кафетерий", "description": "Кофе и закуски", "latitude": 51.187673, "longitude": 71.408765}
]

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# === 2. Создание карты с реальным базовым слоем ===
# Центральные координаты кампуса
campus_center = [51.187911, 71.409788] 

# Используем базовый слой OpenStreetMap
campus_map = folium.Map(location=campus_center, zoom_start=16, tiles="OpenStreetMap")
marker_cluster = MarkerCluster().add_to(campus_map)

# === 3. Добавление кластеризованных маркеров ===
marker_cluster = MarkerCluster().add_to(campus_map)

# Цветовая схема для разных типов зданий
color_map = {
    "Учебный корпус": "blue",
    "Кафетерий": "orange",
    "Биокорпус": "red"
}

# Добавление маркеров
for _, row in df.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"<b>{row['name']}</b><br>{row['purpose']}<br>{row['description']}",
        icon=folium.Icon(color=color_map.get(row["purpose"], "gray"), icon="info-sign")
    ).add_to(marker_cluster)

# === 4. Сохранение карты ===
campus_map.save("real_campus_map.html")

print("Карта сохранена как 'real_campus_map.html'. Откройте файл в браузере, чтобы посмотреть результат.")
