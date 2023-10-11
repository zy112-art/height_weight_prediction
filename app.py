import gradio as gr
from utils import read_visualize_data, predict_data_visualize

# 第一个交互
def visualize_data(gender):
    if gender == "男生":
        read_visualize_data("男生")
    elif gender == "女生":
        read_visualize_data("女生")

iface = gr.Interface(
    fn=visualize_data,
    inputs=gr.inputs.Dropdown(['男生', '女生'], label="选择性别"),
    outputs="auto"
)
iface.launch()

