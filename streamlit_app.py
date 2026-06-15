import streamlit as st

# 1. 앱 제목 및 상단 레이아웃
st.title("🧥 오늘의 기온별 의류 추천 시스템")
st.write("현재 기온을 입력하시면 알맞은 의류 목록을 추천해 드립니다.")
st.markdown("---")

# 2. 데이터 정의 (기존 로직 유지)
cold_clothes = ["코트", "패딩", "목도리"]
warm_clothes = ["셔츠", "청바지", "반팔"]

# 3. Streamlit 위젯을 통한 입력값 받기
# st.number_input을 사용해 기온(정수)을 입력받습니다.
temp = st.number_input(
    "오늘의 기온을 입력하세요 (°C):", 
    min_value=-40, 
    max_value=50, 
    value=18, 
    step=1
)

# 4. 핵심 조건문 로직 실행
if temp < 15:
    recommend = cold_clothes
    weather_status = "추운 날씨"
    alert_icon = "❄️"
else:
    recommend = warm_clothes
    weather_status = "따뜻한 날씨"
    alert_icon = "☀️"

# 5. 결과 출력 (버튼을 누르면 결과가 나오도록 구성)
if st.button("추천 의류 확인하기"):
    st.subheader(f"--- 오늘의 기온별 의류 목록 추천 ({weather_status}) ---")
    
    # 날씨 상태에 따라 성공/정보 메시지 박스 출력
    if temp < 15:
        st.error(f"{alert_icon} 오늘은 {weather_status}입니다. 따뜻하게 입으세요!")
    else:
        st.success(f"{alert_icon} 오늘은 {weather_status}입니다. 활동하기 좋은 날씨예요!")
        
    # 추천 아이템 리스트 출력
    st.write("**💡 추천 아이템:**")
    for item in recommend:
        st.info(f"👉 {item}")