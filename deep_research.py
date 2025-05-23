import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)

async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk

with gr.Blocks(theme=gr.themes.Default(primary_hue="gray")) as ui:
    gr.Markdown("# Deep Research")
    query_textbox = gr.Textbox(label="What would you like to research?")
    run_button = gr.Button("Run", variant="primary")
    output = gr.Markdown(label="Report")

    run_button.click(fn=run, inputs=query_textbox, outputs=output)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=output)

ui.launch(inbrowser=True)
