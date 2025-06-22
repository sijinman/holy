import streamlit as st

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="우리 가족!",
    page_icon="👨‍👩‍👧‍👦",
    layout="wide" # 넓은 레이아웃으로 설정
)

# --- 제목 ---
st.title("❤️ 소중한 우리 가족을 소개합니다 ❤️")
st.write("---")

# --- 프로필 섹션 (3개의 칸으로 나누기) ---
col1, col2, col3 = st.columns(3)

# 첫 번째 칸 (BB 프로필)
with col1:
    st.header("첫째 쁘니")
    # 이 코드는 작동하는 것을 확인했습니다.
    st.image("bb.jpg", caption="우리집 예쁘니")
    
    st.write("**특징:** 고등어 무늬에 뒷발엔 양말 무늬!")
    with st.expander("자세히 보기"):
        st.write("""
            - 좋아하는 것: 우다다, 아빠랑 놀기
            - 좋아하는 간식: 황태, 츄르
        """)

# 두 번째 칸 (YY 프로필)
with col2:
    st.header("둘째 요미")
    # 이 코드는 작동하는 것을 확인했습니다.
    st.image("yy.jpg", caption="보기엔 귀엽지만 엄청 도도")

    st.write("**특징:** 조용하고 잠이 많음")
    with st.expander("자세히 보기"):
        st.write("""
            - 좋아하는 것: 일광욕, 캣휠, 오빠 따라다니기
            - 좋아하는 간식: 닭가슴살, 츄르
        """)

# 세 번째 칸 (GG 프로필)
with col3:
    st.header("셋째 감자")
    # 이 코드는 작동하는 것을 확인했습니다.
    st.image("gg.jpg", caption="에너자이저 막내")
    
    st.write("**특징:** 덩치는 제일 크지만 서열꼴찌")
    with st.expander("자세히 보기"):
        st.write("""
            - 취미: 캣타워 뿌시기
            - 좋아하는 간식: 뭐든지 다 잘먹음
        """)

# --- 추가 기능 ---
st.write("---")
st.header("🎉 축하 버튼 🎉")
if st.button("우리 아이들, 앞으로도 행복하자!"):
    st.balloons()
    st.success("사랑해! ❤️")