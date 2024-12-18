import reflex as rx
@rx.page(route="/umboarding")

def umboarding() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.link(rx.icon("arrow-left",margin_top="10px"),href="/autentication", margin_left="-40vh"),
            rx.text("bienvenido a fitfinder", font_family="Poppins", size="4", text_align="center",margin_top="1vh"),
             rx.text("una app que mejorara tu estilo", font_family="Poppins", size="4", text_align="center",margin_top="1vh"),
            rx.avatar(src="/ropa.jpeg", border_radius="50%", width="200px", height="200px", margin_top="4vh"),
            rx.text("fitfinder", font_family="Poppins", size="8", text_align="center",margin_top="4vh", color="orange"),
            rx.link(rx.button("SIGUIENTE",width="20vh", height="5vh",background_color="blue"),href="/camera",margin_top="12vh"),
             align_items="center"
        )
    )