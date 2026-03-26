import streamlit as st
import pandas as pd

# Load data
data = pd.read_csv('data/superstore_sales.csv')

# Sidebar navigation
st.sidebar.title('Superstore Sales App')
pages = [
    '01_Overview',
    '02_Sales_Analysis',
    '03_Profit_Analysis',
    '04_Customer_Segments',
    '05_Product_Categories',
    '06_Regional_Performance',
    '07_Shipping_Analysis',
    '08_Discount_Impact',
    '09_Top_Products',
    '10_Data_Download'
]
page = st.sidebar.radio('Go to', pages)

# Page loader
def load_page(page):
    if page == '01_Overview':
        import pages.01_Overview as pg
    elif page == '02_Sales_Analysis':
        import pages.02_Sales_Analysis as pg
    elif page == '03_Profit_Analysis':
        import pages.03_Profit_Analysis as pg
    elif page == '04_Customer_Segments':
        import pages.04_Customer_Segments as pg
    elif page == '05_Product_Categories':
        import pages.05_Product_Categories as pg
    elif page == '06_Regional_Performance':
        import pages.06_Regional_Performance as pg
    elif page == '07_Shipping_Analysis':
        import pages.07_Shipping_Analysis as pg
    elif page == '08_Discount_Impact':
        import pages.08_Discount_Impact as pg
    elif page == '09_Top_Products':
        import pages.09_Top_Products as pg
    elif page == '10_Data_Download':
        import pages.10_Data_Download as pg
    else:
        st.write('Page not found.')
    pg.app(data)

load_page(page)
    
    This dashboard provides deep insights into:
    - 📈 Sales trends and patterns
    - 🌍 Regional performance metrics
    - 📦 Product analysis
    - 👥 Customer insights
    - 💰 Profitability analysis
    - 📅 Time series forecasts
    - 🔄 Year-over-year comparisons
    - 🔍 Raw data exploration
    
    **Navigate using the sidebar pages to explore different analyses.**
""")

st.info("💡 Tip: Use the filters and dropdowns on each page to customize your analysis!")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Pages", "10", "📄")
with col2:
    st.metric("Data Updates", "Real-time", "⚡")
with col3:
    st.metric("Regions Covered", "4", "🗺️")
