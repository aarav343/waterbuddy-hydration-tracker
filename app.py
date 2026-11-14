import streamlit as st

st.set_page_config(page_title="WaterBuddy", page_icon="💧", layout="centered")

AGE_GOALS = {
    "Children (4 to 8)": 1200,
    "Teens (9 to 13)": 1700,
    "Adults (14 to 64)": 2250,
    "Seniors (65+)": 1850,
}


def set_goal_from_age():
    st.session_state.daily_goal = AGE_GOALS[st.session_state.age_group]


def add_water(amount):
    amount = int(amount or 0)
    if amount > 0:
        st.session_state.total_ml += amount
        st.session_state.entries.append(amount)


def add_typed_water():
    add_water(st.session_state.typed_amount)
    st.session_state.typed_amount = 0


def confirm_new_day():
    st.session_state.show_reset_confirm = True


def cancel_new_day():
    st.session_state.show_reset_confirm = False


def reset_new_day():
    st.session_state.total_ml = 0
    st.session_state.entries = []
    st.session_state.show_reset_confirm = False


def show_message(message):
    st.markdown(
        f'<div style="padding:12px 14px;border:1px solid #c9e2e6;border-radius:12px;'
        f'background:#edf7f8;color:#173744;font-weight:600;">{message}</div>',
        unsafe_allow_html=True,
    )


