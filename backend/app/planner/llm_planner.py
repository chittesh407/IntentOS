import json

from app.llm.provider import generate
from app.planner.prompt import PLANNER_PROMPT


class LLMPlanner:

    def plan(self, user_input: str):

        response = generate([
            {
                "role": "system",
                "content": PLANNER_PROMPT
            },
            {
                "role": "user",
                "content": user_input
            }
        ])

        return json.loads(response)