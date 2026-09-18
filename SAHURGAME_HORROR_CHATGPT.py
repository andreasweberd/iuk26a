
import tkinter as tk
import math
import time
from collections import deque

# ============================================================
# TUNG TUNG TUNG SAHUR - NIGHTMARE MAZE
# Tkinter raycast 3D game
# ============================================================

SCREEN_W = 1000
SCREEN_H = 650

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 220
MAX_DEPTH = 20

MOVE_SPEED = 2.8
TURN_SPEED = 2.2

# TTT SAHUR IS NOW 3 TIMES AS FAST!
NPC_SPEED = 1.35 * 3

NPC_UPDATE = 0.20

MAP = [
    "####################",
    "#P.....#...........#",
    "#.####.#.#########.#",
    "#....#.#.#.......#.#",
    "####.#.#.#.#####.#.#",
    "#....#...#.#...#.#.#",
    "#.########.#.#.#.#.#",
    "#..........#.#...#.#",
    "#.##########.#####.#",
    "#.#........#......#",
    "#.#.######.######.#",
    "#.#......#........#",
    "#.######.########.#",
    "#.................E#",
    "####################",
]

PLAYER_START = None
EXIT = None

for y, row in enumerate(MAP):
    for x, cell in enumerate(row):
        if cell == "P":
            PLAYER_START = (x + 0.5, y + 0.5)
        elif cell == "E":
            EXIT = (x + 0.5, y + 0.5)

NPC_START = (17.5, 11.5)

WALL_COLORS = [
    "#583c67",
    "#65456f",
    "#493354",
    "#785080",
]


# ============================================================
# GAME
# ============================================================

