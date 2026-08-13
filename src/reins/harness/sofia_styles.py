TRUE_RED = "#ff4040"
BRIGHT_RED = "#ff1100"
BLOOD_BLACK = "#200000"
DIM_GRAY = "#5c5855"

CSS = f"""
SofiaDashboard {{
    background: transparent;
}}
.panel {{
    border: ascii {TRUE_RED};
    background: transparent;
    padding: 1;
    margin: 1;
}}
.panel-title {{
    text-style: bold;
    color: {TRUE_RED};
    margin-bottom: 1;
}}
.metric-label {{
    color: {TRUE_RED};
    width: 15;
}}
.budget-label {{
    color: {TRUE_RED};
    width: 9;
}}
.budget-input {{
    width: 14;
}}
Horizontal {{
    height: auto;
}}
.status-active {{
    color: {TRUE_RED};
    text-style: bold;
    width: 30;
}}
.status-inactive {{
    color: {DIM_GRAY};
    width: 30;
}}
#event-log {{
    height: 12;
    border: ascii {DIM_GRAY};
    background: transparent;
}}
Button {{
    height: 1;
    border: none;
    margin-right: 1;
    min-width: 10;
}}
.btn-terminate {{
    background: {TRUE_RED};
    color: black;
}}
.btn-prio-up, .btn-prio-down, .btn-tune {{
    background: {DIM_GRAY};
    color: white;
}}
DataTable {{
    height: 1fr;
    border: ascii {DIM_GRAY};
}}
"""
