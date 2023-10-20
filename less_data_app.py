import gradio as gr
from utils import read_visualize_data, predict_data_visualize, predict_less_data_visualize, bmi_value

# try:
#     import gradio as gr
# except ImportError:
#     print("Package 'gradio' is not installed. Installing...")
#     import subprocess
#     subprocess.call(["pip", "install", "gradio"])
#     print("Package 'gradio' has been installed.")
#     # 重新尝试导入包
    
# 用于gradio公网代理服务和本机服务之间的网络代理通信
import subprocess
# 复制文件
copy_command = "cp teacher_project/utils/frpc_linux_amd64 /usr/local/envs/ssenv/lib/python3.9/site-packages/gradio/frpc_linux_amd64_v0.2"
subprocess.call(copy_command, shell=True)
# 赋予可执行权限
chmod_command = "chmod +x /usr/local/envs/ssenv/lib/python3.9/site-packages/gradio/frpc_linux_amd64_v0.2"
subprocess.call(chmod_command, shell=True)

# 第3个交互
def predict_and_visualize_data(height, weight, gender):
    if gender == "男生":
        image_1, p_1 = predict_datas_visualize("男生", height, weight)
        image_2, p_2 = predict_less_data_visualize("男生", height, weight)
    elif gender == "女生":
        image_1, p_1 = predict_data_visualize("女生", height, weight)
        image_2, p_2 = predict_less_data_visualize("女生", height, weight)
    bmi_v = bmi_value(height, weight, gender)
    # return [image_1, image_2]   
    return [bmi_v, p_1, p_2, image_1, image_2]

# 创建 Gradio 接口
with gr.Blocks() as demo:
    gr.Markdown(
    """
    ## 输入自己测量的**身高**、**体重**数据，尝试让人工智能模型来帮你**预测**对应水平等级吧！
    """)
    gender_choice = gr.Radio(["男生", "女生"], label="性别", info="请选择性别")
    height = gr.Slider(50, 250, value=160.2, label="身高（厘米）", info="请选择介于50到250之间的数值")
    weight = gr.Slider(10, 200, value=44.1, label="体重（千克）", info="请选择介于10到200之间的数值")

    # gr.Interface(fn=predict_and_visualize_data, inputs=[height, weight, gender_choice], outputs=["text","text","text", "image","image"])
    gr.Interface(fn=predict_and_visualize_data, inputs=[height, weight, gender_choice], outputs=[gr.Text("……" , label="对应BMI等级："), gr.Text("……" , label="模型1的预测值："), gr.Text("……" , label="模型2的预测值："), gr.Image(label="模型1预测可视化："),gr.Image(label="模型2预测可视化：")])

if __name__ == "__main__":
    demo.launch(share=True)

