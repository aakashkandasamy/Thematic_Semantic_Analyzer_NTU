import pandas as pd
from collections import defaultdict
import os
import datetime

# Update the prompt file path to use the correct location
base_dir = os.path.dirname(os.path.abspath(__file__))
PROMPT_FILE = os.path.join(base_dir, "improved_prompt.txt")

def learn_from_feedback(feedback_excel_path):
    try:
        df = pd.read_excel(feedback_excel_path)

        if not {'line', 'LLM_Predicted_Theme', 'Human_Corrected_Theme'}.issubset(df.columns):
            raise ValueError("Feedback file must contain columns: line, LLM_Predicted_Theme, Human_Corrected_Theme")

        # Check if there are any corrections
        has_corrections = False
        for _, row in df.iterrows():
            predicted = row['LLM_Predicted_Theme']
            corrected = row['Human_Corrected_Theme']
            if pd.notna(predicted) and pd.notna(corrected) and predicted != corrected:
                has_corrections = True
                break
                
        if not has_corrections:
            print("ℹ️ No corrections found in the feedback file.")
            return

        correction_counts = defaultdict(lambda: defaultdict(int))

        for _, row in df.iterrows():
            predicted = row['LLM_Predicted_Theme']
            corrected = row['Human_Corrected_Theme']

            if pd.notna(predicted) and pd.notna(corrected) and predicted != corrected:
                correction_counts[predicted][corrected] += 1

        improvement_guidance = "\n".join([
            f"- When you predicted '{predicted}', human corrected it to: " +
            ", ".join([f"'{corrected}' ({count} times)" for corrected, count in corrections.items()])
            for predicted, corrections in correction_counts.items()
        ])

        # Create a backup of the current prompt
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"{PROMPT_FILE}.{timestamp}.bak"
        
        with open(PROMPT_FILE, "r") as f:
            current_prompt = f.read().strip()
            
        # Save backup
        with open(backup_file, "w") as f:
            f.write(current_prompt)
            
        updated_prompt = f"""
{current_prompt}

## Feedback-Based Improvements (Learned from Human Corrections)
{improvement_guidance}
    """

        with open(PROMPT_FILE, "w") as f:
            f.write(updated_prompt)

        print(f"✅ Feedback incorporated into {PROMPT_FILE}")
        print(f"✅ Backup saved to {backup_file}")
        print("✅ Next analysis run will use the updated prompt.")
    except Exception as e:
        print(f"❌ Error updating prompt file: {str(e)}")
        return

if __name__ == "__main__":
    feedback_file = input("Enter the path to the feedback Excel file: ").strip()
    if not os.path.exists(feedback_file):
        print(f"❌ File not found: {feedback_file}")
    else:
        learn_from_feedback(feedback_file)