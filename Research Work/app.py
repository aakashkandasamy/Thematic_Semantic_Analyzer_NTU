import os
import pdfplumber
import pandas as pd

THEMATIC_KEYWORDS = {
    "Plagiarism": ["plagiarism", "copying", "intellectual property", "visual plagiarism"],
    "Ethics": ["ethics", "integrity", "responsibility", "moral", "ethical"],
    "Design Process": ["design", "creativity", "art", "visual", "creative process"],
    "Research Methodology": ["interview", "focus group", "qualitative", "analysis", "sampling", "transcript"],
    "Data Analysis": ["coding", "thematic", "analysis", "themes", "categories", "qualitative data"],
    "Education": ["teaching", "faculty", "students", "education", "learning"],
    "Industry Practices": ["industry", "professional", "practitioners", "standards", "communication design"]
}

def suggest_theme(line):
    matched_themes = []
    lower_line = line.lower()

    for theme, keywords in THEMATIC_KEYWORDS.items():
        if any(keyword.lower() in lower_line for keyword in keywords):
            matched_themes.append(theme)

    return "; ".join(matched_themes) if matched_themes else "Uncategorized"

def extract_lines_from_pdf(pdf_path):
    lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                page_lines = text.split('\n')
                lines.extend(page_lines)
    return lines

def create_dataframe_with_themes(lines):
    df = pd.DataFrame(lines, columns=['Line'])
    df['Theme'] = df['Line'].apply(suggest_theme)
    return df

def process_pdf_to_excel(pdf_path):
    lines = extract_lines_from_pdf(pdf_path)

    if not lines:
        print(f"No readable text found in {pdf_path}")
        return

    df = create_dataframe_with_themes(lines)

    base_name = os.path.splitext(pdf_path)[0]
    excel_path = base_name + ".xlsx"

    df.to_excel(excel_path, index=False)

    print(f"✅ Processed {pdf_path} and saved thematic analysis to {excel_path}")

if __name__ == "__main__":
    input_pdf = input("Enter path to PDF file: ").strip()
    if not os.path.exists(input_pdf):
        print("❌ File not found!")
    else:
        process_pdf_to_excel(input_pdf)