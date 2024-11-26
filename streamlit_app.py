import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and description
st.title("Real Estate Market Adjustment Tool")
st.markdown(
    "This app helps with market adjustment analysis for real estate appraising. "
    "Upload your property data to calculate adjustments and visualize trends."
)

# File upload section
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    # Load the uploaded Excel file
    try:
        data = pd.read_excel(uploaded_file)
        st.write("Preview of the uploaded data:")
        st.dataframe(data.head())

        # Perform calculations (example: calculating New Adjusted Price if not already provided)
        if "Months Passed" in data.columns and "MKT ADJ %" in data.columns:
            data["New ADJ Price"] = data["Orginal Cost"] * (1 + (data["MKT ADJ %"] / 100))
            st.write("Updated Data with Adjusted Prices:")
            st.dataframe(data)

        # Visualization: % Change over Months Passed
        if "Months Passed" in data.columns and "% Change" in data.columns:
            st.subheader("Trend Analysis")
            fig, ax = plt.subplots()
            ax.plot(data["Months Passed"], data["% Change"], marker='o', linestyle='-', label='% Change')
            ax.set_xlabel("Months Passed")
            ax.set_ylabel("% Change")
            ax.set_title("Percentage Change Over Time")
            ax.legend()
            st.pyplot(fig)

        # Download updated data
        st.subheader("Export Updated Data")
        st.download_button(
            label="Download Updated Excel File",
            data=data.to_excel(index=False, engine="openpyxl"),
            file_name="Updated_Market_Adjustments.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error(f"Error processing the file: {e}")

else:
    st.info("Please upload an Excel file to proceed.")
