import reflex as rx
@rx.page(route="/options")

def options() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.hstack(rx.link(rx.icon(tag="arrow-left"), href="/camera"),
            rx.text("ELIJE UN ESTILO",margin_left="7vh", size="5"),margin_top="5vh", margin_bottom="3vh"),
            rx.hstack(
                rx.vstack(rx.image(src="/ropa.jpeg",width="100px", height="100px"),rx.text("opcion1", text_align="center")),
                rx.vstack(rx.image(src="/ropa.jpeg",width="100px", height="100px"),rx.text("opcion1", text_align="center")),
                rx.vstack(rx.image(src="/ropa.jpeg",width="100px", height="100px"),rx.text("opcion1", text_align="center")),
                align_items="center"
                ),
                rx.hstack(
                rx.vstack(rx.image(src="/ropa.jpeg",width="100px", height="100px"),rx.text("opcion2", text_align="center")),
                rx.vstack(rx.image(src="/ropa.jpeg",width="100px", height="100px"),rx.text("opcion2", text_align="center")),
                rx.vstack(rx.image(src="/ropa.jpeg",width="100px", height="100px"),rx.text("opcion2", text_align="center")),
                align_items="center"
                ),
                rx.hstack(
                rx.vstack(rx.image(src="/ropa.jpeg",width="100px", height="100px"),rx.text("opcion3", text_align="center")),
                rx.vstack(rx.image(src="/ropa.jpeg",width="100px", height="100px"),rx.text("opcion3", text_align="center")),
                rx.vstack(rx.image(src="/ropa.jpeg",width="100px", height="100px"),rx.text("opcion3", text_align="center")),
                align_items="center"
                ),
            rx.link(rx.button("SIGUIENTE", width="20vh",margin_left="9.5vh", margin_top="7vh"), href="/details"),
            margin_left="4vh"
            ),
    )