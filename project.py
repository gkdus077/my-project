import streamlit as st
pages = {
    "회원" : [
        st.Page("./page/a.py", title="공지사항📣"),
        st.Page("./page/b.py", title="회원가입"),
        st.Page("./page/c.py", title="로그인")
    ],
    "카테고리2" : [
        st.Page("./page/d.py", title="신청방"),
        st.Page("./page/e.py", title="playlist")
    ]
}
pg = st.navigation(pages)
pg.run()


