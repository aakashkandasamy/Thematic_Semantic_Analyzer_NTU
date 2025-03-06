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
    while True:
        choice = show_menu()
        
        if choice == '1':
            # Import here to avoid circular imports
            from analyze_pdf import process_pdf_to_excel
            pdf_path = input("Enter the path to your PDF file: ").strip()
            if not os.path.exists(pdf_path):
                print(f"❌ File not found: {pdf_path}")
            else:
                process_pdf_to_excel(pdf_path)
                
        elif choice == '2':
            from learn_from_feedback import learn_from_feedback
            feedback_file = input("Enter the path to the feedback Excel file: ").strip()
            if not os.path.exists(feedback_file):
                print(f"❌ File not found: {feedback_file}")
            else:
                learn_from_feedback(feedback_file)
                
        elif choice == '3':
            prompt_file = "improved_prompt.txt"
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