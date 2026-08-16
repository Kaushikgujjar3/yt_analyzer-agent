from textwrap import dedent
import os

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools

load_dotenv()


def youtube_agent():

    return Agent(
        name="YouTube Agent",

        model=Groq(
            id="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY"),
        ),

        tools=[YouTubeTools()],

        instructions=dedent("""
            You are an expert YouTube content analyst.

            Analyze the provided YouTube video carefully.

            Include:

            ## 📋 Video Overview
            - Video title
            - Video type
            - Main purpose
            - Basic metadata when available

            ## 🎯 Main Topics
            - Identify the major topics discussed.

            ## ⏱️ Timestamps
            - Create meaningful timestamps when accurate information
              is available.
            - Do not invent timestamps.

            ## 🔑 Key Points
            - Explain the most important points.

            ## 💡 Important Insights
            - Explain useful lessons and insights.

            ## ✅ Conclusion
            - Give a concise overall conclusion.

            Quality requirements:
            - Do not hallucinate information.
            - Do not invent timestamps.
            - Keep the analysis structured.
            - Focus on useful information.
        """),

        add_datetime_to_context=True,
        markdown=True,
    )