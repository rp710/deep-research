EXAMPLES = [
    "Most popular AI Agent frameworks in 2026",
    "Most commercially successful Agentic AI implementations in 2026",
    "Celebrities who don't like cheese",
]

HEADER_HTML = """
<div class="dr-brand">
    <div class="dr-mark">
        <span class="dr-bar dr-bar-1"></span>
        <span class="dr-bar dr-bar-2"></span>
        <span class="dr-bar dr-bar-3"></span>
    </div>
    <div class="dr-titles">
        <h1>Deep<span class="dr-sep">/</span>Research</h1>
        <p>Multi-search web investigation</p>
    </div>
</div>
"""

CSS = """
.gradio-container {
    --dr-bg: #080b12;
    --dr-surface: #111722;
    --dr-line: #dce7f7;
    --dr-line-soft: #293548;
    --dr-text: #e9f0fb;
    --dr-muted: #8d9ab0;
    --dr-amber: #8ee7ff;
    --dr-blue: #6f8cff;
    --dr-purple: #b28cff;

    max-width: 1180px !important;
    margin: 0 auto !important;
    padding: 2.75rem 2rem 5rem !important;
    background: transparent !important;
    color: var(--dr-text) !important;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
}

.gradio-container.dark,
.dark .gradio-container,
body.dark .gradio-container,
html.dark .gradio-container {
    --dr-bg: #0b0b0c;
    --dr-surface: #161618;
    --dr-line: #f1f1ec;
    --dr-line-soft: #2a2a2d;
    --dr-text: #f1f1ec;
    --dr-muted: #8a8a8e;
}

body {
    background:
        radial-gradient(ellipse at 50% -15%, rgba(111, 140, 255, .20), transparent 44rem),
        radial-gradient(ellipse at 100% 65%, rgba(178, 140, 255, .08), transparent 30rem),
        var(--dr-bg, #080b12) !important;
}

/* === HEADER === */
.dr-brand {
    display: grid;
    grid-template-columns: auto 1fr;
    align-items: center;
    gap: 1.25rem;
    padding: 1.5rem 0 1.35rem;
    border: 0;
    border-bottom: 1px solid var(--dr-line-soft);
    margin-bottom: 3rem;
    background: transparent;
    position: relative;
}

.dr-brand::after {
    content: "AI RESEARCH SYSTEM  /  ONLINE";
    position: absolute;
    right: 1.4rem;
    bottom: .65rem;
    color: var(--dr-amber);
    font: 700 .6rem/1 ui-monospace, SFMono-Regular, Menlo, monospace;
    letter-spacing: .18em;
}

.dr-mark {
    display: flex;
    flex-direction: column;
    gap: 5px;
    width: 38px;
}

.dr-bar { height: 6px; display: block; border-radius: 99px; }
.dr-bar-1 { background: var(--dr-amber);  width: 100%; }
.dr-bar-2 { background: var(--dr-blue);   width: 70%;  }
.dr-bar-3 { background: var(--dr-purple); width: 45%;  }

.dr-titles h1 {
    font-size: clamp(2.2rem, 5vw, 4.4rem);
    font-weight: 750;
    letter-spacing: -0.065em;
    margin: 0;
    line-height: 0.92;
    text-transform: uppercase;
    color: var(--dr-text);
}

.dr-sep {
    color: var(--dr-blue);
    font-weight: 300;
    margin: 0 0.04em;
}

.dr-titles p {
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
    font-size: 0.65rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    margin: 0.55rem 0 0;
    color: var(--dr-muted);
}

/* === QUERY ROW === */
.dr-query-row {
    gap: 0 !important;
    align-items: stretch !important;
}

#dr-query, #dr-query > div, #dr-query .wrap, #dr-query .form, #dr-query .block {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    border-radius: 0 !important;
}

#dr-query textarea, #dr-query input {
    background: var(--dr-surface) !important;
    color: var(--dr-text) !important;
    border: 1px solid var(--dr-line-soft) !important;
    border-radius: 12px !important;
    padding: 1.15rem 1.25rem !important;
    font-size: 1.05rem !important;
    font-family: inherit !important;
    box-shadow: 0 16px 35px rgba(0, 0, 0, .22) !important;
    line-height: 1.45 !important;
    resize: none !important;
    min-height: 56px !important;
    transition: border-color 0.15s, box-shadow 0.15s !important;
}

#dr-query textarea:focus, #dr-query input:focus {
    outline: none !important;
    border-color: var(--dr-blue) !important;
    box-shadow: 0 0 0 3px rgba(111, 140, 255, .20), 0 16px 35px rgba(0, 0, 0, .22) !important;
}

#dr-query textarea::placeholder, #dr-query input::placeholder {
    color: var(--dr-muted) !important;
    opacity: 1 !important;
}

#dr-run {
    background: var(--dr-blue) !important;
    color: #ffffff !important;
    border: 1px solid var(--dr-blue) !important;
    border-left: 0 !important;
    border-radius: 0 12px 12px 0 !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.14em !important;
    font-size: 0.85rem !important;
    box-shadow: 0 16px 35px rgba(0, 0, 0, .22) !important;
    transition: background 0.15s, color 0.15s, transform 0.08s, box-shadow 0.15s !important;
    min-width: 150px !important;
    padding: 1rem 1.5rem !important;
}

#dr-run:hover {
    background: #849cff !important;
    color: #ffffff !important;
    box-shadow: 0 12px 28px rgba(111, 140, 255, .28) !important;
}

#dr-run:active { transform: translate(2px, 2px) !important; }

/* === EXAMPLES === */
.dr-examples-label {
    font-family: ui-monospace, SFMono-Regular, monospace;
    font-size: 0.65rem;
    letter-spacing: 0.28em;
    color: var(--dr-amber);
    text-transform: uppercase;
    margin: 2.75rem 0 0.85rem 0;
    display: flex;
    align-items: center;
    gap: 0.85rem;
}

.dr-examples-label::after {
    content: "";
    flex: 1;
    height: 1px;
    background: var(--dr-line-soft);
}

#dr-examples, #dr-examples > div, #dr-examples .wrap, #dr-examples .block {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    box-shadow: none !important;
}

#dr-examples label, #dr-examples .label-wrap, #dr-examples > div > .label-wrap {
    display: none !important;
}

#dr-examples table {
    border-collapse: separate !important;
    border-spacing: 0 !important;
    width: auto !important;
    background: transparent !important;
    border: none !important;
}

#dr-examples thead { display: none !important; }

#dr-examples tbody { background: transparent !important; }

#dr-examples tr {
    background: transparent !important;
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
    border: none !important;
}

#dr-examples td, #dr-examples button {
    background: var(--dr-surface) !important;
    border: 1px solid var(--dr-line-soft) !important;
    padding: 0.7rem 1.05rem !important;
    cursor: pointer !important;
    transition: border-color 0.15s, color 0.15s, transform 0.1s !important;
    font-size: 0.9rem !important;
    color: var(--dr-text) !important;
    border-radius: 9px !important;
    margin: 0 !important;
    text-align: left !important;
    box-shadow: none !important;
}

#dr-examples td:hover, #dr-examples button:hover {
    border-color: var(--dr-purple) !important;
    color: var(--dr-purple) !important;
    transform: translateY(-1px);
    background: #1a2435 !important;
    box-shadow: 0 8px 20px rgba(0, 0, 0, .18) !important;
}

/* === REPORT === */
#dr-report {
    margin-top: 2.5rem !important;
    padding: 2rem 2.25rem !important;
    background: var(--dr-surface) !important;
    border: 1px solid var(--dr-line-soft) !important;
    border-radius: 14px !important;
    box-shadow: 0 22px 48px rgba(0, 0, 0, .20) !important;
    color: var(--dr-text) !important;
    min-height: 40px;
}

#dr-report > div, #dr-report .prose {
    background: transparent !important;
    color: var(--dr-text) !important;
}

#dr-report:not(:empty) {
    border-top: 1px solid var(--dr-line-soft) !important;
}

#dr-report h1 {
    font-size: clamp(2rem, 4vw, 3.1rem);
    font-weight: 900;
    color: var(--dr-text);
    border-bottom: 1px solid var(--dr-line-soft);
    padding-bottom: 0.45rem;
    margin: 1.5rem 0 1rem;
    letter-spacing: -0.025em;
}

#dr-report h2 {
    font-size: 1.35rem;
    color: var(--dr-amber);
    font-weight: 800;
    margin-top: 1.75rem;
    letter-spacing: -0.015em;
}

#dr-report h3 {
    font-size: 1.1rem;
    color: var(--dr-text);
    font-weight: 800;
    margin-top: 1.5rem;
}

#dr-report p { line-height: 1.7; }

#dr-report a {
    color: var(--dr-blue);
    text-decoration: underline;
    text-decoration-thickness: 2px;
    text-underline-offset: 3px;
}

#dr-report a:hover { color: var(--dr-amber); }

#dr-report code {
    background: var(--dr-surface);
    border: 1px solid var(--dr-line-soft);
    padding: 0.1rem 0.4rem;
    font-size: 0.92em;
    border-radius: 0;
}

#dr-report pre {
    background: var(--dr-surface);
    border: 1.5px solid var(--dr-line-soft);
    border-radius: 0;
    padding: 1rem 1.25rem;
}

#dr-report blockquote {
    border-left: 4px solid var(--dr-blue) !important;
    background: #182235;
    padding: 1rem 1.25rem;
    margin: 1rem 0;
    color: #c9d6e9;
}

#dr-report ul, #dr-report ol { padding-left: 1.5rem; }
#dr-report li { margin: 0.3rem 0; line-height: 1.6; }

#dr-report table {
    border-collapse: collapse;
    border: 1.5px solid var(--dr-line);
}

#dr-report th, #dr-report td {
    border: 1px solid var(--dr-line-soft);
    padding: 0.5rem 0.85rem;
    text-align: left;
}

#dr-report th {
    background: var(--dr-surface);
    font-weight: 800;
    color: var(--dr-blue);
}

/* === CLARIFICATION MODAL === */
#dr-clarify-modal {
    position: fixed !important;
    inset: 0 !important;
    z-index: 1000 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 1.5rem !important;
    background: rgba(3, 6, 12, .72) !important;
    backdrop-filter: blur(12px) !important;
}

#dr-clarify-modal > div {
    width: min(640px, 100%) !important;
    max-height: min(760px, calc(100vh - 3rem)) !important;
    overflow-y: auto !important;
    padding: 2rem !important;
    border: 1px solid #34435e !important;
    border-radius: 18px !important;
    background: #111722 !important;
    box-shadow: 0 30px 90px rgba(0, 0, 0, .45) !important;
}

#dr-clarify-heading h3 {
    margin: 0 !important;
    color: #edf4ff !important;
    font-size: 1.65rem !important;
    letter-spacing: -.035em !important;
}

#dr-clarify-note {
    margin: .4rem 0 1.35rem !important;
    color: #9eabc0 !important;
}

#dr-clarify-fields {
    gap: .85rem !important;
}

#dr-clarify-fields textarea {
    min-height: 68px !important;
    border: 1px solid #34435e !important;
    border-radius: 10px !important;
    background: #0b1019 !important;
    color: #edf4ff !important;
    box-shadow: none !important;
}

#dr-clarify-fields textarea:focus {
    border-color: var(--dr-blue) !important;
    box-shadow: 0 0 0 3px rgba(111, 140, 255, .18) !important;
}

#dr-clarify-fields .label-wrap {
    color: #dce7f7 !important;
    font-size: .84rem !important;
    line-height: 1.35 !important;
}

#dr-refine {
    width: 100% !important;
    margin-top: 1.35rem !important;
    border-radius: 10px !important;
}

footer { display: none !important; }

@media (max-width: 700px) {
    .gradio-container { padding: 1.5rem 1rem 3rem !important; }
    .dr-brand { padding: 1.35rem 0 1.8rem; margin-bottom: 2.5rem; }
    .dr-brand::after { right: 1rem; }
    .dr-query-row { flex-direction: column !important; }
    #dr-run {
        border-left: 1px solid var(--dr-blue) !important;
        border-top: 0 !important;
        border-radius: 12px !important;
        width: 100% !important;
    }
    #dr-clarify-modal { padding: .75rem !important; }
    #dr-clarify-modal > div { padding: 1.25rem !important; max-height: calc(100vh - 1.5rem) !important; }
}
"""

JS = """
() => {
    const focus = () => {
        const el = document.querySelector("#dr-query textarea, #dr-query input");
        if (el) { el.focus(); return true; }
        return false;
    };
    if (!focus()) {
        let tries = 0;
        const i = setInterval(() => {
            if (focus() || ++tries > 20) clearInterval(i);
        }, 100);
    }
}
"""
