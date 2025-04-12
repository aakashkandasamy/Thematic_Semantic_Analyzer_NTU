import os
import sys

def show_menu():
    print("\n=== Thematic Analysis Tool ===")
    print("1. Analyze PDF")
    print("2. Learn from Feedback")
    print("3. View Current Prompt")
    print("4. Exit")
    return input("Select an option (1-4): ")

def list_files_in_directory(directory, extension):
    files = [f for f in os.listdir(directory) if f.endswith(extension)]
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    return files

def main():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    while True:
        choice = show_menu()
        
        if choice == '1':
            from analyze_pdf import process_pdf_to_excel
            pdf_dir = os.path.join(base_dir, "input_pdfs")
            print(f"\nPDF files available in: {pdf_dir}")
            pdf_files = list_files_in_directory(pdf_dir, '.pdf')
            pdf_choice = int(input("Select a PDF file by number: ")) - 1
            pdf_path = os.path.join(pdf_dir, pdf_files[pdf_choice])
            process_pdf_to_excel(pdf_path)
                
        elif choice == '2':
            from learn_from_feedback import learn_from_feedback
            feedback_dir = os.path.join(base_dir, "feedback_excel")
            print(f"\nFeedback files available in: {feedback_dir}")
            feedback_files = list_files_in_directory(feedback_dir, '.xlsx')
            feedback_choice = int(input("Select a feedback file by number: ")) - 1
            feedback_file = os.path.join(feedback_dir, feedback_files[feedback_choice])
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