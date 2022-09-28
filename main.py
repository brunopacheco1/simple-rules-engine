from typing import Union
from qiskit import *
from fastapi import FastAPI
from engine import hit_rules
from input import RuleInput

app = FastAPI()

@app.post("/engine")
def read_rule_output(input: RuleInput):
    return hit_rules(input)
