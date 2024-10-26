import streamlit as st
pages = {
    "회원" : [
        st.Page("a.py", title="공지사항📣"),
        st.Page("b.py", title="회원가입"),
        st.Page("c.py", title="로그인")
    ],
    "카테고리2" : [
        st.Page("d.py", title="신청방"),
        st.Page("e.py", title="playlist")
    ]
}
pg = st.navigation(pages)
pg.run()


