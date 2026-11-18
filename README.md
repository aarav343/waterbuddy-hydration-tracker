# WaterBuddy Hydration Tracker

WaterBuddy is a Python and Streamlit app for tracking daily water intake in millilitres. It suggests a goal, records drinks, and shows how much water remains to reach the target.

[Open WaterBuddy on Streamlit](https://water-buddy-hydration-tracker.streamlit.app/) · [View source on GitHub](https://github.com/aarav343/waterbuddy-hydration-tracker)

## Project requirements

| Requirement | Expected behaviour |
| --- | --- |
| Suggest a daily goal | Select one of four age groups to load its default goal. |
| Adjust the goal | Edit the target between 250 and 6,000 ml. The step buttons change it by 50 ml. |
| Log a quick amount | Add 150, 250, 350, or 500 ml with one click. |
| Enter a custom amount | Enter a positive amount up to 3,000 ml and click **Add amount**. Zero adds no entry. |
| Display progress | Show total intake, percentage of goal, a progress bar, and the amount remaining. |
| Show milestones | Update the message when intake reaches 50%, 75%, and 100% of the target. |
| Display today's entries | List logged amounts with the newest entry first. |
| Start a new day | Ask for confirmation. **Cancel** keeps the entries. **Yes, reset** clears the intake and entries while retaining the age group and goal. |

### Default goals

| Age group | Daily goal |
| --- | ---: |
| Children (4 to 8) | 1,200 ml |
| Teens (9 to 13) | 1,700 ml |
| Adults (14 to 64) | 2,250 ml |
| Seniors (65+) | 1,850 ml |

The app starts with the adult preset. Selecting a different group replaces the current goal with that group's default. The values are coursework presets for demonstrating the tracker.

## Local setup requirements

- Python 3.12 and Streamlit 1.45.1 were used for verification.
- A web browser and a copy of the project containing `app.py`.
- Internet access for downloading Streamlit and its dependencies.

Run these commands from the folder containing `app.py` on macOS or Linux.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install streamlit==1.45.1
python -m streamlit run app.py
```

On Windows, use `py -m venv .venv` to create the environment and `.venv\Scripts\Activate.ps1` to activate it in PowerShell. Open the local URL printed by Streamlit.

## Try the main workflow

1. Select **Children (4 to 8)** and check that the goal changes to **1,200 ml**.
2. Change **Daily goal (ml)** to **1,000** and press Enter.
3. Click **+250 ml**. The app shows **25%** and **750 ml** remaining.
4. Enter **300** and click **Add amount**. The total rises to **550 ml**, progress reaches **55%**, and the entry list shows **300 ml · 250 ml**.
5. Click **+250 ml** twice to reach **800 ml** and then **1,050 ml**. At **105%**, the bar is full and the remaining amount is **0 ml**.
6. Click **New day**, then **Cancel** to keep the total. Open **New day** again and select **Yes, reset** to clear the total and entries. The **1,000 ml** goal remains.

## Implementation and scope

`app.py` defines the Streamlit interface, goal presets, input handlers, and calculations. Remaining water is the goal minus the total, with a minimum of zero. The displayed percentage is intake divided by the goal, rounded to a whole percent. The visual bar stops at 100% while the percentage can go higher.

The current goal, intake, and entries live in Streamlit session state. The project covers one day's intake in the current browser session. Long-term history, account sync, and timed reminders are outside the current scope.
