import streamlit as st

st.title("🔧 UI Test: Audio Summarizer Workflow")

# Step 1: File uploader
uploaded_file = st.file_uploader("📤 Upload a .wav file", type=["wav"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    # Step 2: Simulated transcript output
    st.subheader("📝 Transcript")
    fake_transcript = "This is a simulated transcript of the uploaded audio file. User can make any edits to summary here."
    st.write(fake_transcript)

    # Step 3: Template selector
    template = st.selectbox("🧩 Choose a summary template", ["Option 1", "Option 2"])

    # Step 4: Prompt input (shown only after template is selected)
    user_prompt = st.text_input("💬 Enter your prompt for summary generation")

    # Step 5: Generate summary only when prompt is filled
    if user_prompt:
        if st.button("🔍 Generate Summary"):
            st.session_state["summary"] = f"Simulated summary using '{template}' template with prompt: '{user_prompt}'."
            st.success("✅ Summary generated!")

    # Step 6: Editable summary area
    if "summary" in st.session_state:
        edited_summary = st.text_area("✏️ Editable Summary", st.session_state["summary"], height=300)

        # Step 7: Tag selector
        tags = st.multiselect("🏷️ Select tags", [
            "Candidate Introduction Bio", "News", "LinkedIn Message", 
            "Text/ WhatsApp", "People Moves", "Reference/ Griff", "Comp & Revenue", 
            "Search Update", "CV Punt In", "Business Development (BD)", "Internal", 
            "Meeting", "Phone Call / VC", "Interview Feedback"
        ])

        # Step 8: Push to CRM simulation
        if st.button("📤 Push to CRM"):
            st.success(f"✅ Pushed summary to CRM with tags: {', '.join(tags)}")
