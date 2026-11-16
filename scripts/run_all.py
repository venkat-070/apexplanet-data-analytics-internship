"""
run_all.py
Master Orchestration Script for ApexPlanet Data Analytics Internship
Author: Venkata Vedhadri Marisetti (23981A44Y9)
ApexPlanet Software Pvt. Ltd. | 01 Aug - 30 Sep 2026
"""

import subprocess
import sys
import os
import time

SCRIPTS = [
    ("00_generate_dataset.py", "Generating Raw Enterprise Dataset with Realistic Anomalies"),
    ("01_data_wrangling.py", "Task 1: Data Immersion, Quality Audit & Wrangling Pipeline"),
    ("02_eda_and_bi.py", "Task 2: Exploratory Data Analysis & SQL Analytics Verification"),
    ("03_deep_dive_analysis.py", "Task 3: Deep-Dive RFM Segmentation & Dashboard Engine"),
    ("04_statistical_validation.py", "Task 4: Hypothesis Testing & Data Storytelling"),
    ("05_generate_notebooks.py", "Task 5: Generating Interactive Jupyter Notebooks")
]

def main():
    print("=" * 80)
    print("APEXPLANET DATA ANALYTICS INTERNSHIP - COMPLETE PIPELINE RUNNER")
    print("Student: Venkata Vedhadri Marisetti (23981A44Y9)")
    print("College: Raghu Engineering College (Autonomous)")
    print("Guide:   Md Imam Khader Shariff, Assistant Professor")
    print("=" * 80)

    start_time = time.time()
    scripts_dir = os.path.dirname(os.path.abspath(__file__))

    for script_name, description in SCRIPTS:
        script_path = os.path.join(scripts_dir, script_name)
        print(f"\n>>> Running: {script_name} - {description}")
        result = subprocess.run([sys.executable, script_path], capture_output=False)
        if result.returncode != 0:
            print(f"ERROR: Execution failed for {script_name} with exit code {result.returncode}")
            sys.exit(result.returncode)

    elapsed = time.time() - start_time
    print("\n" + "=" * 80)
    print(f"ALL INTERNSHIP TASKS 1-5 EXECUTED SUCCESSFULLY IN {elapsed:.2f}s!")
    print("=" * 80)

if __name__ == "__main__":
    main()
