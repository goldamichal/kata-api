from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

UNIT_COST = 4.5


class RequestBody(BaseModel):
    name: str
    unit: str
    value: float


class ResponseBody(RequestBody):
    unit_cost: float
    total_cost: float


@app.post("/", response_model=ResponseBody)
def post(body: RequestBody):
    total_cost = body.value * UNIT_COST

    return ResponseBody(
        name=body.name,
        unit=body.unit,
        value=body.value,
        unit_cost=UNIT_COST,
        total_cost=total_cost,
    )
