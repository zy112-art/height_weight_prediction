import gradio as gr
from utils import read_visualize_data, predict_data_visualize

# 第一个交互
def visualize_data(gender):
    if gender == "男生":
        read_visualize_data("男生")
    elif gender == "女生":
        read_visualize_data("女生")
    return 'scatter_plot_1.png'

# # 第二个交互
# def predict_and_visualize_data(height, weight, gender):
#     return predict_data_visualize(gender, height, weight)

iface = gr.Interface(
    fn=visualize_data,
    inputs=gr.inputs.Dropdown(['男生', '女生'], label="选择性别"),
    outputs="image"
)
iface.launch()

# iface2 = gr.Interface(
#     fn=predict_and_visualize_data,
#     inputs=[gr.inputs.Number(label="身高 (cm)"), gr.inputs.Number(label="体重 (kg)"),
#             gr.inputs.Dropdown(['男生', '女生'], label="性别")],
#     outputs="auto"
# )
# iface2.launch()
