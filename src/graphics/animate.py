class Animate:
    def __init__(self, sprites, num_per_direction=3):
        self.num_per_direction = num_per_direction

        self.down = sprites[:2]
        self.down_pos = 0

        self.left = sprites[3:5]
        self.left_pos = 0

        self.right = sprites[6:8]
        self.right_pos = 0

        self.up = sprites[9:11]
        self.up_pos = 0

    def get_down(self):
        self.down_pos += 1
        if self.down_pos == 3:
            self.down_pos = 0
        return self.down[self.down_pos - 1]

    def get_left(self):
        self.left_pos += 1
        if self.left_pos == 3:
            self.left_pos = 0
        return self.left[self.down_pos - 1]

    def get_right(self):
        self.right_pos += 1
        if self.right_pos == 3:
            self.right_pos = 0
        return self.right[self.right_pos - 1]

    def get_up(self):
        self.up_pos += 1
        if self.up_pos == 3:
            self.up_pos = 0
        return self.up[self.up_pos - 1]