class TungTungMaze:

    def __init__(self, root):

        self.root = root
        self.root.title(
            "TUNG TUNG TUNG SAHUR - DAS HORRORSPIEL"
        )
        self.root.configure(bg="#08080c")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            root,
            width=SCREEN_W,
            height=SCREEN_H,
            bg="#08080c",
            highlightthickness=0
        )
        self.canvas.pack()

        self.keys = set()

        self.running = True
        self.dead = False
        self.won = False

        self.last_time = time.perf_counter()
        self.npc_timer = 0

        self.npc_path = []
        self.npc_path_index = 0

        # Flashlight
        self.flashlight = True
        self.flashlight_range = 16.0
        self.flashlight_fov = math.pi / 4

        # Small screen effects
        self.message = ""
        self.message_timer = 0

        self.reset()

        root.bind("<KeyPress>", self.key_down)
        root.bind("<KeyRelease>", self.key_up)

        root.bind("<Escape>", lambda e: root.destroy())

        self.canvas.focus_set()

        self.loop()

    # ========================================================
    # RESET
    # ========================================================

    def reset(self):

        self.px, self.py = PLAYER_START

        self.angle = 0.0

        self.nx, self.ny = NPC_START

        self.npc_path = []
        self.npc_path_index = 0
        self.npc_timer = 0

        self.dead = False
        self.won = False

        self.flashlight = True

        self.message = ""
        self.message_timer = 0

        self.start_time = time.perf_counter()

    # ========================================================
    # INPUT
    # ========================================================

    def key_down(self, event):

        key = event.keysym.lower()

        if key == "f1":
            self.reset()
            return

        if self.dead or self.won:

            if key in ("r", "return", "space"):
                self.reset()

            return

        # Toggle flashlight
        if key == "f":
            self.flashlight = not self.flashlight
            return

        self.keys.add(key)

    def key_up(self, event):

        self.keys.discard(event.keysym.lower())

    # ========================================================
    # COLLISION
    # ========================================================

    def is_wall(self, x, y):

        ix = int(x)
        iy = int(y)

        if iy < 0 or iy >= len(MAP):
            return True

        if ix < 0 or ix >= len(MAP[iy]):
            return True

        return MAP[iy][ix] == "#"

    def can_move(self, x, y, radius=0.18):

        checks = [
            (x, y),
            (x + radius, y),
            (x - radius, y),
            (x, y + radius),
            (x, y - radius),
        ]

        return all(
            not self.is_wall(a, b)
            for a, b in checks
        )

    # ========================================================
    # PLAYER
    # ========================================================

    def update_player(self, dt):

        if self.dead or self.won:
            return

        move_x = 0
        move_y = 0

        if "w" in self.keys or "up" in self.keys:

            move_x += math.cos(self.angle)
            move_y += math.sin(self.angle)

        if "s" in self.keys or "down" in self.keys:

            move_x -= math.cos(self.angle)
            move_y -= math.sin(self.angle)

        if "a" in self.keys:

            move_x += math.cos(
                self.angle - math.pi / 2
            )

            move_y += math.sin(
                self.angle - math.pi / 2
            )

        if "d" in self.keys:

            move_x += math.cos(
                self.angle + math.pi / 2
            )

            move_y += math.sin(
                self.angle + math.pi / 2
            )

        if "left" in self.keys or "q" in self.keys:
            self.angle -= TURN_SPEED * dt

        if "right" in self.keys or "e" in self.keys:
            self.angle += TURN_SPEED * dt

        length = math.sqrt(
            move_x * move_x + move_y * move_y
        )

        if length > 0:

            move_x /= length
            move_y /= length

            speed = MOVE_SPEED * dt

            nx = self.px + move_x * speed
            ny = self.py + move_y * speed

            if self.can_move(nx, self.py):
                self.px = nx

            if self.can_move(self.px, ny):
                self.py = ny

        # Exit
        if math.dist(
            (self.px, self.py),
            EXIT
        ) < 0.55:

            self.won = True

    # ========================================================
    # BFS PATHFINDING
    # ========================================================

    def get_neighbors(self, cell):

        x, y = cell

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if (
                0 <= ny < len(MAP)
                and 0 <= nx < len(MAP[ny])
                and MAP[ny][nx] != "#"
            ):
                yield (nx, ny)

    def bfs(self, start, goal):

        start = (
            int(start[0]),
            int(start[1])
        )

        goal = (
            int(goal[0]),
            int(goal[1])
        )

        queue = deque([start])
        came_from = {start: None}

        while queue:

            current = queue.popleft()

            if current == goal:
                break

            for neighbor in self.get_neighbors(current):

                if neighbor not in came_from:

                    came_from[neighbor] = current
                    queue.append(neighbor)

        if goal not in came_from:
            return []

        path = []

        current = goal

        while current is not None:

            path.append(current)
            current = came_from[current]

        path.reverse()

        return path

    # ========================================================
    # NPC MOVEMENT
    # ========================================================

    def update_npc(self, dt):

        if self.dead or self.won:
            return

        self.npc_timer -= dt

        if self.npc_timer <= 0:

            self.npc_timer = NPC_UPDATE

            self.npc_path = self.bfs(
                (self.nx, self.ny),
                (self.px, self.py)
            )

            self.npc_path_index = 1

        if len(self.npc_path) > 1:

            target_cell = self.npc_path[
                min(
                    self.npc_path_index,
                    len(self.npc_path) - 1
                )
            ]

            tx = target_cell[0] + 0.5
            ty = target_cell[1] + 0.5

            dx = tx - self.nx
            dy = ty - self.ny

            distance = math.sqrt(
                dx * dx + dy * dy
            )

            if distance < 0.12:

                self.npc_path_index += 1

            elif distance > 0:

                dx /= distance
                dy /= distance

                # 3x SPEED
                speed = NPC_SPEED * dt

                nx = self.nx + dx * speed
                ny = self.ny + dy * speed

                if self.can_move(nx, self.ny, 0.15):
                    self.nx = nx

                if self.can_move(self.nx, ny, 0.15):
                    self.ny = ny

        # INSTANT DEATH
        if math.dist(
            (self.px, self.py),
            (self.nx, self.ny)
        ) < 0.42:

            self.die()

    # ========================================================
    # RAYCAST
    # ========================================================

    def cast_ray(self, ray_angle):

        ray_angle %= math.tau

        ray_dir_x = math.cos(ray_angle)
        ray_dir_y = math.sin(ray_angle)

        map_x = int(self.px)
        map_y = int(self.py)

        delta_dist_x = (
            abs(1 / ray_dir_x)
            if abs(ray_dir_x) > 1e-9
            else 1e30
        )

        delta_dist_y = (
            abs(1 / ray_dir_y)
            if abs(ray_dir_y) > 1e-9
            else 1e30
        )

        if ray_dir_x < 0:

            step_x = -1

            side_dist_x = (
                self.px - map_x
            ) * delta_dist_x

        else:

            step_x = 1

            side_dist_x = (
                map_x + 1.0 - self.px
            ) * delta_dist_x

        if ray_dir_y < 0:

            step_y = -1

            side_dist_y = (
                self.py - map_y
            ) * delta_dist_y

        else:

            step_y = 1

            side_dist_y = (
                map_y + 1.0 - self.py
            ) * delta_dist_y

        side = 0

        for _ in range(100):

            if side_dist_x < side_dist_y:

                side_dist_x += delta_dist_x
                map_x += step_x
                side = 0

            else:

                side_dist_y += delta_dist_y
                map_y += step_y
                side = 1

            if self.is_wall(map_x, map_y):

                if side == 0:

                    distance = (
                        map_x - self.px
                        + (1 - step_x) / 2
                    ) / ray_dir_x

                else:

                    distance = (
                        map_y - self.py
                        + (1 - step_y) / 2
                    ) / ray_dir_y

                return (
                    max(0.001, distance),
                    side,
                    map_x,
                    map_y
                )

        return MAX_DEPTH, 0, map_x, map_y

    # ========================================================
    # FLASHLIGHT LIGHTING
    # ========================================================

    def flashlight_factor(self, ray_angle, distance):

        if not self.flashlight:
            return 0.08

        relative = (
            (ray_angle - self.angle + math.pi)
            % math.tau
        ) - math.pi

        # Light cone
        if abs(relative) > self.flashlight_fov / 2:
            return 0.10

        # Strong beam in front
        beam = max(
            0.0,
            1.0 - abs(relative)
            / (self.flashlight_fov / 2)
        )

        falloff = max(
            0.0,
            1.0 - distance
            / self.flashlight_range
        )

        return 0.4 + beam * falloff * 1.0

    def shade_color(self, color, factor):

        color = color.lstrip("#")

        r = int(int(color[0:2], 16) * factor)
        g = int(int(color[2:4], 16) * factor)
        b = int(int(color[4:6], 16) * factor)

        return "#{:02x}{:02x}{:02x}".format(
            max(0, min(255, r)),
            max(0, min(255, g)),
            max(0, min(255, b))
        )

    # ========================================================
    # DRAW 3D
    # ========================================================

    def draw_3d(self):

        self.canvas.create_rectangle(
            0, 0,
            SCREEN_W,
            SCREEN_H // 2,
            fill="#111321",
            outline=""
        )

        self.canvas.create_rectangle(
            0,
            SCREEN_H // 2,
            SCREEN_W,
            SCREEN_H,
            fill="#17121b",
            outline=""
        )

        strip_w = SCREEN_W / NUM_RAYS

        for ray in range(NUM_RAYS):

            ray_angle = (
                self.angle - HALF_FOV
                + FOV * ray / NUM_RAYS
            )

            distance, side, mx, my = self.cast_ray(
                ray_angle
            )

            corrected = distance * math.cos(
                ray_angle - self.angle
            )

            corrected = max(0.001, corrected)

            wall_height = min(
                SCREEN_H * 2,
                SCREEN_H / corrected
            )

            top = (
                SCREEN_H / 2
                - wall_height / 2
            )

            bottom = (
                SCREEN_H / 2
                + wall_height / 2
            )

            # FLASHLIGHT ILLUMINATION
            light = self.flashlight_factor(
                ray_angle,
                corrected
            )

            shade = max(
                0.10,
                min(1.0, light)
            )

            if side == 1:
                shade *= 0.72

            base = WALL_COLORS[
                (mx * 3 + my * 5)
                % len(WALL_COLORS)
            ]

            color = self.shade_color(
                base,
                shade
            )

            x1 = int(ray * strip_w)
            x2 = int((ray + 1) * strip_w) + 1

            self.canvas.create_rectangle(
                x1,
                int(top),
                x2,
                int(bottom),
                fill=color,
                outline=""
            )

        self.draw_npc()
        self.draw_flashlight_overlay()
        self.draw_hud()

    # ========================================================
    # FLASHLIGHT OVERLAY
    # ========================================================

    def draw_flashlight_overlay(self):

        if not self.flashlight:
            return

        cx = SCREEN_W // 2
        cy = SCREEN_H // 2

        # Subtle flashlight glow around crosshair
        self.canvas.create_oval(
            cx - 20,
            cy - 20,
            cx + 20,
            cy + 20,
            outline="#e8e0c2",
            width=1
        )

    # ========================================================
    # NPC
    # BROWN RECTANGLE + RED EYES
    # ========================================================

    def draw_npc(self):

        dx = self.nx - self.px
        dy = self.ny - self.py

        distance = math.sqrt(
            dx * dx + dy * dy
        )

        if distance < 0.1:
            return

        angle_to_npc = math.atan2(dy, dx)

        relative = (
            (angle_to_npc - self.angle + math.pi)
            % math.tau
        ) - math.pi

        if abs(relative) > HALF_FOV + 0.15:
            return

        wall_distance, _, _, _ = self.cast_ray(
            angle_to_npc
        )

        if wall_distance < distance - 0.1:
            return

        corrected = distance * math.cos(relative)

        if corrected <= 0:
            return

        screen_x = (
            SCREEN_W / 2
            + math.tan(relative)
            / math.tan(HALF_FOV)
            * SCREEN_W / 2
        )

        height = min(
            650,
            SCREEN_H / corrected * 0.82
        )

        width = height * 0.55

        left = screen_x - width / 2
        right = screen_x + width / 2

        bottom = SCREEN_H / 2 + height / 2
        top = bottom - height

        # ====================================================
        # SIMPLE TTT SAHUR
        # Brown rectangular body
        # ====================================================

        self.canvas.create_rectangle(
            left,
            top,
            right,
            bottom,
            fill="#713d24",
            outline="#2b160d",
            width=4
        )

        # Darker bottom strip
        self.canvas.create_rectangle(
            left,
            bottom - height * 0.08,
            right,
            bottom,
            fill="#4a2417",
            outline=""
        )

        # Red glowing eyes
        eye_y = top + height * 0.28

        eye_w = max(4, width * 0.13)
        eye_h = max(4, height * 0.055)

        eye_left_x = screen_x - width * 0.22
        eye_right_x = screen_x + width * 0.22

        # Eye glow
        self.canvas.create_oval(
            eye_left_x - eye_w * 1.8,
            eye_y - eye_h * 1.8,
            eye_left_x + eye_w * 1.8,
            eye_y + eye_h * 1.8,
            fill="#4d0b0b",
            outline=""
        )

        self.canvas.create_oval(
            eye_right_x - eye_w * 1.8,
            eye_y - eye_h * 1.8,
            eye_right_x + eye_w * 1.8,
            eye_y + eye_h * 1.8,
            fill="#4d0b0b",
            outline=""
        )

        # Actual red eyes
        self.canvas.create_rectangle(
            eye_left_x - eye_w,
            eye_y - eye_h,
            eye_left_x + eye_w,
            eye_y + eye_h,
            fill="#ff1717",
            outline="#ff5555",
            width=1
        )

        self.canvas.create_rectangle(
            eye_right_x - eye_w,
            eye_y - eye_h,
            eye_right_x + eye_w,
            eye_y + eye_h,
            fill="#ff1717",
            outline="#ff5555",
            width=1
        )

    # ========================================================
    # HUD
    # ========================================================

    def draw_hud(self):

        cx = SCREEN_W // 2
        cy = SCREEN_H // 2

        # Crosshair
        self.canvas.create_line(
            cx - 8,
            cy,
            cx + 8,
            cy,
            fill="#d5d5d5",
            width=1
        )

        self.canvas.create_line(
            cx,
            cy - 8,
            cx,
            cy + 8,
            fill="#d5d5d5",
            width=1
        )

        distance = math.dist(
            (self.px, self.py),
            (self.nx, self.ny)
        )

        danger = max(
            0,
            1 - distance / 6
        )

        if danger > 0:

            width = max(
                2,
                int(danger * 15)
            )

            self.canvas.create_rectangle(
                width // 2,
                width // 2,
                SCREEN_W - width // 2,
                SCREEN_H - width // 2,
                outline="#8c151f",
                width=width
            )

        # Title
        self.canvas.create_text(
            20,
            18,
            anchor="nw",
            text="TUNG TUNG TUNG SAHUR SUCHT DICH...",
            fill="#ef5966",
            font=("Consolas", 17, "bold")
        )

        # Controls
        self.canvas.create_text(
            20,
            45,
            anchor="nw",
            text="WASD: BEWEGEN   ARROWS/QE: DREHEN   F: TASCHENLAMPE",
            fill="#b8aab8",
            font=("Consolas", 10)
        )

        # Threat
        self.canvas.create_text(
            SCREEN_W - 20,
            20,
            anchor="ne",
            text="THREAT: {:.1f}m".format(distance),
            fill="#ff6972" if distance < 4 else "#b7aeb7",
            font=("Consolas", 13, "bold")
        )

        # Flashlight status
        self.canvas.create_text(
            SCREEN_W - 20,
            45,
            anchor="ne",
            text=(
                "FLASHLIGHT: ON"
                if self.flashlight
                else "FLASHLIGHT: OFF"
            ),
            fill="#f0e6b2" if self.flashlight else "#777777",
            font=("Consolas", 11)
        )

        self.canvas.create_text(
            SCREEN_W / 2,
            SCREEN_H - 25,
            text="FIND THE EXIT",
            fill="#d7c5db",
            font=("Consolas", 12, "bold")
        )

    # ========================================================
    # END SCREENS
    # ========================================================

    def die(self):

        self.dead = True

    def draw_end_screen(self):

        if self.dead:

            self.canvas.create_rectangle(
                0,
                0,
                SCREEN_W,
                SCREEN_H,
                fill="#29070b",
                outline=""
            )

            self.canvas.create_text(
                SCREEN_W / 2,
                SCREEN_H / 2 - 70,
                text="DU BIST TOT",
                fill="#ff2538",
                font=("Impact", 62, "bold")
            )

            self.canvas.create_text(
                SCREEN_W / 2,
                SCREEN_H / 2 + 10,
                text="TUNG TUNG TUNG SAHUR HAT DICH GEFANGEN.",
                fill="#e8b6b6",
                font=("Consolas", 17, "bold")
            )

            self.canvas.create_text(
                SCREEN_W / 2,
                SCREEN_H / 2 + 65,
                text="R / LEERTASTE UM NEUZUSTARTEN",
                fill="#ffffff",
                font=("Consolas", 14)
            )

        elif self.won:

            self.canvas.create_rectangle(
                0,
                0,
                SCREEN_W,
                SCREEN_H,
                fill="#0c241b",
                outline=""
            )

            self.canvas.create_text(
                SCREEN_W / 2,
                SCREEN_H / 2 - 70,
                text="DU BIST ENTKOMMEN!",
                fill="#55ffae",
                font=("Impact", 55, "bold")
            )

            self.canvas.create_text(
                SCREEN_W / 2,
                SCREEN_H / 2 + 10,
                text="SAHUR WIRD WIEDERKEHREN...",
                fill="#b7e8ce",
                font=("Consolas", 16, "bold")
            )

            self.canvas.create_text(
                SCREEN_W / 2,
                SCREEN_H / 2 + 65,
                text="R / LEERTASTE UM NEUZUSTARTEN",
                fill="#ffffff",
                font=("Consolas", 14)
            )

    # ========================================================
    # LOOP
    # ========================================================

    def loop(self):

        if not self.running:
            return

        now = time.perf_counter()

        dt = min(
            0.05,
            now - self.last_time
        )

        self.last_time = now

        self.update_player(dt)
        self.update_npc(dt)

        self.canvas.delete("all")

        self.draw_3d()

        if self.dead or self.won:
            self.draw_end_screen()

        self.root.after(
            16,
            self.loop
        )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    game = TungTungMaze(root)

    root.mainloop()
