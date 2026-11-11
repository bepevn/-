from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CHAIN : 잔광", page_icon="⛓️", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
.stApp {background:#060912;}
.block-container {padding:0.6rem 0.8rem 0;max-width:1600px;}
header[data-testid="stHeader"] {background:transparent;height:0;}
footer {display:none;}
</style>""", unsafe_allow_html=True)
components.html(Path(__file__).with_name("game.html").read_text(encoding="utf-8"), height=820, scrolling=False)
with st.expander("조작 / v5 모듈"):
    st.markdown("""
- W 점프 / Q 대시 / E 궁극기 / R 산데비스탄 / T 전격 / C 속박 / F 상호작용.
- 좌클릭 유지: 로프 런처를 장착했을 때만 사용 가능. 최대 연결 거리 620px. 우클릭 또는 J 베기.
- 평타(우클릭/J)로 가까운 전방 적 탄환을 반사합니다. 방어 피막은 제거되었습니다.
- 우측 하단 퇴장 버튼 또는 일시정지 메뉴에서 중간 퇴장할 수 있습니다.
- 출격 전 슬롯 2개에 모듈을 자유롭게 조합하세요. 빈 슬롯 허용, 같은 모듈 중복 불가.
- 다른 모듈은 로프 사거리나 견인력을 바꾸지 않습니다.
- 연습장은 체력과 에너지 무제한, B 정비실, N 연습장 리셋.
- A/D 이동, P 일시정지, M 음소거. PC 키보드와 마우스 권장.
""")
