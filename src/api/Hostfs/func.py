from __future__ import annotations
from typing import Dict as D, Tuple as T
from shs.request import Request as R
from shs.response import Response as P, bad_request as B

def _(o, v): return {"user_id": "Hostfs", "operation": o, "a": v[0], "b": v[1], "result": v[2]}
def __r(q):
    try: return (int(q.query["a"]), int(q.query["b"]))
    except: return B("error")

add = lambda r, p: (x := __r(r)) and (x if isinstance(x, P) else _("add", (x[0], x[1], x[0] + x[1])))
minus = lambda r, p: (x := __r(r)) and (x if isinstance(x, P) else _("minus", (x[0], x[1], x[0] - x[1])))
multiply = lambda r, p: (x := __r(r)) and (x if isinstance(x, P) else _("multiply", (x[0], x[1], x[0] * x[1])))
divide = lambda r, p: (x := __r(r)) and (x if isinstance(x, P) else (B("b must not be 0") if x[1] == 0 else _("divide", (x[0], x[1], x[0] / x[1]))))