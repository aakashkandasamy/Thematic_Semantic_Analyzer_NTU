import os
import pdfplumber
import pandas as pd
import requests
import json
import time


DEEPSEEK_LOCAL_URL = "http://localhost:8000/v1/chat/completions"
MODEL_NAME = "deepseek-chat"

PROMPT_FILE = "improved_prompt.txt"

if os.path.exists(PROMPT_FILE):
    with open(PROMPT_FILE, "r") as f:
        THEMATIC_PROMPT = f.read().strip()
else:

    THEMATIC_PROMPT = """
You are a qualitative research assistant specializing in thematic analysis. 
Analyze each line from qualitative research data related to visual plagiarism, creative integrity, and professional ethics in Singapore's Art & Design industry.

Follow Braun & Clarke's Reflexive Thematic Analysis framework (2006):
1. Open Coding: Describe what the line is about.
2. Axial Coding: Categorize the line into broader concepts.
3. Selective Coding: Place the line into one of these High-Level Themes:
    - Plagiarism & Creative Integrity
    - Ethics & Professionalism
    - Research Methods & Data Collection
    - Thematic Analysis Process
    - Design Education & Industry Practices

Definitions:
- Plagiarism & Creative Integrity: Issues around copying, originality, cultural borrowing.
- Ethics & Professionalism: Ethical practices, responsibility in creative work.
- Research Methods & Data Collection: Interviews, focus groups, sampling, qualitative data collection.
- Thematic Analysis Process: Open, axial, and selective coding; identifying, refining, and reporting themes.
- Design Education & Industry Practices: Education challenges, faculty views, mentoring, cultural factors.

For each line, output strictly in this JSON format:
{
    "line": "<original line>",
    "open_code": "<short description>",
    "axial_code": "<category>",
    "selective_code": "<high-level theme>"
}
    """

def extract_lines_from_pdf(pdf_path):
    lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines.extend(line.strip() for line in text.split('\n') if line.strip())
    return lines

def call_deepseek_local(line):
    user_prompt = f"{THEMATIC_PROMPT}\n\nLine to analyze:\n{line}"

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a thematic analysis expert."},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 1024
    }

    response = requests.post(DEEPSEEK_LOCAL_URL, json=payload)
    response.raise_for_status()
    result_text = response.json()['choices'][0]['message']['content'].strip()

    try:
        return json.loads(result_text)
    except json.JSONDecodeError:
        return {"line": line, "open_code": "Error", "axial_code": "Error", "selective_code": "Error"}

def process_pdf_to_excel(pdf_path):
    lines = extract_lines_from_pdf(pdf_path)
    total_lines = len(lines)
    print(f"Processing {total_lines} lines from PDF...")
    
    results = []
    for i, line in enumerate(lines):
        try:
            result = call_deepseek_local(line)
            results.append(result)
            print(f"Processed line {i+1}/{total_lines} - Theme: {result['selective_code']}")
            # Add a small delay to avoid overwhelming the API
            time.sleep(0.5)
        except Exception as e:
            print(f"Error processing line {i+1}: {str(e)}")
            results.append({"line": line, "open_code": "Error", "axial_code": "Error", "selective_code": "Error"})
    
    df = pd.DataFrame(results)
    
    # Add a column for human corrections
    df['Human_Corrected_Theme'] = ""
    
    output_path = os.path.splitext(pdf_path)[0] + "_analysis.xlsx"
    df.to_excel(output_path, index=False)

    print(f"✅ Analysis saved to: {output_path}")
    print(f"To provide feedback, fill in the 'Human_Corrected_Theme' column and use learn_from_feedback.py")

if __name__ == "__main__":
    pdf_path = input("Enter the path to your PDF file: ").strip()
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
    else:
        process_pdf_to_excel(pdf_path)