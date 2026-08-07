import os

import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager
from styles import CSS, JS, EXAMPLES, HEADER_HTML

load_dotenv(override=True)


async def run(query: str):
    async for status_update in ResearchManager().run(query):
        yield status_update


async def open_clarification(query: str):
    query = (query or "").strip()
    if not query:
        message = "Please enter a research question first."
        empty = gr.update(label="", value="")
        return gr.update(visible=False), message, empty, empty, empty

    try:
        result = await ResearchManager().clarify(query)
        questions = result.questions
    except Exception:
        questions = [
            "What scope, time period, or geography should the research cover?",
            "Who is the intended audience, and what decision should this support?",
            "Which comparisons, constraints, or sources matter most to you?",
        ]

    updates = [gr.update(label=f"{index}. {question}", value="") for index, question in enumerate(questions, 1)]
    return gr.update(visible=True), "Answer the questions below to sharpen the research brief.", *updates


async def run_refined(query: str, answer_one: str, answer_two: str, answer_three: str):
    clarifications = "\n".join(
        answer for answer in [answer_one, answer_two, answer_three] if (answer or "").strip()
    )
    async for status_update in ResearchManager().run(query, clarifications):
        yield gr.update(visible=False), status_update


with gr.Blocks(title="Deep Research") as ui:
    gr.HTML(HEADER_HTML)

    with gr.Row(elem_classes="dr-query-row"):
        query_textbox = gr.Textbox(
            placeholder="Type a research question...",
            show_label=False,
            container=False,
            autofocus=True,
            elem_id="dr-query",
            scale=5,
        )
        run_button = gr.Button("Investigate", variant="primary", elem_id="dr-run", scale=1)

    gr.HTML('<div class="dr-examples-label">Try one</div>')
    gr.Examples(examples=EXAMPLES, inputs=query_textbox, elem_id="dr-examples")

    report = gr.Markdown(elem_id="dr-report")

    with gr.Group(visible=False, elem_id="dr-clarify-modal") as clarification_modal:
        gr.Markdown("### Refine your research brief\nA few focused answers will help the agent search with better intent.", elem_id="dr-clarify-heading")
        clarification_note = gr.Markdown(elem_id="dr-clarify-note")
        with gr.Column(elem_id="dr-clarify-fields"):
            question_one = gr.Textbox(show_label=True, lines=2, elem_id="dr-question-1")
            question_two = gr.Textbox(show_label=True, lines=2, elem_id="dr-question-2")
            question_three = gr.Textbox(show_label=True, lines=2, elem_id="dr-question-3")
        refine_button = gr.Button("Begin refined research", variant="primary", elem_id="dr-refine")

    run_button.click(
        open_clarification,
        inputs=query_textbox,
        outputs=[clarification_modal, clarification_note, question_one, question_two, question_three],
    )
    query_textbox.submit(
        open_clarification,
        inputs=query_textbox,
        outputs=[clarification_modal, clarification_note, question_one, question_two, question_three],
    )
    refine_button.click(
        run_refined,
        inputs=[query_textbox, question_one, question_two, question_three],
        outputs=[clarification_modal, report],
    )


if __name__ == "__main__":
    ui.launch(
        server_name="0.0.0.0",
        server_port=int(os.getenv("PORT", "7860")),
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
    )