for key, value in {
    "age_group": "Adults (14 to 64)",
    "daily_goal": 2250,
    "total_ml": 0,
    "entries": [],
    "typed_amount": 0,
    "show_reset_confirm": False,
}.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.markdown(
    """
    <style>
    :root { color-scheme: light !important; }
    html, body, .stApp, [data-testid="stAppViewContainer"],
    [data-testid="stMain"], [data-testid="stMainBlockContainer"] {
      color-scheme: light !important;
      color: #173744 !important;
      background: #f3f7f8 !important;
      background-image: none !important;
    }
    [data-testid="stHeader"] { background: #f3f7f8 !important; }
    [data-testid="stMain"] h1, [data-testid="stMain"] h2,
    [data-testid="stMain"] h3, [data-testid="stMain"] h4,
    [data-testid="stMain"] p, [data-testid="stMain"] label,
    [data-testid="stMain"] span, [data-testid="stMain"] [data-testid="stCaptionContainer"],
    [data-testid="stMain"] [data-testid="stMetricLabel"],
    [data-testid="stMain"] [data-testid="stMetricValue"] {
      color: #173744 !important;
    }
    [data-testid="stMain"] input, [data-testid="stMain"] [role="combobox"],
    [data-testid="stMain"] [role="spinbutton"],
    [data-testid="stMain"] [data-baseweb="select"],
    [data-testid="stMain"] [data-baseweb="input"] {
      color: #173744 !important; -webkit-text-fill-color: #173744 !important;
      background: #ffffff !important; background-image: none !important;
      border-color: #b9cdd3 !important;
    }
    [data-testid="stMain"] [role="progressbar"] { background: #dcebed !important; border-radius: 999px !important; }
    [data-testid="stMain"] [role="progressbar"] > div { background: #0b91a5 !important; border-radius: 999px !important; }
    .block-container { max-width: 820px; padding: 1.5rem 1.1rem 3rem; }
    .wb-hero { display:flex; align-items:center; gap:18px; margin:0 0 1.4rem; padding:25px 27px; border-radius:24px; background:#087e99 !important; box-shadow:0 15px 35px rgba(9,105,124,.18); }
    .wb-drop { display:grid; place-items:center; flex:0 0 58px; height:58px; border:1px solid rgba(255,255,255,.4); border-radius:19px; background:rgba(255,255,255,.16); font-size:30px; }
    .wb-brand { color:white !important; font-size:1.75rem; line-height:1.15; font-weight:800; letter-spacing:-.03em; }
    .wb-tagline { color:#e7ffff !important; margin-top:5px; font-size:.98rem; }
    .wb-kicker { color:#e0ffff !important; font-size:.72rem; font-weight:800; letter-spacing:.13em; text-transform:uppercase; margin-bottom:4px; }
    [data-testid="stVerticalBlockBorderWrapper"] { border:1px solid #d5e1e5 !important; border-radius:20px !important; background:#ffffff !important; background-image:none !important; box-shadow:0 6px 18px rgba(24,76,91,.06); }
    [data-testid="stMetricLabel"] p { color:#55717c !important; font-size:.83rem !important; }
    [data-testid="stMetricValue"] { color:#123b49 !important; font-weight:750 !important; }
    [data-testid="stProgress"] { margin:.45rem 0 .8rem; }
    .wb-remaining { display:flex; align-items:center; gap:8px; margin-top:8px; padding:11px 14px; border-radius:13px; background:#eaf6f7; }
    .wb-remaining strong { color:#126a78; font-size:1rem; }
    .wb-remaining span { color:#54727c; font-size:.9rem; }
    [data-testid="stMain"] button { border-radius:13px; border:1px solid #c8e6eb; background:#eaf7f9; color:#124757 !important; font-weight:700; transition:transform .15s ease,box-shadow .15s ease; }
    [data-testid="stMain"] button:hover { border-color:#6fc6ce; background:#def3f5; box-shadow:0 5px 12px rgba(19,117,133,.1); transform:translateY(-1px); }
    [data-testid="stMain"] button[kind="primary"] { background:#087e99 !important; color:white !important; border-color:#087e99 !important; }
    [data-baseweb="select"] > div, [data-baseweb="input"] > div { background:#ffffff !important; background-image:none !important; border-color:#b9cdd3 !important; border-radius:12px !important; }
    [data-baseweb="select"] *, [data-baseweb="input"] input { color:#173744 !important; }
    @media (max-width:600px) { .block-container { padding:1rem .8rem 2.5rem; } .wb-hero { padding:20px; gap:14px; border-radius:20px; } .wb-brand { font-size:1.5rem; } [data-testid="stMetricValue"] { font-size:1.35rem !important; } }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="wb-hero"><div class="wb-drop">💧</div><div>'
    '<div class="wb-kicker">YOUR DAILY HYDRATION COMPANION</div>'
    '<div class="wb-brand">WaterBuddy</div>'
    '<div class="wb-tagline">A little water. A brighter day.</div></div></div>',
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.subheader("Set your daily target")
    st.caption("Choose an age group to get a suggested goal. You can adjust it anytime.")
    st.selectbox("Age group", list(AGE_GOALS), key="age_group", on_change=set_goal_from_age)
    st.number_input("Daily goal (ml)", min_value=250, max_value=6000, step=50, key="daily_goal")

goal = max(1, int(st.session_state.daily_goal))
total = int(st.session_state.total_ml)
remaining = max(0, goal - total)
percent = total / goal * 100
progress = min(1.0, total / goal)

with st.container(border=True):
    st.subheader("Today's progress")
    st.progress(progress)
    st.caption(f"{int(round(percent))}% of your daily goal")
    st.metric("Total today", f"{total:,} ml")
    st.markdown(
        f'<div class="wb-remaining"><strong>{remaining:,} ml</strong>'
        '<span>left to reach your daily goal</span></div>',
        unsafe_allow_html=True,
    )
    if total >= goal:
        message = "Great job! You reached your goal today! 🎉"
    elif percent >= 75:
        message = "Almost there! You are past 75%. 🌊"
    elif percent >= 50:
        message = "Great! You reached 50%! 😊"
    else:
        message = "You’re doing well. Every glass gets you closer! 💙"
    show_message(message)

st.subheader("Log some water")
st.caption("Choose a quick pour or enter your own amount.")
quick_columns = st.columns(4)
for column, amount in zip(quick_columns, (150, 250, 350, 500)):
    with column:
        if st.button(f"+{amount} ml", use_container_width=True):
            add_water(amount)
            st.rerun()

entry_col, button_col = st.columns([2, 1])
with entry_col:
    st.number_input("Or type an amount (ml)", min_value=0, max_value=3000, step=50, key="typed_amount")
with button_col:
    st.write("")
    st.write("")
    st.button("Add amount", use_container_width=True, on_click=add_typed_water)

if st.session_state.entries:
    st.subheader("Today's entries")
    st.write(" · ".join(f"{amount:,} ml" for amount in reversed(st.session_state.entries)))

if st.session_state.show_reset_confirm:
    show_message("Start a new day?")
    reset_col, cancel_col = st.columns(2)
    with reset_col:
        st.button("Yes, reset", type="primary", use_container_width=True, on_click=reset_new_day)
    with cancel_col:
        st.button("Cancel", use_container_width=True, on_click=cancel_new_day)
else:
    st.button("New day", on_click=confirm_new_day)

st.caption("Your progress stays in this browser session and is not sent to an account.")
