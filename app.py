import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Universal Data Visualizer", layout="wide")

st.title("📊 Universal Data Visualization Dashboard")
st.write("Upload any CSV file and create interactive visualizations automatically.")

data_source = st.radio(
    "Select Data Source:",
    ["Upload CSV File", "Load from URL"],
    horizontal=True
)

uploaded_file = None
url_input = None

if data_source == "Upload CSV File":
    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )
else:
    url_input = st.text_input(
        "Enter CSV URL",
        placeholder="https://example.com/data.csv"
    )

@st.cache_data
def load_data(source):
    try:
        df = pd.read_csv(source)

        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col])
            except:
                try:
                    df[col] = pd.to_datetime(df[col])
                except:
                    pass

        return df

    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

source = uploaded_file if data_source == "Upload CSV File" else (
    url_input if url_input else None
)

if source:

    df = load_data(source)

    if not df.empty:

        st.success("✅ Data Loaded Successfully")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Missing Values", int(df.isnull().sum().sum()))

        if st.checkbox("View Dataset"):
            st.dataframe(df, use_container_width=True)

        if st.checkbox("View Statistical Summary"):
            st.write(df.describe(include='all'))

        numeric_cols = df.select_dtypes(include='number').columns.tolist()

        st.sidebar.header("Visualization Settings")

        chart_type = st.sidebar.selectbox(
            "Select Chart Type",
            [
                "Line Chart",
                "Bar Chart",
                "Scatter Plot",
                "Histogram",
                "Box Plot",
                "Pie Chart"
            ]
        )

        if chart_type == "Line Chart":

            x = st.sidebar.selectbox("X Axis", df.columns)

            if len(numeric_cols) == 0:
                st.warning("No numeric columns available.")
            else:
                y = st.sidebar.selectbox("Y Axis", numeric_cols)

                color = st.sidebar.selectbox(
                    "Color",
                    ["None"] + list(df.columns)
                )

                fig = px.line(
                    df,
                    x=x,
                    y=y,
                    color=None if color == "None" else color,
                    title=f"{y} vs {x}"
                )

                st.plotly_chart(fig, use_container_width=True)

        elif chart_type == "Bar Chart":

            if len(numeric_cols) == 0:
                st.warning("No numeric columns available.")
            else:
                x = st.sidebar.selectbox("Category", df.columns)
                y = st.sidebar.selectbox("Value", numeric_cols)

                fig = px.bar(
                    df,
                    x=x,
                    y=y,
                    title=f"{y} by {x}"
                )

                st.plotly_chart(fig, use_container_width=True)

        elif chart_type == "Scatter Plot":

            if len(numeric_cols) < 2:
                st.warning("Scatter Plot requires at least two numeric columns.")
            else:
                x = st.sidebar.selectbox("X Axis", numeric_cols)
                y = st.sidebar.selectbox(
                    "Y Axis",
                    numeric_cols,
                    index=1
                )

                color = st.sidebar.selectbox(
                    "Color",
                    ["None"] + list(df.columns)
                )

                fig = px.scatter(
                    df,
                    x=x,
                    y=y,
                    color=None if color == "None" else color,
                    title=f"{x} vs {y}"
                )

                st.plotly_chart(fig, use_container_width=True)

        elif chart_type == "Histogram":

            if len(numeric_cols) == 0:
                st.warning("Histogram requires at least one numeric column.")
            else:
                x = st.sidebar.selectbox(
                    "Column",
                    numeric_cols
                )

                fig = px.histogram(
                    df,
                    x=x,
                    title=f"Distribution of {x}"
                )

                st.plotly_chart(fig, use_container_width=True)

        elif chart_type == "Box Plot":

            if len(numeric_cols) == 0:
                st.warning("Box Plot requires at least one numeric column.")
            else:
                y = st.sidebar.selectbox(
                    "Numeric Column",
                    numeric_cols
                )

                x = st.sidebar.selectbox(
                    "Category",
                    ["None"] + list(df.columns)
                )

                fig = px.box(
                    df,
                    x=None if x == "None" else x,
                    y=y,
                    title=f"Box Plot of {y}"
                )

                st.plotly_chart(fig, use_container_width=True)

        elif chart_type == "Pie Chart":

            if len(numeric_cols) == 0:
                st.warning("Pie Chart requires at least one numeric column.")
            else:
                names = st.sidebar.selectbox(
                    "Category",
                    df.columns
                )

                values = st.sidebar.selectbox(
                    "Values",
                    numeric_cols
                )

                fig = px.pie(
                    df,
                    names=names,
                    values=values,
                    title=f"{values} by {names}"
                )

                st.plotly_chart(fig, use_container_width=True)

        if len(numeric_cols) > 1:

            st.subheader("Correlation Heatmap")

            corr = df[numeric_cols].corr()

            fig = px.imshow(
                corr,
                text_auto=True,
                aspect="auto"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    else:
        st.error("Dataset could not be loaded.")

else:
    st.info("👆 Upload a CSV file or provide a URL to begin.")