from app.planner.llm_planner import LLMPlanner

planner = LLMPlanner()

while True:

    text = input("You: ")

    result = planner.plan(text)

    print(result)