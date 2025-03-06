import os
import sys

def show_menu():
    print("\n=== Thematic Analysis Tool ===")
    print("1. Analyze PDF")
    print("2. Learn from Feedback")
    print("3. View Current Prompt")
    print("4. Exit")
    return input("Select an option (1-4): ")

def main():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    while True:
        choice = show_menu()
        
        if choice == '1':
            from analyze_pdf import process_pdf_to_excel
            pdf_path = input("Enter the path to your PDF file: ").strip()
            if not os.path.exists(pdf_path):
                print(f"❌ File not found: {pdf_path}")
            else:
                process_pdf_to_excel(pdf_path)
                
        elif choice == '2':
            from learn_from_feedback import learn_from_feedback
            feedback_dir = os.path.join(base_dir, "feedback_excel")
            print(f"\nFeedback files should be in: {feedback_dir}")
            
            if os.path.exists(feedback_dir):
                feedback_files = [f for f in os.listdir(feedback_dir) if f.endswith('.xlsx')]
                if feedback_files:
                    print("Available feedback files:")
                    for i, file in enumerate(feedback_files, 1):
                        print(f"{i}. {file}")
            
            feedback_file = input("Enter the path to the feedback Excel file: ").strip()
            
            if not os.path.isabs(feedback_file) and not feedback_file.startswith('./'):
                if not os.path.exists(feedback_file):
                    potential_path = os.path.join(feedback_dir, feedback_file)
                    if os.path.exists(potential_path):
                        feedback_file = potential_path
            
            if not os.path.exists(feedback_file):
                print(f"❌ File not found: {feedback_file}")
            else:
                learn_from_feedback(feedback_file)
                
        elif choice == '3':
            prompt_file = os.path.join(base_dir, "improved_prompt.txt")
            if os.path.exists(prompt_file):
                with open(prompt_file, "r") as f:
                    print("\n=== Current Prompt ===")
                    print(f.read())
            else:
                print("❌ Prompt file not found.")
                
        elif choice == '4':
            print("Exiting. Goodbye!")
            sys.exit(0)
            
        else:
            print("Invalid choice. Please select 1-4.")
            
if __name__ == "__main__":
    main() 