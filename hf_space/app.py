import evaluate
from evaluate.utils import launch_gradio_widget

module = evaluate.load("Etamin/tsed")
launch_gradio_widget(module)
