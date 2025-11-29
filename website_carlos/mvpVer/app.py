import gradio as gr
import random

import pandas as pd

def analyze_risk(
    gender, age, academic_pressure, study_satisfaction, 
    study_hours, sleep_duration, dietary_habits, 
    family_history, financial_stress
):
    """
    Mock backend logic to simulate risk analysis.
    Now predicts both Depression Risk and Suicidal Thoughts Risk.
    """
    # --- Depression Risk Calculation ---
    dep_score = 0
    if academic_pressure > 3: dep_score += 1
    if study_satisfaction < 3: dep_score += 1
    if sleep_duration in ["Less than 5 hours", "5-6 hours"]: dep_score += 1
    if family_history == "Yes": dep_score += 1
    if financial_stress > 3: dep_score += 1
    # Study hours factor (mock)
    if study_hours > 10: dep_score += 1 # Overworking
    
    is_depressed = dep_score >= 3
    dep_result = "Depression Risk: HIGH" if is_depressed else "Depression Risk: LOW"
    
    # --- Suicidal Thoughts Risk Calculation (Mock) ---
    # Based on higher stress and poor habits
    suicide_score = 0
    if academic_pressure >= 4: suicide_score += 1
    if financial_stress >= 4: suicide_score += 1
    if family_history == "Yes": suicide_score += 1
    if dietary_habits == "Unhealthy": suicide_score += 0.5
    
    has_suicidal_risk = suicide_score >= 2.5
    suicide_result = "Suicidal Thoughts Risk: DETECTED" if has_suicidal_risk else "Suicidal Thoughts Risk: LOW"
    
    # Combine results
    final_text = f"{dep_result}\n{suicide_result}"
    

    # Resources Text
    resources_md = """
    ### Help Resources
    
    If you feel overwhelmed, please seek professional help.
    
    *   **Suicide Prevention Lifeline:** 988 (USA) / [Your local number]
    *   **Student Health Services:** Contact your university counseling center.
    *   **Emergency:** Call 911 or go to the nearest hospital.
    """
    
    return final_text, resources_md

# UI Layout
with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Early Identification of Distress Signals
        
        **Disclaimer:** This tool is an academic prototype demonstration. It is **NOT** a real medical diagnosis.
        
        Please complete the following survey to analyze risk factors.
        """
    )
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Demographics")
            gender = gr.Radio(["Male", "Female"], label="Gender")
            age = gr.Slider(18, 30, step=1, label="Age")
            
            gr.Markdown("### Academic Factors")
            academic_pressure = gr.Slider(1, 5, step=1, label="Academic Pressure (1-5)")
            study_satisfaction = gr.Slider(1, 5, step=1, label="Study Satisfaction (1-5)")
            study_hours = gr.Number(label="Study Hours per day (Avg)")
            
        with gr.Column():
            gr.Markdown("### Health & Lifestyle")
            sleep_duration = gr.Dropdown(
                ["Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"], 
                label="Sleep Duration"
            )
            dietary_habits = gr.Dropdown(
                ["Healthy", "Moderate", "Unhealthy"], 
                label="Dietary Habits"
            )
            family_history = gr.Radio(["Yes", "No"], label="Family History of Mental Illness")
            financial_stress = gr.Slider(1, 5, step=1, label="Financial Stress (1-5)")
            
    analyze_btn = gr.Button("Analyze Risk", variant="primary", size="lg")
    
    gr.Markdown("---")
    
    with gr.Row():
        with gr.Column():
            result_label = gr.Label(label="Analysis Results")
            resources_output = gr.Markdown(label="Resources")

            
    analyze_btn.click(
        fn=analyze_risk,
        inputs=[
            gender, age, academic_pressure, study_satisfaction, 
            study_hours, sleep_duration, dietary_habits, 
            family_history, financial_stress
        ],
        outputs=[result_label, resources_output]
    )

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Default(primary_hue="red", secondary_hue="pink"), share=True)
