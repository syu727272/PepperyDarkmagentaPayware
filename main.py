
import streamlit as st
import pandas as pd
import numpy as np

# Set page title and configuration
st.set_page_config(
    page_title="Streamlit デモ",
    page_icon="📊",
    layout="wide"
)

# Main title
st.title("Streamlit デモアプリケーション")

# Sidebar
with st.sidebar:
    st.header("設定")
    user_name = st.text_input("あなたの名前", "ゲスト")
    color = st.color_picker("好きな色を選んでください", "#00f900")
    
    st.markdown("---")
    st.markdown("## Streamlitについて")
    st.markdown("Streamlitは、データアプリケーションを簡単に作成できるPythonライブラリです。")
    st.markdown("[Streamlit公式ドキュメント](https://docs.streamlit.io/)")

# Main content
st.header(f"こんにちは、{user_name}さん！")

# Create tabs
tab1, tab2, tab3 = st.tabs(["📈 データ表示", "🗃️ テーブル", "🧮 インタラクティブ要素"])

with tab1:
    st.subheader("チャートの例")
    
    # Generate sample data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C'])
    
    st.line_chart(chart_data)
    
    st.markdown(f"あなたが選んだ色: <span style='color:{color}'>■■■</span>", unsafe_allow_html=True)

with tab2:
    st.subheader("データテーブルの例")
    
    # Create a sample dataframe
    df = pd.DataFrame({
        '日付': pd.date_range(start='2023-01-01', periods=5),
        '売上': [100, 120, 90, 150, 180],
        '費用': [80, 85, 75, 95, 100],
        '利益': [20, 35, 15, 55, 80]
    })
    
    st.dataframe(df, use_container_width=True)
    
    # Calculate stats
    total_profit = df['利益'].sum()
    st.metric("合計利益", f"¥{total_profit}")

with tab3:
    st.subheader("インタラクティブ要素")
    
    # Slider
    slider_val = st.slider("値を選んでください", 0, 100, 50)
    st.write(f"選択された値: {slider_val}")
    
    # Checkbox
    if st.checkbox("詳細を表示"):
        st.write("これは詳細情報です！")
        
    # Selectbox
    option = st.selectbox(
        'お気に入りのプログラミング言語は？',
        ['Python', 'JavaScript', 'Java', 'C++', 'その他'])
    st.write(f'あなたは {option} を選びました！')

# Footer
st.markdown("---")
st.caption("Streamlit on Replit - デモアプリケーション")
