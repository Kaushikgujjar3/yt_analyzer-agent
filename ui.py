import streamlit as st
from youtube_analyzer import youtube_agent


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="YouTube AI Analyzer",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="expanded",
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🎥 YouTube AI")

    st.divider()

    st.subheader("🤖 About")

    st.write(
        """
        Analyze any YouTube video using AI and get:

        • Video summary  
        • Main topics  
        • Key points  
        • Important insights  
        • Conclusion
        """
    )

    st.divider()

    st.subheader("⚡ How it works")

    st.info(
        """
        **1.** Paste YouTube URL

        **2.** Click Analyze Video

        **3.** Wait for AI analysis

        **4.** Read your report
        """
    )

    st.divider()

    st.subheader("✨ Features")

    st.write("🧠 AI Video Analysis")
    st.write("📝 Smart Summary")
    st.write("🎯 Key Points")
    st.write("💡 Insights")
    st.write("⚡ Fast Results")


# ============================================================
# AGENT
# ============================================================

@st.cache_resource
def get_agent():
    return youtube_agent()


agent = get_agent()


# ============================================================
# HEADER
# ============================================================

st.title("🎥 YouTube AI Analyzer")

st.subheader(
    "Turn any YouTube video into an intelligent AI report."
)

st.write(
    "Paste a YouTube video link below and let AI analyze "
    "the video's content."
)

st.divider()


# ============================================================
# URL INPUT
# ============================================================

video_url = st.text_input(
    "🔗 YouTube Video Link",
    placeholder="https://www.youtube.com/watch?v=...",
)


# ============================================================
# ANALYZE BUTTON
# ============================================================

button = st.button(
    "🚀 Analyze Video",
    use_container_width=True,
)





# ============================================================
# ANALYSIS
# ============================================================

if button:

    if not video_url.strip():

        st.warning(
            "⚠️ Please paste a YouTube video link first."
        )

    else:

        st.divider()

        st.subheader("🧠 AI Analysis Report")

        with st.spinner(
            "🔍 AI is analyzing your YouTube video..."
        ):

            try:

                response = agent.run(
                    f"""
                    Analyze this YouTube video:

                    {video_url}

                    Provide a clear and structured analysis.

                    Include:

                    ## 📋 Video Summary

                    ## 🎯 Main Topics

                    ## 🔑 Key Points

                    ## 💡 Important Insights

                    ## ✅ Conclusion
                    """
                )

                st.success(
                    "✅ Video analysis completed!"
                )

                st.markdown(
                    response.content
                )

                st.divider()

                st.download_button(
                    label="📥 Download Analysis",
                    data=response.content,
                    file_name="youtube_analysis.txt",
                    mime="text/plain",
                    use_container_width=True,
                )

            except Exception as e:

                st.error(
                    f"❌ Error while analyzing video: {e}"
                )
                
                
                # ============================================================
# QUICK FEATURES
# ============================================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🧠 Analysis",
        value="AI",
    )

with col2:
    st.metric(
        label="📝 Summary",
        value="Smart",
    )

with col3:
    st.metric(
        label="💡 Insights",
        value="AI",
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🎥 YouTube AI Analyzer • Built with Streamlit + AI"
)