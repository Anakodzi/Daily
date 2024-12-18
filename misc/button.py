import arcade

from misc import scaler


class Button:
    """A button module addon for arcade"""

    def __init__(
        self,
        text: str,
        center_x,
        center_y,
        width,
        height,
        color,
        text_color,
        font_size,
        screen_width,
        screen_height,
    ):
        self.text = text
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.color = color
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.text_color = text_color
        self.font_size = font_size
        self.scaler = scaler

    def create_button(self):
        """Makes buttons possible by combining text and rectangle methods"""
        x = self.scaler.dynamic_width(self.screen_width, self.width)
        y = self.scaler.dynamic_height(self.screen_height, self.height)
        arcade.draw_rectangle_filled(self.center_x, self.center_y, x, y, self.color)
        arcade.draw_text(
            self.text,
            self.center_x,
            self.center_y,
            self.text_color,
            anchor_x="center",
            anchor_y="center",
            font_size=self.scaler.dynamic_font(x, y, self.font_size),
        )
