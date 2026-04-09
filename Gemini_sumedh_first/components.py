import reflex as rx
from .state import State

def calc_button(label: str, action, color_scheme: str = "gray") -> rx.Component:
    """A generic calculator button."""
    return rx.button(
        label,
        on_click=action,
        color_scheme=color_scheme,
        size="4",
        width="100%",
        height="60px",
    )

def calculator_ui() -> rx.Component:
    """The full calculator UI."""
    return rx.vstack(
        # Calculator Display
        rx.box(
            rx.heading(
                State.display,
                size="8",
                text_align="right",
                padding_right="4",
                color=rx.color("accent", 11),
            ),
            width="100%",
            bg=rx.color("accent", 3),
            padding="4",
            border_radius="lg",
            margin_bottom="4",
        ),
        # Button Grid
        rx.grid(
            # Row 1
            calc_button("7", lambda: State.append_digit("7")),
            calc_button("8", lambda: State.append_digit("8")),
            calc_button("9", lambda: State.append_digit("9")),
            calc_button("/", lambda: State.set_operation("/"), "orange"),
            
            # Row 2
            calc_button("4", lambda: State.append_digit("4")),
            calc_button("5", lambda: State.append_digit("5")),
            calc_button("6", lambda: State.append_digit("6")),
            calc_button("*", lambda: State.set_operation("*"), "orange"),
            
            # Row 3
            calc_button("1", lambda: State.append_digit("1")),
            calc_button("2", lambda: State.append_digit("2")),
            calc_button("3", lambda: State.append_digit("3")),
            calc_button("-", lambda: State.set_operation("-"), "orange"),
            
            # Row 4
            calc_button("C", State.clear, "red"),
            calc_button("0", lambda: State.append_digit("0")),
            calc_button("=", State.calculate, "green"),
            calc_button("+", lambda: State.set_operation("+"), "orange"),
            
            columns="4",
            spacing="2",
            width="100%",
        ),
        padding="6",
        bg=rx.color("gray", 2),
        border_radius="xl",
        box_shadow="lg",
        width="350px",
    )
