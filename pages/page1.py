import streamlit as st
st.title("ユーザー情報ページ")
if'user_name'in st.session_state and st.session_state.user_name:
    st.success(f"こんにちは{st.session_state.user_name}さん!")
    st.write("メインページで入力された名前が表示しています。")
    st.balloons()
else:
    st.error("ユーザー名が設定されていません")
    st.write("メインページで名前を入力してください。")