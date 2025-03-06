import streamlit as st

# Set Page Configuration
st.set_page_config(page_title="Registration App", page_icon="🚀", layout="centered")

# Custom Background Color (Using Streamlit CSS Injection)
st.markdown(
    """
    <style>
        /* Lighter Gradient Background */
        .stApp {
            background: linear-gradient(to right, #6a85b6, #bac8e0);
            color: black;
        }

        /* Text Input Styling */
        .stTextInput>div>div>input {
            background-color: #ffffff;
            color: black;
            padding: 10px;
            border-radius: 5px;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 5px;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def register():
    st.title("🚀 Python Registration App 🚀")
    st.markdown("### Enter your details below")

    # Input Fields
    name = st.text_input("👤 Name", placeholder="Enter your name")
    email = st.text_input("📧 Email", placeholder="Enter your email")
    password = st.text_input("🔑 Password", placeholder="Enter your password", type="password")
    confirm_password = st.text_input("🔒 Confirm Password", placeholder="Re-enter your password", type="password")

    # Register Button
    if st.button("✅ Register"):
        if not name or not email or not password or not confirm_password:
            st.warning("⚠️ Please fill in all fields!")
        elif password != confirm_password:
            st.error("❌ Passwords do not match!")
        else:
            filename = f"{name}.txt"
            with open(filename, 'w') as file:
                file.write(f'Name: {name}\n')
                file.write(f'Email: {email}\n')
                file.write(f'Password: {password}\n')
            st.success(f"✅ Registration Successful!\n\nName: {name}\nEmail: {email}")

            # Provide download link for the saved file
            with open(filename, "rb") as file:
                st.download_button(label="📥 Download Registration File", data=file, file_name=filename, mime="text/plain")

if __name__ == "__main__":
    register()
