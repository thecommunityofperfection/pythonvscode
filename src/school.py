import streamlit as st
import pandas as pd
from pathlib import Path, WindowsPath
from PIL import Image
import io
import os
from datetime import datetime

CSV_PATH: WindowsPath = Path("csv/school.csv")
IMAGE_FOLDER: str = "img"


class StudentRegistry:
    """
    Manages student registrations, data storage, and profile picture handling.
    Uses a CSV file for student info and saves profile pictures as PNG files.
    """

    def __init__(self, csv_file: WindowsPath = CSV_PATH) -> None:
        self.csv_file: str = str(csv_file)
        self.admin_password: str = "School12457"
        self.data_frame: pd.DataFrame = self._load_data()

    def _load_data(self) -> pd.DataFrame:
        """Load student data from CSV, or create empty DataFrame if file missing."""
        try:
            return pd.read_csv(self.csv_file)
        except FileNotFoundError:
            return pd.DataFrame()

    def save_profile_picture(self, uploaded_file: st.runtime.uploaded_file_manager.UploadedFile, student_id: str) -> None:
        """
        Save uploaded profile picture to a PNG file named by student ID.
        Converts and verifies image format using Pillow.

        Parameters:
            uploaded_file: Uploaded image file from Streamlit uploader
            student_id: Unique identifier for the student, used as filename
        """
        try:
            image = Image.open(io.BytesIO(uploaded_file.read()))
            # Convert to RGB to avoid saving issues with transparency, etc.
            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")
            image.save(
                os.path.join(IMAGE_FOLDER, f"{student_id}.png"),
                format="PNG"
            )
        except Exception as e:
            st.error(f"Failed to process image: {e}")

    def register_student(self) -> None:
        """
        Streamlit UI for registering a student and saving their data.
        """
        st.title("- Student Registration Form")
        st.divider()
        st.write("**- Student Information**")

        uploadpfp = st.file_uploader("Choose profile picture: ", type=["jpg", "png", "jpeg"])

        c1, c2 = st.columns(2)
        with c1:
            fname: str = st.text_input("First name:")
            dob = st.date_input("Date of Birth:", min_value=datetime(2000, 1, 1))
            gender: str = st.radio("Gender:", ["Male", "Female"], horizontal=True)
        with c2:
            lname: str = st.text_input("Last name:")
            nation: str = st.text_input("Nationality:")
            email: str = st.text_input("Student Email:")

        student_id = "student" + str(len(self.data_frame) + 1)

        st.divider()
        st.write("**- Parent/Guardian Information**")

        p1, p2 = st.columns(2)
        with p1:
            p_name: str = st.text_input("Parent/guardian Name:")
            p_contact: str = st.text_input("Contact information:")
        with p2:
            relation: str = st.text_input("Relationship to student:")
            emergency: str = st.text_input("Emergency contact information:")

        agreement: str = st.radio("Do you agree to the terms and conditions of enrollment?", ["Yes", "No"])

        if agreement == "Yes" and st.button("Save Student Information"):
            # Validate inputs
            if uploadpfp and fname and lname:
                student_data = {
                    "First Name": [fname],
                    "Last Name": [lname],
                    "Birthday": [dob],
                    "Nationality": [nation],
                    "Gender": [gender],
                    "Email": [email],
                    "Parent Name": [p_name],
                    "Parent Relationship": [relation],
                    "Parent Contact": [p_contact],
                    "Emergency Contact": [emergency],
                    "StudentID": [student_id],
                }
                new_df = pd.DataFrame(student_data)
                combined_df = pd.concat([self.data_frame, new_df], ignore_index=True)
                combined_df.to_csv(self.csv_file, index=False)
                self.save_profile_picture(uploadpfp, student_id)
                st.success("Saved Student Information!")
                # Reload data after save
                self.data_frame = combined_df
            else:
                st.error("Upload student picture first & fill all details!")

    def view_student_info(self) -> None:
        """
        Streamlit UI for viewing student info after admin authentication.
        """
        student_user: str = st.sidebar.text_input("Input student ID: ").lower()
        admin: str = st.sidebar.text_input("Enter admin password: ", type="password")

        st.sidebar.write("**Made by Sam**")

        if st.sidebar.button("View student info"):
            if admin == self.admin_password:
                filtered = self.data_frame[self.data_frame["StudentID"] == student_user]
                if filtered.empty:
                    st.error("Student ID not found.")
                    return
                # Extract info safely with iloc[0]
                student_info = filtered.iloc[0]
                student_img_path = os.path.join(IMAGE_FOLDER, f"{student_user}.png")

                l1, l2 = st.columns(2)
                with l1:
                    st.title(f":red[{student_info['First Name']} {student_info['Last Name']}]")
                with l2:
                    if Path(student_img_path).exists():
                        st.image(student_img_path)
                    else:
                        st.warning("Profile picture not found.")
                
                st.divider()

                side1, side2 = st.columns(2)
                with side1:
                    with st.container():
                        st.subheader("Student Info")
                        st.write("User ID:", student_info["StudentID"])
                        st.write("Gender:", student_info["Gender"])
                        st.write("Birth Date:", student_info["Birthday"])
                        st.write("Email:", student_info["Email"])
                with side2:
                    with st.container():
                        st.subheader("Parent Info")
                        st.write("Parent/Guardian:", student_info["Parent Name"])
                        st.write("Parent Contact:", int(student_info["Parent Contact"]))
                        st.write("Relationship:", student_info["Parent Relationship"])
                        st.write("Emergency Contact:", student_info["Emergency Contact"])
            else:
                st.sidebar.error("Incorrect Password")

    def run(self) -> None:
        """
        Run the Streamlit app, switching between registration and viewing modes.
        """
        menu = st.sidebar.selectbox("Menu", ["Registration", "View Student Info"])
        if menu == "Registration":
            self.register_student()
        elif menu == "View Student Info":
            self.view_student_info()


if __name__ == "__main__":
    registry = StudentRegistry()
    registry.run()
