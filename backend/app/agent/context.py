from pydantic import BaseModel


class AgentContext(BaseModel):

    user_input: str

    intent: str = ""

    target: str = ""

    resolved_type: str = ""

    resolved_value: str = ""

    risk: str = ""

    confirmation_required: bool = False

    execution_status: str = ""

    verified: bool = False

    response: str = ""