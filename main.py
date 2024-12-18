import arcade

from misc import button, scaler

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200


class Daily(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.width = int(width)
        self.height = int(height)
        self.button = button.Button
        self.scaler = scaler

    def setup(self):
        pass

    def on_draw(self):
        self.clear(arcade.color.ASH_GREY)
        self.button(
            "Begin",
            self.width // 2,
            self.height // 2,
            5,
            5,
            (255, 255, 255),
            (0, 0, 0),
            20,
            self.width,
            self.height,
        ).create_button()

    def update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass

    def on_resize(self, width, height):
        return super().on_resize(width, height)


def main():
    app = Daily(SCREEN_WIDTH, SCREEN_HEIGHT, "Daily")
    app.setup()
    arcade.run()


if __name__ == "__main__":
    main()
