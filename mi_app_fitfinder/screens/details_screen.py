import reflex as rx
@rx.page(route="/details")

def details() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.hstack(rx.link(rx.icon(tag="arrow-left", margin_left="3vh"), href="/options"),
            rx.text("BUENA OPCION",margin_left="9vh", size="5"),margin_top="5vh", margin_bottom="3vh"),
            rx.image(src="/ropa.jpeg",width="350px", height="200px", margin_left="2.3vh", border_radius="9%"),
            rx.text("DESCRIPCION", margin_top="3vh"),
            rx.text("""lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem
                     lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem
                     lorem lorem lorem lorem"""),
            rx.text("""lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem
                     lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem
                     lorem lorem lorem lorem"""),
            rx.link(rx.button("FINALIZADO", margin_top="7vh", margin_left="8vh", width="30vh"),href="/splash")
        )
    )