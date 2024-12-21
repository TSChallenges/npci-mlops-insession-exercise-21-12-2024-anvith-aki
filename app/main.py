import re
import joblib
import gradio
import gradio as gr
import numpy as np
import pandas as pd


# Load model
# Load model
model_path = "app/model/iris_model.pkl"
trained_model = joblib.load(model_path)


# UI - Input components
inputs = [
    gr.Number(label="Sepal Length (cm)"),
    gr.Number(label="Sepal Width (cm)"),
    gr.Number(label="Petal Length (cm)"),
    gr.Number(label="Petal Width (cm)")
]

# UI - Output component
output = gr.Textbox(label="Predicted Iris Species")



# Label prediction function
def get_output_label(sepal_length, sepal_width, petal_length, petal_width):
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = trained_model.predict(data)[0]
    return ['Setosa', 'Versicolor', 'Virginica'][prediction]


# Create Gradio interface object
# Create Gradio interface
iface = gr.Interface(
    fn=get_output_label,
    inputs=inputs,
    outputs=output
)

# Launch gradio interface
# set server_name = "0.0.0.0" and server_port = 7860 while launching it inside container.
# default server_name = "127.0.0.1", and server_port = 7860

iface.launch(server_name = "0.0.0.0", server_port = 7860)