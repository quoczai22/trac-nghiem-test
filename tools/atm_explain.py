"""Explanations for the ATM bank, merged by convert_atm_bank.py.

EXPLAIN maps a question id to (why the answer is right, {wrong letter: why it is wrong}).
Letters are the final ones in subjects/an-toan-mang/questions.js; the converter checks
that every note sits on a wrong option, so a reshuffled question fails loudly.
"""

from atm_explain_c1 import EXPLAIN as C1
from atm_explain_c2 import EXPLAIN as C2
from atm_explain_c3 import EXPLAIN as C3
from atm_explain_c4 import EXPLAIN as C4
from atm_explain_c5 import EXPLAIN as C5
from atm_explain_c6 import EXPLAIN as C6

EXPLAIN = {**C1, **C2, **C3, **C4, **C5, **C6}
