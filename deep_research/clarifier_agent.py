import os

from agents import Agent
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv(override=True)

MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gpt-5.4-mini")


class ClarifyingQuestions(BaseModel):
    questions: list[str] = Field(
        min_length=3,
        max_length=3,
        description="Exactly three concise questions that will materially improve the research.",
    )


clarifier_agent = Agent(
    name="Research Clarifier",
    model=MODEL_NAME,
    output_type=ClarifyingQuestions,
    instructions="""
You are the clarification editor for a professional research service.
Given an initial research request, ask exactly three concise questions that
will materially improve the final answer. Focus on decisions such as scope,
audience, geography, time period, comparison criteria, desired depth, and
the intended use of the research. Do not ask questions whose answers can be
found by searching the web. If the request is already specific, ask useful
questions about priorities and output format instead. Return only the three
questions, with no introduction.
""",
)
