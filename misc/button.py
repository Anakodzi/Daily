import arcade

from misc import scaler


class Button(arcade.Sprite):
    """A button module addon for arcade"""

    def __init__(
        self,
        center_x,
        center_y,
        width,
        height,
        screen_width,
        screen_height,
        filename=None,
        scale=1,
    ):
        super().__init__(filename, scale)
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.scaler = scaler
        self.pressed: bool

    def create_button(
        self,
        label: str,
        color,
        text_color,
        font_size,
    ):
        """Makes buttons possible by combining text and rectangle methods"""
        x = self.scaler.dynamic_width(self.screen_width, self.width)
        y = self.scaler.dynamic_height(self.screen_height, self.height)
        rect = arcade.draw_rectangle_filled(self.center_x, self.center_y, x, y, color)
        text = arcade.draw_text(
            label,
            self.center_x,
            self.center_y,
            text_color,
            anchor_x="center",
            anchor_y="center",
            font_size=self.scaler.dynamic_font(x, y, font_size),
        )
        return rect, text
