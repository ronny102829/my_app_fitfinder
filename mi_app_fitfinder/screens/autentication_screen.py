import reflex as rx
@rx.page(route="/autentication")

def autentication() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.avatar(src="/ropa.jpeg", border_radius="50%", width="200px", height="200px", margin_top="20vh"),
            rx.text("fitfinder", font_family="Poppins", size="8", text_align="center",margin_top="4vh", color="orange"),
            rx.link(rx.button("Facebook",width="20vh", height="5vh",background_color="blue"),href="/umboarding",margin_top="5vh"),
            rx.link(rx.button("Google",width="18vh", height="5vh",background_color="green"),href="/umboarding",margin_top="2.8vh"),
             align_items="center"
        )
    )