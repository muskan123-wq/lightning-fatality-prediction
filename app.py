import gradio as gr
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_csv("Machine_learning/datawarehouse/final_dataset.csv")
query = """
SELECT 
    f.deaths,
    l.intensity_value,
    sv.poverty_rate,
    sv.literacy_rate,
    sv.population,
    sv.forest_cover,
    sm.lightning_density
FROM fatalities f
JOIN lightning_intensity l 
    ON f.state_id = l.state_id AND f.year = l.year
JOIN static_variables sv 
    ON f.state_id = sv.state_id
LEFT JOIN state_metrics sm 
    ON f.state_id = sm.state_id AND f.year = sm.year
"""

df = df.dropna()

# ---- Features and target ----
X = df[['intensity_value','poverty_rate','literacy_rate',
        'population','forest_cover','lightning_density']]

y = df['deaths']

# ---- Train model ----
model = LinearRegression()
model.fit(X, y)

# ---- Prediction function ----
def predict(intensity, poverty, literacy, population, forest, density):
    input_data = np.array([[intensity, poverty, literacy, population, forest, density]])
    prediction = model.predict(input_data)[0]

    # Risk classification
    if prediction < 50:
        risk = "Low Risk"
    elif prediction < 200:
        risk = "Moderate Risk"
    else:
        risk = "High Risk"

    # Reasoning
    reasons = []

    if intensity > 150000:
        reasons.append("High lightning intensity increases exposure")
    if poverty > 20:
        reasons.append("Higher poverty increases vulnerability")
    if literacy < 70:
        reasons.append("Lower literacy reduces awareness and safety")
    if population > 30000000:
        reasons.append("Large population increases exposure")

    explanation = "\n".join([f"- {r}" for r in reasons]) if reasons else "No major risk factors detected."

    return f"""
##  Prediction Result

**Predicted Fatalities:** {prediction:.2f}  
**Risk Level:** {risk}

###  Key Factors:
{explanation}
"""

# ---- Sample Input Function ----
def load_sample():
    return 150000, 25, 65, 35000000, 30, 5

# ---- Gradio UI ----
with gr.Blocks() as demo:
    gr.Markdown("# Lightning Fatality Prediction System")
    gr.Markdown("Enter parameters or load a sample input to see prediction.")

    with gr.Row():
        intensity = gr.Number(label="Lightning Intensity", value=150000, info="Typical: 50,000 – 200,000")
        poverty = gr.Number(label="Poverty Rate (%)", value=20, info="Typical: 5 – 40")
        literacy = gr.Number(label="Literacy Rate (%)", value=75, info="Typical: 50 – 100")

    with gr.Row():
        population = gr.Number(label="Population", value=30000000, info="State population")
        forest = gr.Number(label="Forest Cover (%)", value=25, info="Typical: 10 – 50")
        density = gr.Number(label="Lightning Density", value=5, info="Strikes per km²")

    output = gr.Markdown()

    with gr.Row():
        predict_btn = gr.Button("🔍 Predict")
        sample_btn = gr.Button("⚡ Load Sample Input")

    predict_btn.click(
        predict,
        inputs=[intensity, poverty, literacy, population, forest, density],
        outputs=output
    )

    sample_btn.click(
        load_sample,
        outputs=[intensity, poverty, literacy, population, forest, density]
    )

demo.launch()