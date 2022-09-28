from nis import match
from pydantic import BaseModel
from typing import Union

class RuleInput(BaseModel):
    input1: Union[str, None] = None
    input2: Union[str, None] = None

def parse_input1(input: RuleInput):
    if input.input1 is None: return "00"
    match input.input1.upper():
        case "A": return "01"
        case "B": return "10"
        case _: return "00"

def parse_input2(input: RuleInput):
    if input.input2 is None: return "00"
    match input.input2.upper():
        case "A": return "01"
        case "B": return "10"
        case _: return "00"

def parse_rule_input(input: RuleInput):
    input1 = parse_input1(input)
    input2 = parse_input2(input)
    return input2 + input1
