import reflex as rx
from .components import calculator_ui

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Reflex Calculator", size="9"),
            calculator_ui(),
            spacing="5",
            align="center",
            min_height="85vh",
        ),
        padding_top="50px",
    )

app = rx.App()
app.add_page(index)
