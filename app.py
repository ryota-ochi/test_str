import hmac
import streamlit as st
import pandas as pd


def check_password():
    def login_form():
        with st.form("Credentials"):
            st.text_input("ユーザ", key="username")
            st.text_input("パスワード", type="password", key="password")
            st.form_submit_button("ログイン", on_click=password_entered)

    def password_entered():
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    login_form()
    if "password_correct" in st.session_state:
        st.error("ユーザ名もしくはパスワードが間違っています。")
    return False


if not check_password():
    st.stop()


display_array = [
    {"name": "田中太郎", "sex": "男", "age": 20, "point": 5},
    {"name": "山田太郎", "sex": "男", "age": 20, "point": 5},
    {"name": "鈴木花子", "sex": "女", "age": 25, "point": 7},
    {"name": "佐藤次郎", "sex": "男", "age": 22, "point": 4},
]


def filter_by_sex(display_array, sex):
    filtered_list = [person for person in display_array if person["sex"] == sex]
    return filtered_list

def main():
    st.title('一覧絞り込み機能')
    sex_filter = st.selectbox("性別を選んでください",  options=["選択してください", "男", "女"], index=0)
 

    filtered_array = filter_by_sex(display_array, sex_filter)
    if len(filtered_array) > 0:
        df = pd.DataFrame(filtered_array)
        df
    else:
        df = pd.DataFrame(display_array)
        df

if __name__ == "__main__":
    main()