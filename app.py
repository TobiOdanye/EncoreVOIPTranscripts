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

    # Step 4: User prompt input BEFORE summary generation
    user_prompt = st.text_area("✏️ Enter a prompt to guide the summary generation", "")

    # Step 5: Simulate summary generation
    if st.button("🔍 Generate Summary"):
        # Simulate GPT summary creation
        summary = f"Simulated summary using '{template}' template and prompt: {user_prompt}"
        
        # Save to session_state for memory and refinement
        st.session_state["summary"] = summary
        st.session_state["prompt"] = user_prompt
        st.session_state["template"] = template
        st.session_state["history"] = f"Prompt: {user_prompt}\nSummary: {summary}"

        st.success("✅ Summary generated!")

    # Step 6: Show and edit the summary
    if "summary" in st.session_state:
        st.subheader("📝 Editable Summary")
        edited_summary = st.text_area("Edit the summary below if needed:", st.session_state["summary"], height=300)

        # Save the edited version
        st.session_state["summary"] = edited_summary

        # Step 7: Option to refine further
        st.subheader("🔁 Refine Summary")
        refine_prompt = st.text_area("Refine the summary further (based on above)?", "")

        if st.button("↩️ Re-generate with refinement") and refine_prompt:
            previous = st.session_state["summary"]
            refined_summary = f"Refined summary using: {refine_prompt}\n\nPrevious Summary:\n{previous}"
            st.session_state["summary"] = refined_summary
            st.session_state["history"] += f"\n\nRefine Prompt: {refine_prompt}\nRefined Summary: {refined_summary}"
            st.success("✅ Refined summary generated!")

        # Step 8: Tag selector
        tags = st.multiselect("🏷️ Select tags", [
            "Candidate Introduction Bio", "News", "LinkedIn Message", 
            "Text/ WhatsApp", "People Moves", "Reference/ Griff", "Comp & Revenue", 
            "Search Update", "CV Punt In", "Business Development (BD)", "Internal", 
            "Meeting", "Phone Call / VC", "Interview Feedback"
        ])

        # Step 9: Push to CRM simulation
        if st.button("📤 Push to CRM"):
            st.success(f"✅ Pushed summary to CRM with tags: {', '.join(tags)}")
            st.info("📌 Remember to add context in the Ezekia note. I.e. Tag the relevant people/companies.")

