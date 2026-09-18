
import tkinter as tk
from tkinter import ttk
import random


# =========================
# WAFFEN
# =========================

Waffen = [
    "Schwert",
    "Langschwert",
    "Speer",
    "Fäuste",
    "Hellebarde",
    "Flegel"
]

WeaponStats = {
    "Schwert": {
        "Damage": 25,
        "Accuracy": 50
    },
    "Langschwert": {
        "Damage": 40,
        "Accuracy": 40
    },
    "Speer": {
        "Damage": 20,
        "Accuracy": 70
    },
    "Fäuste": {
        "Damage": 10,
        "Accuracy": 90
    },
    "Hellebarde": {
        "Damage": 30,
        "Accuracy": 60
    },
    "Flegel": {
        "Damage": 60,
        "Accuracy": 30
    }
}


# =========================
# SPIEL
# =========================

class SahurGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Tung Tung Tung Sahur")
        self.root.geometry("650x700")
        self.root.resizable(False, False)

        # Farben
        self.bg_color = "#202124"
        self.panel_color = "#292a2d"
        self.text_color = "#ffffff"
        self.accent_color = "#e63946"
        self.green_color = "#4caf50"
        self.button_color = "#3c4043"

        self.root.configure(bg=self.bg_color)

        # Spielwerte
        self.Waffe = "Fäuste"
        self.PlayerHealth = 100
        self.SahurHealth = 300
        self.Turn = "Player"
        self.GameRunning = True

        self.create_styles()
        self.create_weapon_selection()

    # =========================
    # STYLES
    # =========================

    def create_styles(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")

        # WICHTIG:
        # Progressbar-Styles müssen einen gültigen
        # TProgressbar-Stil verwenden.
        #
        # Der alte Name "Health.Horizontal" führte
        # zu folgendem Fehler:
        #
        # Layout Horizontal.Health.Horizontal not found

        # Spieler HP
        style.configure(
            "Health.Horizontal.TProgressbar",
            troughcolor="#3a3a3a",
            background=self.green_color,
            bordercolor="#3a3a3a",
            lightcolor=self.green_color,
            darkcolor=self.green_color
        )

        style.layout(
            "Health.Horizontal.TProgressbar",
            [
                (
                    "Horizontal.Progressbar.trough",
                    {
                        "children": [
                            (
                                "Horizontal.Progressbar.pbar",
                                {
                                    "side": "left",
                                    "sticky": "ns"
                                }
                            ),
                            (
                                "Horizontal.Progressbar.label",
                                {
                                    "sticky": ""
                                }
                            )
                        ],
                        "sticky": "nswe"
                    }
                )
            ]
        )

        # Sahur HP
        style.configure(
            "Sahur.Horizontal.TProgressbar",
            troughcolor="#3a3a3a",
            background=self.accent_color,
            bordercolor="#3a3a3a",
            lightcolor=self.accent_color,
            darkcolor=self.accent_color
        )

        style.layout(
            "Sahur.Horizontal.TProgressbar",
            [
                (
                    "Horizontal.Progressbar.trough",
                    {
                        "children": [
                            (
                                "Horizontal.Progressbar.pbar",
                                {
                                    "side": "left",
                                    "sticky": "ns"
                                }
                            ),
                            (
                                "Horizontal.Progressbar.label",
                                {
                                    "sticky": ""
                                }
                            )
                        ],
                        "sticky": "nswe"
                    }
                )
            ]
        )

    # =========================
    # HILFSFUNKTIONEN
    # =========================

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_label(self, parent, text, size=12, bold=False):
        font = ("Arial", size, "bold" if bold else "normal")

        return tk.Label(
            parent,
            text=text,
            font=font,
            bg=self.bg_color,
            fg=self.text_color
        )

    def create_button(self, parent, text, command, width=20):
        return tk.Button(
            parent,
            text=text,
            command=command,
            width=width,
            font=("Arial", 11, "bold"),
            bg=self.button_color,
            fg=self.text_color,
            activebackground="#55585c",
            activeforeground=self.text_color,
            relief="flat",
            cursor="hand2",
            pady=6
        )

    # =========================
    # WAFFENWAHL
    # =========================

    def create_weapon_selection(self):
        self.clear_window()

        title = self.create_label(
            self.root,
            "TUNG TUNG TUNG SAHUR",
            24,
            True
        )
        title.pack(pady=(25, 5))

        subtitle = self.create_label(
            self.root,
            "Welche Waffe wählst du?",
            15
        )
        subtitle.pack(pady=(0, 20))

        self.weapon_var = tk.StringVar(value="Fäuste")

        weapon_frame = tk.Frame(
            self.root,
            bg=self.panel_color,
            padx=15,
            pady=15
        )
        weapon_frame.pack(padx=30, fill="x")

        for weapon in Waffen:
            stats = WeaponStats[weapon]

            text = (
                f"{weapon}   |   "
                f"Schaden: {stats['Damage']}   |   "
                f"Trefferchance: {stats['Accuracy']}%"
            )

            radio = tk.Radiobutton(
                weapon_frame,
                text=text,
                variable=self.weapon_var,
                value=weapon,
                font=("Arial", 11),
                bg=self.panel_color,
                fg=self.text_color,
                selectcolor="#45474b",
                activebackground=self.panel_color,
                activeforeground=self.text_color,
                anchor="w",
                padx=10,
                pady=7
            )

            radio.pack(fill="x")

        start_button = self.create_button(
            self.root,
            "KAMPF STARTEN",
            self.start_game,
            width=25
        )
        start_button.pack(pady=30)

    # =========================
    # SPIEL STARTEN
    # =========================

    def start_game(self):
        self.Waffe = self.weapon_var.get()

        self.PlayerHealth = 100
        self.SahurHealth = 300
        self.Turn = "Player"
        self.GameRunning = True

        self.create_game_screen()

        self.log(
            f"Du hast {self.Waffe} gewählt."
        )

        self.log(
            "TUNG TUNG TUNG SAHUR erscheint!"
        )

        self.log(
            "Du bist am Zug."
        )

        self.update_health()
        self.enable_player_buttons()

    # =========================
    # SPIELSCREEN
    # =========================

    def create_game_screen(self):
        self.clear_window()

        title = self.create_label(
            self.root,
            "TUNG TUNG TUNG SAHUR",
            22,
            True
        )
        title.pack(pady=(20, 5))

        weapon_label = self.create_label(
            self.root,
            f"Deine Waffe: {self.Waffe}",
            13
        )
        weapon_label.pack(pady=(0, 15))

        # HP-Panel
        health_frame = tk.Frame(
            self.root,
            bg=self.panel_color,
            padx=20,
            pady=15
        )
        health_frame.pack(padx=30, fill="x")

        # Spieler HP
        self.player_hp_label = tk.Label(
            health_frame,
            text="Dein HP: 100 / 100",
            font=("Arial", 13, "bold"),
            bg=self.panel_color,
            fg=self.text_color
        )
        self.player_hp_label.pack(anchor="w")

        self.player_hp_bar = ttk.Progressbar(
            health_frame,
            style="Health.Horizontal.TProgressbar",
            orient="horizontal",
            length=560,
            mode="determinate",
            maximum=100
        )
        self.player_hp_bar.pack(fill="x", pady=(5, 15))

        # Sahur HP
        self.sahur_hp_label = tk.Label(
            health_frame,
            text="Sahur HP: 300 / 300",
            font=("Arial", 13, "bold"),
            bg=self.panel_color,
            fg=self.text_color
        )
        self.sahur_hp_label.pack(anchor="w")

        self.sahur_hp_bar = ttk.Progressbar(
            health_frame,
            style="Sahur.Horizontal.TProgressbar",
            orient="horizontal",
            length=560,
            mode="determinate",
            maximum=300
        )
        self.sahur_hp_bar.pack(fill="x", pady=(5, 0))

        # Kampfstatus
        self.turn_label = self.create_label(
            self.root,
            "DEIN ZUG",
            16,
            True
        )
        self.turn_label.pack(pady=15)

        # Buttons
        self.action_frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )
        self.action_frame.pack()

        self.attack_button = self.create_button(
            self.action_frame,
            "Angriff",
            lambda: self.player_turn("1"),
            width=22
        )
        self.attack_button.grid(row=0, column=0, padx=5, pady=5)

        self.light_button = self.create_button(
            self.action_frame,
            "Leichter Angriff",
            lambda: self.player_turn("2"),
            width=22
        )
        self.light_button.grid(row=0, column=1, padx=5, pady=5)

        self.heavy_button = self.create_button(
            self.action_frame,
            "Schwerer Angriff",
            lambda: self.player_turn("3"),
            width=22
        )
        self.heavy_button.grid(row=1, column=0, padx=5, pady=5)

        self.heal_button = self.create_button(
            self.action_frame,
            "Heilen",
            lambda: self.player_turn("4"),
            width=22
        )
        self.heal_button.grid(row=1, column=1, padx=5, pady=5)

        # Kampfprotokoll
        log_title = self.create_label(
            self.root,
            "Kampfprotokoll",
            13,
            True
        )
        log_title.pack(pady=(20, 5))

        log_frame = tk.Frame(
            self.root,
            bg=self.panel_color
        )
        log_frame.pack(padx=30, fill="both", expand=True)

        self.combat_log = tk.Text(
            log_frame,
            height=8,
            width=70,
            font=("Consolas", 10),
            bg="#18191b",
            fg="#eeeeee",
            insertbackground="white",
            state="disabled",
            relief="flat",
            padx=10,
            pady=10,
            wrap="word"
        )
        self.combat_log.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = tk.Scrollbar(
            log_frame,
            command=self.combat_log.yview
        )
        scrollbar.pack(side="right", fill="y")

        self.combat_log.config(
            yscrollcommand=scrollbar.set
        )

    # =========================
    # LOG
    # =========================

    def log(self, message):
        self.combat_log.config(state="normal")

        self.combat_log.insert(
            "end",
            message + "\n"
        )

        self.combat_log.see("end")
        self.combat_log.config(state="disabled")

    # =========================
    # HP AKTUALISIEREN
    # =========================

    def update_health(self):
        self.player_hp_label.config(
            text=f"Dein HP: {self.PlayerHealth} / 100"
        )

        self.sahur_hp_label.config(
            text=f"Sahur HP: {self.SahurHealth} / 300"
        )

        self.player_hp_bar["value"] = self.PlayerHealth
        self.sahur_hp_bar["value"] = self.SahurHealth

    # =========================
    # ATTACK
    # =========================

    def Attack(self, Damage, Accuracy, attacker):
        Accuracy = max(0, min(100, Accuracy))

        Roll = random.randint(1, 100)

        self.log(
            f"Trefferchance: {Accuracy:.1f}% | "
            f"Wurf: {Roll}"
        )

        if Roll <= Accuracy:

            if attacker == "Player":
                self.log(
                    f"GETROFFEN! Sahur nimmt "
                    f"{Damage:.1f} Schaden."
                )
            else:
                self.log(
                    f"GETROFFEN! Du nimmst "
                    f"{Damage:.1f} Schaden."
                )

            return Damage

        else:
            self.log("NICHT GETROFFEN!")

            return 0

    # =========================
    # PLAYER TURN
    # =========================

    def player_turn(self, choice):
        if not self.GameRunning:
            return

        if self.Turn != "Player":
            return

        self.disable_player_buttons()

        if choice == "1":

            Damage = WeaponStats[self.Waffe]["Damage"]
            Accuracy = WeaponStats[self.Waffe]["Accuracy"]

            self.log("\nANGRIFF!")

            DamageDealt = self.Attack(
                Damage,
                Accuracy,
                "Player"
            )

            self.SahurHealth -= DamageDealt

        elif choice == "2":

            Damage = WeaponStats[self.Waffe]["Damage"] * 0.8
            Accuracy = WeaponStats[self.Waffe]["Accuracy"] * 1.2

            self.log("\nLEICHTER ANGRIFF!")

            DamageDealt = self.Attack(
                Damage,
                Accuracy,
                "Player"
            )

            self.SahurHealth -= DamageDealt

        elif choice == "3":

            Damage = WeaponStats[self.Waffe]["Damage"] * 1.2
            Accuracy = WeaponStats[self.Waffe]["Accuracy"] * 0.8

            self.log("\nSCHWERER ANGRIFF!")

            DamageDealt = self.Attack(
                Damage,
                Accuracy,
                "Player"
            )

            self.SahurHealth -= DamageDealt

        elif choice == "4":

            self.PlayerHealth += 10

            if self.PlayerHealth > 100:
                self.PlayerHealth = 100

            self.log("\n10 HP geheilt.")

        self.update_health()

        # Prüfen, ob Sahur tot ist
        if self.SahurHealth <= 0:
            self.SahurHealth = 0
            self.update_health()
            self.game_win()
            return

        # Sahur ist dran
        self.Turn = "Sahur"

        self.turn_label.config(
            text="SAHUR IST AM ZUG"
        )

        # Kurze Pause vor Sahurs Angriff
        self.root.after(700, self.sahur_turn)

    # =========================
    # SAHUR TURN
    # =========================

    def sahur_turn(self):

        if not self.GameRunning:
            return

        self.log("\nSAHUR GREIFT AN!")

        Damage = 40
        Accuracy = 30

        DamageDealt = self.Attack(
            Damage,
            Accuracy,
            "Sahur"
        )

        self.PlayerHealth -= DamageDealt

        if self.PlayerHealth < 0:
            self.PlayerHealth = 0

        self.update_health()

        # Prüfen, ob Spieler tot ist
        if self.PlayerHealth <= 0:
            self.game_over()
            return

        self.Turn = "Player"

        self.turn_label.config(
            text="DEIN ZUG"
        )

        self.enable_player_buttons()

    # =========================
    # BUTTONS
    # =========================

    def disable_player_buttons(self):
        self.attack_button.config(state="disabled")
        self.light_button.config(state="disabled")
        self.heavy_button.config(state="disabled")
        self.heal_button.config(state="disabled")

    def enable_player_buttons(self):
        self.attack_button.config(state="normal")
        self.light_button.config(state="normal")
        self.heavy_button.config(state="normal")
        self.heal_button.config(state="normal")

    # =========================
    # GAME OVER / WIN
    # =========================

    def game_over(self):
        self.GameRunning = False
        self.disable_player_buttons()

        self.turn_label.config(
            text="GAME OVER",
            fg="#ff4444"
        )

        self.log("\nSahur hat dich getötet.")
        self.log("GAME OVER")

        self.show_restart_button()

    def game_win(self):
        self.GameRunning = False
        self.disable_player_buttons()

        self.turn_label.config(
            text="DU HAST GEWONNEN!",
            fg="#4caf50"
        )

        self.log("\nSahur ist tot.")
        self.log("DU HAST GEWONNEN!")

        self.show_restart_button()

    def show_restart_button(self):
        restart_button = self.create_button(
            self.root,
            "NOCHMAL SPIELEN",
            self.restart_game,
            width=25
        )

        restart_button.pack(pady=15)

    def restart_game(self):
        self.create_weapon_selection()


# =========================
# START
# =========================

if __name__ == "__main__":
    root = tk.Tk()

    game = SahurGame(root)

    root.mainloop()
