import gradio as gr
from markitdown import MarkItDown

# Initialize MarkItDown instance
markitdown = MarkItDown()


# Define file conversion function
def convert_to_markdown(file):
    result = markitdown.convert(file.name)
    return result.text_content


# Create Gradio interface with Blocks for layout control
with gr.Blocks() as demo:
    gr.Markdown("# File to Markdown Converter")
    file_input = gr.File(label="Upload File")
    markdown_output = gr.Textbox(label="Markdown Content", lines=20,
                                 placeholder="Converted markdown will appear here...")
    convert_button = gr.Button("Convert")

    # Define the interaction
    convert_button.click(
        fn=convert_to_markdown,
        inputs=file_input,
        outputs=markdown_output
    )

# Launch the app
if __name__ == "__main__":
    demo.launch()
