import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Upload Files", page_icon="⬆️")
menu = st.sidebar.selectbox("Choose an option:", ["Upload CSV and edit", "Upload Image", "Upload Video", "Upload Audio"])

class UploadHandler:
    """
        A class to handle various file upload operations in a Streamlit application.
        
        This class provides methods for handling different types of file uploads including:
        - CSV files with data analysis capabilities
        - Image files
        - Video files
        - Audio files

        Attributes:
            None

        Methods:
            uploadEditCSV(): Handles CSV file uploads and provides data analysis capabilities.
            uploadImage(): Allows users to upload and display image files in JPG, JPEG, or PNG format.
            uploadVideo(): Allows users to upload and play video files from YouTube links.
            uploadAudio(): Allows users to upload and play audio files from MP3 or WAV format.

        Usage:
            upload_handler = UploadHandler()
            upload_handler.uploadEditCSV()
            upload_handler.uploadImage()
            upload_handler.uploadVideo()
            upload_handler.uploadAudio()

        Note:
            This class assumes that the necessary libraries (e.g., pandas, plotly) are imported and available.
        """
    
    def __init__(self) -> None:
        pass

    def uploadEditCSV(self) -> None:
        """
        Allows users to upload and analyze CSV files with interactive visualizations.
            
            This function provides a streamlit interface for:
            - Uploading CSV files
            - Viewing the data in a table format
            - Selecting specific columns for analysis
            - Performing statistical operations (Average, Sum, Count)
            - Visualizing results using Bar or Pie charts
            
            Returns:
                None
        """
        uploaded_file = st.file_uploader("Upload CSV File:", type="csv")

        if not uploaded_file:
            st.warning("Please upload a CSV file.")
            return

        # Read and display CSV
        df = pd.read_csv(uploaded_file)
        with st.expander("View Uploaded File"):
            st.table(df)
        
        # Select columns and operations
        available_columns = df.columns
        selected_columns = st.multiselect("Choose columns to analyze", available_columns)

        col1, col2 = st.columns(2)
        with col1:
            chart_type = st.radio("Select Chart Type", ["Bar Chart", "Pie Chart"], horizontal=True)
        with col2:
            operation = st.radio("Select Statistical Operation", ["Average", "Sum", "Count"], horizontal=True)

        # Perform operations and plot charts
        if selected_columns:
            results_df = self._perform_operation(df, selected_columns, operation)

            if results_df is None:
                return # Exit if no valid data

            # Display results
            st.write(f"Results for {operation} operation:")
            st.table(results_df)

            # Plot charts
            if chart_type == "Bar Chart":
                self._plot_bar_chart(results_df)
            elif chart_type == "Pie Chart":
                self._plot_pie_chart(results_df)
        else:
            st.info("Please select at least one column.")

    def _perform_operation(self, df, columns, operation):
        """Performs the selected statistical operation on the chosen columns."""
        try:
            if operation == "Average":
                result = df[columns].mean().reset_index(name="Value")
            elif operation == "Sum":
                result = df[columns].sum().reset_index(name="Value")
            elif operation == "Count":
                result = df[columns].count().reset_index(name="Value")
            else:
                raise ValueError("Invalid operation selected.")
        except TypeError:
            st.error("Invalid data type for the selected columns.")
            return None
        result.rename(columns={"index": "Column"}, inplace=True)
        return result

    def _plot_bar_chart(self, results_df):
        """Plots a bar chart using the results DataFrame."""
        fig = px.bar(results_df, x="Column", y="Value", title="Bar Chart", labels={"Value": "Value"})
        st.plotly_chart(fig)

    def _plot_pie_chart(self, results_df):
        """Plots a pie chart using the results DataFrame."""
        fig = px.pie(results_df, names="Column", values="Value", title="Pie Chart")
        st.plotly_chart(fig)

    def uploadImage(self) -> None:
        """Allows users to upload and display image files in JPG, JPEG, or PNG format.
            The uploaded image will be displayed using the full column width."""
        
        uploadimage = st.file_uploader("Upload Image File:", type=["jpg", "jpeg", "png"])

        if uploadimage:
            st.image(uploadimage,use_column_width=True)

    def uploadVideo(self) -> None:
        """Allows users to upload and play video files from YouTube links.
            The video will be displayed in the Streamlit app if the link is valid."""

        st.subheader("Upload Youtube Video Link")
        youtubelink = st.text_input("Paste Youtube Video Link")
        if st.button("Play Youtube Video"):
            if youtubelink:
                try:
                    st.video(youtubelink)
                except Exception:
                    st.error("Sorry cannot play this video link")

    def uploadAudio(self) -> None:
        """Allows users to upload and play audio files from MP3 or WAV format.
            The audio will be displayed in the Streamlit app if the file is valid."""

        uploadaudio = st.file_uploader("Upload Audio File:", type=["mp3", "wav"])

        if uploadaudio:
            with st.expander("View File"):
                st.audio(uploadaudio,format='audio/mp3')

upload_handler = UploadHandler()

match menu:
    case "Upload CSV and edit":
        upload_handler.uploadEditCSV()

    case "Upload Image":
        upload_handler.uploadImage()

    case "Upload Video":
        upload_handler.uploadVideo()

    case "Upload Audio":
        upload_handler.uploadAudio()