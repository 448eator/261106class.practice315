import streamlit as st
from html import escape

st.set_page_config(page_title="먼작귀 캐릭터 도감", page_icon="🍀", layout="wide")

CHARACTERS = [
    {"name": "치이카와", "group": "주요 친구", "symbol": "ち", "color": "#f6d5d9"},
    {"name": "하치와레", "group": "주요 친구", "symbol": "は", "color": "#c9e2ef"},
    {"name": "우사기", "group": "주요 친구", "symbol": "う", "color": "#f5e5a6"},
    {"name": "모몽가", "group": "친구들", "symbol": "も", "color": "#d8d1ed"},
    {"name": "쿠리만쥬", "group": "친구들", "symbol": "く", "color": "#e9c9ad"},
    {"name": "시사", "group": "친구들", "symbol": "シ", "color": "#d3e7c9"},
    {"name": "랏코", "group": "친구들", "symbol": "ラ", "color": "#c9d8ed"},
]

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Jua&display=swap');
    :root {
        --ink: #263b36;
        --muted: #74837c;
        --coral: #e87968;
        --leaf: #739c73;
        --paper: #fffdf8;
        --line: #e6e9df;
    }
    .stApp {
        color: var(--ink);
        background-color: var(--paper);
        background-image: radial-gradient(#dce8d9 0.75px, transparent 0.75px);
        background-size: 19px 19px;
    }
    [data-testid="stHeader"] { background: transparent; }
    .block-container { max-width: 1120px; padding-top: 1.5rem; padding-bottom: 3rem; }
    h1, h2, h3, p, label { font-family: 'Gowun Dodum', sans-serif; letter-spacing: 0; }
    .hero {
        position: relative;
        overflow: hidden;
        padding: 1.6rem 1.9rem 1.45rem;
        margin: 0.25rem 0 1.4rem;
        border: 1px solid #e6eadf;
        border-radius: 8px;
        background: linear-gradient(105deg, #e8f1df 0%, #fff8df 55%, #f9e3df 100%);
    }
    .hero:after {
        content: '✿';
        position: absolute;
        right: 3.2rem;
        top: -1.6rem;
        color: #ffffffa8;
        font-size: 8rem;
        transform: rotate(16deg);
    }
    .hero-kicker { color: #58765b; font-size: 0.8rem; font-weight: 700; }
    .hero-title {
        margin: 0.25rem 0 0;
        color: var(--ink);
        font-family: 'Jua', sans-serif;
        font-size: 2.35rem;
    }
    .hero-note { margin: 0.35rem 0 0; color: #586e64; font-size: 0.98rem; }
    .hero-stamp {
        position: absolute;
        z-index: 1;
        right: 1.4rem;
        bottom: 1.25rem;
        padding: 0.45rem 0.8rem;
        border: 1px solid #ffffff;
        border-radius: 99px;
        background: #ffffffb8;
        color: #58765b;
        font-size: 0.8rem;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-color: var(--line);
        border-radius: 8px;
        background: #ffffffd9;
    }
    .portrait-placeholder {
        display: grid;
        position: relative;
        min-height: 158px;
        place-items: center;
        overflow: hidden;
        border-radius: 6px;
        background: radial-gradient(circle at 50% 45%, #fff 0 27%, var(--accent) 28% 100%);
    }
    .portrait-placeholder:before, .portrait-placeholder:after {
        content: '✦';
        position: absolute;
        color: #ffffffd9;
        font-size: 1.2rem;
    }
    .portrait-placeholder:before { top: 1rem; left: 1.15rem; }
    .portrait-placeholder:after { right: 1.25rem; bottom: 1rem; font-size: 0.9rem; }
    .portrait-mark {
        color: #41564b;
        font-family: 'Jua', sans-serif;
        font-size: 3.5rem;
        line-height: 1;
    }
    .portrait-caption { position: absolute; bottom: 0.7rem; color: #52665a; font-size: 0.72rem; }
    .character-name { margin: 0.7rem 0 0.05rem; font-family: 'Jua', sans-serif; font-size: 1.45rem; }
    .character-group { color: var(--muted); font-size: 0.8rem; }
    .profile-line {
        display: flex;
        justify-content: space-between;
        gap: 0.8rem;
        padding: 0.45rem 0;
        border-bottom: 1px dashed #e8ebe4;
        font-size: 0.86rem;
    }
    .profile-line:last-child { border-bottom: 0; }
    .profile-label { color: #697970; }
    .profile-value { color: #a0aaa3; text-align: right; }
    .rank-row {
        display: flex;
        align-items: center;
        gap: 0.9rem;
        padding: 0.3rem 0;
    }
    .rank-number {
        display: grid;
        width: 2.25rem;
        height: 2.25rem;
        flex: 0 0 2.25rem;
        place-items: center;
        border-radius: 50%;
        background: #eef4e9;
        color: #628263;
        font-family: 'Jua', sans-serif;
    }
    .rank-name { color: var(--ink); font-family: 'Jua', sans-serif; font-size: 1.05rem; }
    .rank-status { margin-left: auto; color: #99a59c; font-size: 0.82rem; }
    div[data-testid="stFileUploader"] section { padding: 0.65rem; }
    div[data-testid="stTabs"] button { font-family: 'Jua', sans-serif; font-size: 1rem; }
    @media (max-width: 640px) {
        .hero { padding: 1.25rem; }
        .hero-title { font-size: 1.9rem; }
        .hero-stamp { position: static; display: inline-block; margin-top: 0.8rem; }
        .hero:after { right: 0.5rem; top: -1.2rem; font-size: 6rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <header class="hero">
        <div class="hero-kicker">CHIikawa · CHARACTER FILE</div>
        <div class="hero-title">먼작귀 친구들 도감</div>
        <div class="hero-note">작고 소중한 친구들을 한 페이지에 모아보기</div>
        <div class="hero-stamp">오늘도 귀여움 충전 🍀</div>
    </header>
    """,
    unsafe_allow_html=True,
)

catalog_tab, ranking_tab = st.tabs(["캐릭터 도감", "인기 순위"])

with catalog_tab:
    search_column, group_column = st.columns([1.5, 1])
    with search_column:
        search_text = st.text_input("캐릭터 찾기", placeholder="이름으로 검색")
    with group_column:
        selected_group = st.selectbox("친구 구분", ["전체", "주요 친구", "친구들"])

    visible_characters = [
        character
        for character in CHARACTERS
        if search_text.strip() in character["name"]
        and (selected_group == "전체" or character["group"] == selected_group)
    ]

    if not visible_characters:
        st.info("검색 결과가 없어요.")
    else:
        character_columns = st.columns(3)
        for character_index, character in enumerate(visible_characters):
            with character_columns[character_index % len(character_columns)]:
                with st.container(border=True):
                    with st.expander("이미지 추가"):
                        character_image = st.file_uploader(
                            "이미지 파일",
                            type=["png", "jpg", "jpeg", "webp"],
                            key=f"image_{character['name']}",
                        )
                    if character_image is not None:
                        st.image(character_image, use_container_width=True)
                    else:
                        st.markdown(
                            f"""
                            <div class="portrait-placeholder" style="--accent:{character['color']}">
                                <span class="portrait-mark">{escape(character['symbol'])}</span>
                                <span class="portrait-caption">PROFILE IMAGE</span>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                    st.markdown(
                        f"""
                        <div class="character-name">{escape(character['name'])}</div>
                        <div class="character-group">{escape(character['group'])}</div>
                        """,
                        unsafe_allow_html=True,
                    )
                    for field_name in ["MBTI", "외모 특징", "말투", "대표 성격", "인기 순위"]:
                        st.markdown(
                            f"<div class='profile-line'><span class='profile-label'>{field_name}</span>"
                            "<span class='profile-value'>추후 입력</span></div>",
                            unsafe_allow_html=True,
                        )

with ranking_tab:
    st.subheader("친구 인기 순위")
    st.caption("순위는 나중에 직접 채울 수 있도록 비워 두었어요.")
    rank_columns = st.columns(2)
    for character_index, character in enumerate(CHARACTERS):
        with rank_columns[character_index % len(rank_columns)]:
            with st.container(border=True):
                st.markdown(
                    f"""
                    <div class="rank-row">
                        <span class="rank-number">?</span>
                        <span class="rank-name">{escape(character['name'])}</span>
                        <span class="rank-status">순위 입력 예정</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
