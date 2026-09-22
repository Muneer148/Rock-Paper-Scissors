import tkinter as tk
import random

# Rock Paper Scissors
# Academic project - St. Martin's Engineering College

CHOICES = ("Rock", "Paper", "Scissors")


class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("620x520")
        self.root.resizable(False, False)

        self.player_score = 0
        self.computer_score = 0
        self.draws = 0

        self.title = tk.Label(
            root,
            text="✊ ROCK  •  PAPER  •  SCISSORS",
            font=("Arial", 22, "bold"),
        )
        self.title.pack(pady=(25, 8))

        tk.Label(
            root,
            text="Choose your move",
            font=("Arial", 13),
        ).pack(pady=(0, 18))

        button_frame = tk.Frame(root)
        button_frame.pack()

        for choice, symbol in (
            ("Rock", "✊"),
            ("Paper", "✋"),
            ("Scissors", "✌"),
        ):
            tk.Button(
                button_frame,
                text=f"{symbol}\n{choice}",
                font=("Arial", 13, "bold"),
                width=11,
                height=3,
                command=lambda c=choice: self.play(c),
            ).pack(side=tk.LEFT, padx=7)

        self.result = tk.Label(
            root,
            text="Make your choice to start!",
            font=("Arial", 17, "bold"),
            wraplength=520,
        )
        self.result.pack(pady=(35, 15))

        self.player_choice = tk.Label(
            root, text="You: —", font=("Arial", 13)
        )
        self.player_choice.pack(pady=4)

        self.computer_choice = tk.Label(
            root, text="Computer: —", font=("Arial", 13)
        )
        self.computer_choice.pack(pady=4)

        self.score = tk.Label(
            root,
            text=self.score_text(),
            font=("Arial", 14, "bold"),
        )
        self.score.pack(pady=25)

        tk.Button(
            root,
            text="Reset Game",
            font=("Arial", 11, "bold"),
            width=15,
            command=self.reset,
        ).pack()

        tk.Label(
            root,
            text="First to any score — or keep playing for a high score!",
            font=("Arial", 9),
        ).pack(side=tk.BOTTOM, pady=12)

    @staticmethod
    def winner(player, computer):
        if player == computer:
            return "draw"

        winning_moves = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper",
        }

        return "player" if winning_moves[player] == computer else "computer"

    def play(self, player):
        computer = random.choice(CHOICES)
        outcome = self.winner(player, computer)

        if outcome == "player":
            self.player_score += 1
            message = "🎉 You win!"
        elif outcome == "computer":
            self.computer_score += 1
            message = "💻 Computer wins!"
        else:
            self.draws += 1
            message = "🤝 It's a draw!"

        self.player_choice.config(text=f"You: {player}")
        self.computer_choice.config(text=f"Computer: {computer}")
        self.result.config(text=message)
        self.score.config(text=self.score_text())

    def score_text(self):
        return (
            f"Player: {self.player_score}    |    "
            f"Computer: {self.computer_score}    |    "
            f"Draws: {self.draws}"
        )

    def reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.draws = 0

        self.player_choice.config(text="You: —")
        self.computer_choice.config(text="Computer: —")
        self.result.config(text="Make your choice to start!")
        self.score.config(text=self.score_text())


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
