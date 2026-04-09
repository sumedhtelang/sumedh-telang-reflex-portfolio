import reflex as rx

def counter_component() -> rx.Component:
    """A simple counter component."""
    from Gemini_sumedh_first.state import State
    return rx.hstack(
        rx.button(
            "Decrement",
            on_click=State.decrement,
            color_scheme="red",
        ),
        rx.heading(State.count, size="5"),
        rx.button(
            "Increment",
            on_click=State.increment,
            color_scheme="green",
        ),
        spacing="4",
        align="center",
    )
