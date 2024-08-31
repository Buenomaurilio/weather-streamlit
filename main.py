import streamlit as st
import requests
# from streamlit import st_autorefresh

# Função que obtém os dados meteorológicos com cache de 5 minutos (300 segundos)
@st.cache_data(ttl=300)
def weather():
    api_key = 'cf76c2165242486d94361057241606'
    city = 'Dublin'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

    response = requests.get(url)
    data = response.json()
    return data

# Recarrega a página automaticamente a cada 5 minutos
# st.experimental_rerun = st_autorefresh(interval=300 * 1000)  # 300 segundos em milissegundos

city = 'Dublin'
st.write('''# Weather''')

col1, col2, col3 = st.columns([2, 1, 2])
col4, col5, col6 = st.columns([2, 1, 2])
col7, col8, col9 = st.columns([2, 1, 2])

# Executa a função para obter os dados do clima
data = weather()

# Extrai e exibe as informações
temp = data['current']['temp_c']
feelslike = data['current']['feelslike_c']
humidity = data['current']['humidity']
weather_description = data['current']['condition']['text']
wind = data['current']['wind_kph']
time = data['location']['localtime']

# Insere os dados nas colunas
with col1:
    st.write(f'{city}: {temp}°C')

with col3:
    st.write(f'Feels like: {feelslike}°C')

with col4:
    st.write(f'Humidity: {humidity}%')

with col6:
    st.write(f'Weather: {weather_description}')

with col7:
    st.write(f'Wind: {wind} km/h')

with col9:
    st.write(f'Local date time: {time}')
