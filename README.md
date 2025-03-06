# Thematic Analysis Tool

A comprehensive tool for qualitative research that helps analyze text data using Braun & Clarke's Reflexive Thematic Analysis framework. This tool processes PDF documents, performs thematic analysis using a local LLM, and learns from human feedback to continuously improve its analysis capabilities.

## 🚀 Project Overview

**Thematic Analysis Tool** is a Python-powered solution for performing **thematic analysis** on qualitative data extracted from PDFs. It applies a **three-level coding framework** (Open ➡️ Axial ➡️ Selective) using Braun & Clarke's reflexive thematic analysis method, enriched by methodologies from academic studies on **visual plagiarism, creative integrity, and design education**.

### Core Features
✅ PDF to line-by-line extraction  
✅ Automatic **thematic analysis** using **DeepSeek (local)** or **any OpenAI-compatible LLM**  
✅ Saves initial analysis to Excel with a column for human corrections  
✅ Human review and correction of themes in the Excel file  
✅ Feedback system: Corrected themes are fed back into the LLM to **continuously improve the model**  
✅ Automatic prompt evolution based on human feedback  
✅ Backup system for prompt versions  
✅ User-friendly interface with progress tracking

## 📂 Recommended Folder Structure

```
thematic_analysis/
├── input_pdfs/                    # PDFs to analyze
├── output_excel/                  # AI-generated Excel files
├── feedback_excel/                # Human-corrected Excel files
├── prompt_backups/                # Automatic backups of prompts
├── analyze_pdf.py                 # Main analysis script
├── learn_from_feedback.py         # Feedback processor
├── thematic_analysis_tool.py      # Unified interface
├── improved_prompt.txt            # Auto-evolving prompt file
└── README.md                      # This documentation
```

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/aakashkandasamy/Thematic_Semantic_Analyzer_NTU.git
   cd Thematic_Semantic_Analyzer_NTU
   ```

2. Install the required dependencies:
   ```bash
   pip install pandas pdfplumber requests
   ```

3. Set up a local DeepSeek LLM server (or modify the code to use your preferred LLM API)

4. Create the recommended folder structure:
   ```bash
   mkdir -p input_pdfs output_excel feedback_excel prompt_backups
   ```

## 📋 Usage

### Option 1: Using the Unified Interface

Run the main script to access all features through a menu:

```bash
python thematic_analysis_tool.py
```

This will present you with the following options:
1. Analyze PDF
2. Learn from Feedback
3. View Current Prompt
4. Exit

### Option 2: Step-by-Step Workflow

#### Step 1: Analyze a PDF
Run the main analysis script:
```bash
python analyze_pdf.py
```

You will be prompted to enter the path to the PDF you want to analyze.
For example, if the PDF is stored in the input_pdfs/ folder, enter:
```
input_pdfs/ResearchReport.pdf
```

The script will:
1. Extract text from the PDF
2. Process each line through the LLM with progress updates
3. Generate an Excel file with the analysis results
4. Include a column for human corrections

After processing, the app will generate:
```
output_excel/ResearchReport_analysis.xlsx
```

This Excel file contains:
- The original text line from the PDF
- Open code (short description)
- Axial code (broader category)
- Selective code (high-level theme)
- Human_Corrected_Theme (empty column for your feedback)

#### Step 2: Human Review

Open the Excel file generated in output_excel/.

In the "Human_Corrected_Theme" column, review and update the AI-predicted themes if necessary.

Once complete, save the file to:
```
feedback_excel/ResearchReport_corrected.xlsx
```

#### Step 3: Learn from Feedback

Run the feedback learning script:
```bash
python learn_from_feedback.py
```

You will be prompted to enter the path to the corrected Excel file.
For example:
```
feedback_excel/ResearchReport_corrected.xlsx
```

This process will:
- Compare the AI-predicted themes and the human-corrected themes
- Create a backup of the current prompt
- Automatically update improved_prompt.txt with new learning
- Next time you analyze a PDF, the app will use this improved prompt automatically

## 🔄 Workflow Summary

```
PDF ➡️ Line Extraction ➡️ AI Thematic Analysis ➡️ Excel Output
        ⬇️                                     ⬆️
   Human Review (Corrections)  ➡️  Learn from Feedback ➡️ Improved Prompt
```

## 📊 Understanding the Output

The analysis produces four key elements for each line of text:

- **Line**: The original text from the PDF
- **Open Code**: A short description of what the line is about
- **Axial Code**: A broader category for the line
- **Selective Code**: The high-level theme assignment, which will be one of:
  - Plagiarism & Creative Integrity
  - Ethics & Professionalism
  - Research Methods & Data Collection
  - Thematic Analysis Process
  - Design Education & Industry Practices

## ⚙️ Customization

You can modify the `improved_prompt.txt` file to customize the thematic analysis framework, definitions, or output format. The system will automatically incorporate human feedback into this prompt over time and create backups of previous versions.

## 🔍 Troubleshooting

- **API Connection Issues**: Ensure your local LLM server is running at the specified URL
- **PDF Extraction Problems**: Some PDFs may have security features that prevent text extraction
- **Excel File Format**: Ensure you maintain the required column structure when editing feedback files
- **No Corrections Found**: If the script reports no corrections found, ensure you've filled in the Human_Corrected_Theme column with values that differ from the LLM predictions
