import reflex as rx
@rx.page(route="/camera")

def camera() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.hstack(
                rx.icon(tag="user", width="50px", height="50px", margin_left="31vh", margin_top="3vh"),
                rx.icon(tag="bell", width="50px", height="50px", margin_top="3vh")
                ),
            rx.image(src="/ropa.jpeg", width="360px", height="540px", margin_left="2vh"),
            rx.hstack(
            rx.link(rx.icon(tag="arrow-left", margin_left="3vh", margin_top="4vh"), href="/umboarding"),
            rx.link(rx.icon(tag="loader", margin_left="15vh", margin_top="4vh"), href="/options")),
            )
        )