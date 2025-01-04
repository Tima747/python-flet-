from flet import *
import flet

class MenuDetail(UserControl):
    def __init__(self):
        super().__init__()
        self.back_btn = Container(
            content=Icon(
                icons.ARROW_BACK_IOS_NEW_OUTLINED,
                size=30,
                color='#606060'
            ),
            padding=padding.all(5),
        )
        self.like_btn = Container(
            content=Icon(
                icons.FAVORITE_OUTLINE,
                size=30,
                color='#606060'
            ),
            padding=padding.all(5),
        )
        self.menu = Container(
            content=Row([
                self.back_btn,
                Text(
                    "Details",
                    size=16,
                    weight='w500',
                ),
                self.like_btn
                ], alignment='SpaceBetween'),
            height=60,
            #bgcolor='red',
            padding=padding.only(10, 20, 10, 0),
        )

    def build(self):
        return self.menu  # Возвращаем объект меню без вызова как функции

body = Container(
    content=Column([
        MenuDetail(),
        Container(
            Image(
                src='assets/foto_1.jpg',
                scale=0.8,
            )
        ),
        Container(
                Row([
                    Text(
                        "Domino train",
                        weight='w600',
                        size=20,
                    ),
                    Row([
                        Icon(
                            icons.STAR,
                            color='#67b19f',
                        ),
                        Text(
                            "4.8"
                        )
                    ],spacing=0)
            ],alignment='SpaceBetween'),
            padding=padding.only(20,-20,20,0)
        ),
        Container(
            Text(
                "The automatic domino train places dominoes evenly as it moves, making setup quick and fun for all ages."
            ),
            padding=padding.only(20, 0,20,0)
        ),
        Container(
            Row([
                Column([
                    Text('Price', color='#606060', size=14),
                    Text(
                        "$39,90",
                        size= 22,
                        weight='w600'
                    )
                ], spacing=0),
                ElevatedButton(
                    "Add to Cart",
                    style=ButtonStyle(
                        color='white',
                        bgcolor='#67b19f'
                    ),
                    height=50
                )
            ], alignment='spaceBetween'),
            padding=padding.only(20,0,10,0)
        )
    ]),
    gradient=LinearGradient(
        begin=alignment.top_left,
        end=alignment.bottom_right,
        colors=['#67b19f', 'white','white']
    ),
    width=360,
    height=640,
)

def manage(page: Page):
    page.window.max_width = 360  # Обновлено с учетом новых методов
    page.window.width = 360
    page.window.max_height = 640
    page.window.height = 640

    page.padding = 0
    page.add(body)

flet.app(target=manage)
