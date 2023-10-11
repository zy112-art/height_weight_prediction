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
def predict_and_visualize_data(height, weight, gender):
    if gender == "男生":
        predict_data_visualize("男生", height, weight)
    elif gender == "女生":
        predict_data_visualize("女生", height, weight)
    return 'scatter_plot_2.png'

# 创建 Gradio 接口
gender_choice = gr.Radio(["男生", "女生"], label="性别", info="请选择性别")

gr.Interface(fn=visualize_data, inputs=gender_choice, outputs="image").launch()


# 创建 Gradio 接口
height = gr.Slider(50, 250, value=160.2, label="身高（厘米）", info="请选择介于50到250之间的数值")
weight = gr.Slider(10, 200, value=44.1, label="体重（千克）", info="请选择介于10到200之间的数值")
gender_choice = gr.Radio(["男生", "女生"], label="性别", info="请选择性别")

gr.Interface(fn=predict_and_visualize_data, inputs=[height, weight, gender_choice], outputs="image").launch()

