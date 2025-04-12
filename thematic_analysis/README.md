# Thematic Analysis Tool

A comprehensive tool for qualitative research that helps analyze text data using Braun & Clarke's Reflexive Thematic Analysis framework. This tool processes PDF documents, performs thematic analysis using Google's Gemini API, and learns from human feedback to continuously improve its analysis capabilities.

## 🚀 Project Overview

**Thematic Analysis Tool** is a Python-powered solution for performing **thematic analysis** on qualitative data extracted from PDFs. It applies a **three-level coding framework** (Open ➡️ Axial ➡️ Selective) using Braun & Clarke's reflexive thematic analysis method, enriched by methodologies from academic studies on **visual plagiarism, creative integrity, and design education**.

### Core Features
✅ PDF to line-by-line extraction  
✅ Automatic **thematic analysis** using **Google's Gemini API**  
✅ Saves initial analysis to Excel with a column for human corrections  
✅ Human review and correction of themes in the Excel file  
✅ Feedback system: Corrected themes are fed back into the LLM to **continuously improve the model**  
✅ Automatic prompt evolution based on human feedback  
✅ Backup system for prompt versions  
✅ User-friendly interface with progress tracking

## 📂 Project Structure

```
thematic_analysis/
├── input_pdfs/                    # PDFs to analyze
├── feedback_excel/                # Human-corrected Excel files
├── past_prompts/                  # Backup of previous prompt versions
├── analyze_pdf.py                 # Main analysis script
├── learn_from_feedback.py         # Feedback processor
├── thematic_analysis_tool.py      # Unified interface
├── improved_prompt.txt            # Auto-evolving prompt file
├── .env                          # Environment variables (API keys)
├── requirements.txt               # Python dependencies
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
   pip install -r requirements.txt
   ```

3. Set up your environment:
   - Create a `.env` file in the project root
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

4. Create the required folders:
   ```bash
   mkdir -p input_pdfs feedback_excel past_prompts
   ```

## 📋 Usage

### Using the Unified Interface

Run the main script to access all features through a menu:

```bash
python thematic_analysis_tool.py
```

This will present you with the following options:
1. Analyze PDF
2. Learn from Feedback
3. View Current Prompt
4. Exit

### Step-by-Step Workflow

#### Step 1: Analyze a PDF
1. Place your PDF file in the `input_pdfs/` directory
2. Run the analysis through the unified interface
3. Select the PDF file from the list
4. The script will:
   - Extract text from the PDF
   - Process each line through Gemini API with progress updates
   - Generate an Excel file with the analysis results
   - Include a column for human corrections

The output Excel file will be created in the same directory as the input PDF, with "_analysis.xlsx" appended to the filename.

#### Step 2: Human Review
1. Open the generated Excel file
2. Review the analysis in the following columns:
   - `line`: Original text from the PDF
   - `open_code`: Short description of the line
   - `axial_code`: Broader category
   - `selective_code`: High-level theme
   - `Human_Corrected_Theme`: Column for your corrections
3. Make corrections in the `Human_Corrected_Theme` column
4. Save the corrected file in the `feedback_excel/` directory

#### Step 3: Learn from Feedback
1. Run the feedback learning through the unified interface
2. Select the corrected Excel file
3. The system will:
   - Compare AI predictions with human corrections
   - Create a backup of the current prompt
   - Update `improved_prompt.txt` with new learning
   - Next analysis will use the improved prompt automatically

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

## 🔒 Security Note

The `.env` file containing your API key is automatically excluded from version control via `.gitignore`. Never commit this file to your repository.

## ⚙️ Customization

You can modify the `improved_prompt.txt` file to customize the thematic analysis framework, definitions, or output format. The system will automatically incorporate human feedback into this prompt over time and create backups in the `past_prompts/` directory.

## 🔍 Troubleshooting

- **API Connection Issues**: Ensure your Gemini API key is correctly set in the `.env` file
- **PDF Extraction Problems**: Some PDFs may have security features that prevent text extraction
- **Excel File Format**: Ensure you maintain the required column structure when editing feedback files
- **No Corrections Found**: If the script reports no corrections found, ensure you've filled in the Human_Corrected_Theme column with values that differ from the LLM predictions 