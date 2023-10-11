import gradio as gr
from utils import read_visualize_data, predict_data_visualize

# 第一个交互
def visualize_data(gender):
    if gender == "男生":
        read_visualize_data("男生")
    elif gender == "女生":
        read_visualize_data("女生")
    return 'scatter_plot_1.png'

# 创建 Gradio 接口
markdown_txt = gr.Markdown("## 选择**性别**，查看小学四年级学生体测数据分布！")
gender_choice = gr.Radio(["男生", "女生"], label="性别", info="请选择性别")

gr.Interface(fn=visualize_data, inputs=[markdown_txt, gender_choice], outputs="image").launch()
