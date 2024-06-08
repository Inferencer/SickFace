import gradio as gr
import os

def run_demo(input_image_path, driving_video_path, movement_scale):
    # Default paths for checkpoint and config
    checkpoint_path = "./checkpoints/vox256.pt"
    config_path = "./configs/vox256.yaml"
    
    # Construct the command to run demo.py with the correct options
    if movement_scale == "Relative":
        movement_scale_option = "--relative"
    elif movement_scale == "Absolute":
        movement_scale_option = "--absolute"
    else:
        raise ValueError("Invalid movement scale option")
    
    # Construct and execute the command
    command = f'python demo.py --checkpoint {checkpoint_path} --config {config_path} --source_image {input_image_path} --driving_video {driving_video_path} --source_idx 0 {movement_scale_option} --adapt_scale --find_best_frame'
    os.system(command)
    
    # Path to the result video
    result_video_path = "result.mp4"  # Replace with the actual output video path
    
    return result_video_path

def demo_ui(input_image_path, driving_video_path, movement_scale):
    # Run the demo and get the result video path
    result_video_path = run_demo(input_image_path, driving_video_path, movement_scale)
    
    return result_video_path

input_image = gr.Image(label="Upload Input Image (512x512)", type="filepath")
driving_video = gr.Video(label="Upload Driving Video (512x512)")
movement_scale_option = gr.Radio(["Relative", "Absolute"], label="Movement Scale", value="Relative")

with gr.Blocks() as demo_interface:
    with gr.Row():
        input_image.render()
        driving_video.render()
    movement_scale_option.render()
    generate_button = gr.Button("Generate")
    result_video = gr.Video(label="Result Video")
    
    generate_button.click(
        fn=demo_ui,
        inputs=[input_image, driving_video, movement_scale_option],
        outputs=result_video
    )

demo_interface.launch()
