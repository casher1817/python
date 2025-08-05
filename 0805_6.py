from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    # 地球半徑 (公里)
    R = 6371.0

    # 轉為弧度
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

# 範例城市座標（台北、高雄）
cities = {
    'Taipei': (25.0330, 121.5654),
    'Kaohsiung': (22.6273, 120.3014)
}

city1 = 'Taipei'
city2 = 'Kaohsiung'

lat1, lon1 = cities[city1]
lat2, lon2 = cities[city2]

distance = haversine(lat1, lon1, lat2, lon2)
print(f"{city1} 和 {city2} 之間的距離為 {distance:.2f} 公里")