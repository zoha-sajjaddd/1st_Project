import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_grade_model(df):
    """Trains an optimized Random Forest Classifier for higher accuracy."""
    feature_cols = ['stu_hours', 'attendance', 'eng', 'isl', 'maths', 'statistics', 'linear_algebra']
    
    X = df[feature_cols]
    y = df['grade']  
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # TUNED MODEL: More trees, balanced weights, and depth limits for higher accuracy
    model = RandomForestClassifier(
        n_estimators=200,          # More trees for stability
        max_depth=10,              # Prevents overfitting on noisy raw data
        min_samples_split=4,       # Requires more consensus to make a split
        class_weight='balanced',   # Handles class imbalances organically
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    # Evaluate performance
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred) * 100
    print(f"📈 Optimized Classifier Accuracy: {acc:.2f}%")
    
    # Print detailed report to see accuracy per grade (A, B, C, D, F)
    print("\nDetailed Performance Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the model artifact
    joblib.dump(model, 'model.pkl')
    print("✔ Optimized Classifier model saved successfully as 'model.pkl'")
    
    return model