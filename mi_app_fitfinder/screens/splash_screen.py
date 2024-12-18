import reflex as rx
@rx.page(route="/splash")

def splash() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            rx.link(rx.avatar(src="/ropa.jpeg", width="200px", height="200px", border_radius="50%",margin_top="24vh"), href="/autentication"),
            rx.text("fitfinder", font_family="Poppins", size="8", text_align="center",margin_top="4vh",color="orange"),
            align_items="center",
        )
    )