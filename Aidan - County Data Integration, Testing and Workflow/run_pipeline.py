from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
steps = [
    ["Brennan - Pre and Post Integration Data Quality Checks", "assess_quality.py", "before"],
    ["Maddy - Cleaning Verification, Data Dictionary and Status Report", "check_cleaning.py"],
    ["Aidan - County Data Integration, Testing and Workflow", "integrate_data.py"],
    ["Aidan - County Data Integration, Testing and Workflow", "test_integration.py"],
    ["Brennan - Pre and Post Integration Data Quality Checks", "assess_quality.py", "after"],
    ["Maddy - Cleaning Verification, Data Dictionary and Status Report", "make_dictionary.py"],
    ["Aidan - County Data Integration, Testing and Workflow", "analyze_data.py"]
]

for step in steps:
    folder, script, *args = step
    print(f"Running {script}", flush=True)
    subprocess.run([sys.executable, str(root / folder / script), *args], cwd=root, check=True)

print("Current processed-data pipeline completed.")
