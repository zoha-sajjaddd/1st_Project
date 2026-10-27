import joblib
import pandas as pd

def interactive_prediction():
    try:
        model = joblib.load('model.pkl')
    except FileNotFoundError:
        print("❌ Error: 'model.pkl' not found. Please run 'main.py' first!")
        return

    print("="*65)
    print("     AI-POWERED STUDENT GRADE CLASSIFICATION SYSTEM      ")
    print("="*65)
    print("Type 'n', 'no', or 'exit' when prompted to quit.\n")

    while True:
        print("-" * 50)
        print("Enter details for the new student:")
        
        try:
            stu_hours = float(input("  -> Study hours per week: "))
            attendance = float(input("  -> Attendance percentage (0-100): "))
            eng = float(input("  -> English marks: "))
            isl = float(input("  -> Islamiat marks: "))
            maths = float(input("  -> Maths marks: "))
            statistics = float(input("  -> Statistics marks: "))
            linear_algebra = float(input("  -> Linear Algebra marks: "))
        except ValueError:
            print("\n❌ Invalid input! Please enter valid numbers only.\n")
            continue

        # Package user inputs into a DataFrame
        user_input = pd.DataFrame([{
            'stu_hours': stu_hours,
            'attendance': attendance,
            'eng': eng,
            'isl': isl,
            'maths': maths,
            'statistics': statistics,
            'linear_algebra': linear_algebra
        }])

        # Predict the letter grade directly
        predicted_grade = model.predict(user_input)[0]

        # Display the result
        print("\n" + "="*45)
        print(" 🎯 AI PREDICTION RESULTS:")
        print(f"    • Predicted Student Grade: {predicted_grade}")
        print("="*45 + "\n")

        # Exit prompt check
        choice = input("Do you want to predict for another student? (y/n): ").strip().lower()
        
        # This properly catches 'n', 'no', 'exit', or anything other than 'y'
        if choice in ['n', 'no', 'exit', 'quit']:
            print("\nExiting predictor. Good luck with your project! 👋")
            break

if __name__ == '__main__':
    interactive_prediction()