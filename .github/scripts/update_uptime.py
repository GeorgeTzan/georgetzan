import re
from datetime import datetime

BIRTHDAY = datetime(2004, 8, 8) 
now = datetime.now()

years = now.year - BIRTHDAY.year
if (now.month, now.day) < (BIRTHDAY.month, BIRTHDAY.day):
    years -= 1

last_birthday = datetime(now.year if (now.month, now.day) >= (BIRTHDAY.month, BIRTHDAY.day) else now.year - 1, BIRTHDAY.month, BIRTHDAY.day)
remaining_days = (now - last_birthday).days

uptime_str = f'<span style="color: #ff9e3b; font-weight: bold;">Uptime</span> ......... {years} years, {remaining_days} days<br/>'

with open("assets/coloring.svg", "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"<!-- UPTIME:START -->.*?<!-- UPTIME:END -->"
replacement = f"<!-- UPTIME:START -->\n      {uptime_str}\n      <!-- UPTIME:END -->"

updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open("assets/coloring.svg", "w", encoding="utf-8") as f:
    f.write(updated_content)
