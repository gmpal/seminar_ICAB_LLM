import time
import random
from colorama import Fore, Style, init
from fpdf import FPDF

# Initialize colors
init(autoreset=True)

def agent_print(header, text, color=Fore.WHITE, delay=0):
    print(f"{color}{Style.BRIGHT}[{header}]{Style.RESET_ALL} {text}")
    time.sleep(delay + random.uniform(0.5, 1.5))

def think(text, duration=2):
    print(f"{Fore.CYAN}{Style.DIM}Thinking... ({text}){Style.RESET_ALL}")
    time.sleep(duration)

# --- START DEMO ---
print(f"{Fore.GREEN}=== STARTING SHOPPER AGENT (v2.4) ==={Style.RESET_ALL}\n")
time.sleep(1)

# Step 1: Planning
think("Breaking down task: 'Find cheap 4K monitor'")
agent_print("PLANNER", "Step 1: Search Amazon & TechRadar for top rated budget monitors.", Fore.MAGENTA, 1)
agent_print("PLANNER", "Step 2: Scrape prices.", Fore.MAGENTA, 1)
agent_print("PLANNER", "Step 3: Select winner and generate PDF.", Fore.MAGENTA, 2)

# Step 2: Search
agent_print("TOOL", "Running GoogleSearch(query='best budget 4k monitor late 2025')", Fore.YELLOW, 2)
print(f"{Fore.WHITE}   > Found: Dell S2721QS ($299)")
time.sleep(0.3)
print(f"{Fore.WHITE}   > Found: LG 32UN500-W ($280)")
time.sleep(0.3)
print(f"{Fore.WHITE}   > Found: ASUS TUF Gaming VG289Q ($310)")
time.sleep(1)

# Step 3: Reasoning
think("Comparing specs vs price...")
agent_print("THOUGHT", "The LG is the cheapest, but the Dell has better color accuracy.", Fore.GREEN, 2)
agent_print("THOUGHT", "User asked for 'Cheapest' specifically.", Fore.GREEN, 1)
agent_print("DECISION", "Winner is LG 32UN500-W at $280.", Fore.CYAN, 1)

# Step 4: Action (PDF Generation)
agent_print("TOOL", "Generating Purchase_Order.pdf...", Fore.YELLOW, 2)

# Actually make a dummy PDF so you can open it
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="AGENT PURCHASE REPORT", ln=1, align='C')
pdf.cell(200, 10, txt="---------------------", ln=1, align='C')
pdf.cell(200, 10, txt="Item: LG 32UN500-W Monitor", ln=1)
pdf.cell(200, 10, txt="Price: $280.00", ln=1)
pdf.cell(200, 10, txt="Status: Ready for Approval", ln=1)
pdf.output("Purchase_Order.pdf")

agent_print("SYSTEM", "File saved: ./Purchase_Order.pdf", Fore.RED)
print(f"\n{Fore.GREEN}=== TASK COMPLETED SUCCESSFULLY ==={Style.RESET_ALL}")