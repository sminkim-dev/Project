from tkinter import *
from tkinter import messagebox

# --- 26.05.31 11:58 --- #
# 단순 예제가 아닌...앱 처럼 만들었을 경우의 구조. AI로 생성하였고, 구조 공부 중...

# mainloop()
#     │
#     ├─ TicTacToeApp()
#     │      │
#     │      └─ __init__()
#     │              │
#     │              └─ show_start_screen()
#     │
#     ├─ [시작하기 클릭]
#     │      │
#     │      └─ show_game_screen()
#     │
#     ├─ [칸 클릭]
#     │      │
#     │      └─ click()
#     │             │
#     │             ├─ check_winner()
#     │             │
#     │             └─ finish_game()
#     │
#     ├─ [리셋 클릭]
#     │      │
#     │      └─ reset_game()
#     │
#     └─ [종료 클릭]
#            │
#            └─ quit_game()

# --- Note memo --- #
#   함수 사용할 때 기존에는 () 를 항상 써야한단 인식이 있었음. 하지만 여기선 사용하지 않음.
#   이유! >> () 를 붙이면 "버튼을 생성되자 마자 함수 실행"인 느낌으로 감. 즉, 버튼을 눌렀을 때 실행되게끔 만들어야 하므로 ()를 안씀.
#   그럼 어떻게 되는가? ---> 함수를 불렀을 때 해당 함수에 () 가 없으면 실행하진 않고 기억하고만 있다가 이벤트가 발생하면(클릭) 그때 실행되는 느낌.
#   tkinket의 command= 는 함수 자체를 넘겨야 하므로 ()가 없음. 그래서 lamda를 사용함.
#   수업 내용이 그래서...lamda를 사용하지 않고 하려면 함수를 제대로 호출 할 수 없기에 반복문 안에 또 함수를 만들고 해당 함수를 호출하는 식으로 진행했었음.
#   -----   -----   -----
#   람다를 쓰지 않을 경우 아래처럼 사용했었음.
# def click(index):
#     print(index)

# def wrapper():
#     click(3)

# Button(command=wrapper)
#   -----    -----   -----
#   시각화
# 버튼 클릭
#     ↓
# wrapper()
#     ↓
# click(3)

# lamda (람다)란 무엇인가? > 짧게 쓰는 문법이라 이해하자.

# 예를 들어...
# def add(a , b): return a + b 를 lamda를 쓴다면..? >> add = lamda a , b : a + b 로 사용 가능. (임시 함수 느낌이라 생각하자.)
# lamda 안에서 넘기는 값은 "복사" 가 아닌 "참조"다. 
# 즉, 반복문 안에 예를 들면...
# for i in range(9): command=lamda self.click(i) 를 한다면, 오류남. 모든 버튼이 버튼 8만 실행됨. 그 이유가 참조이기 때문에 가장 마지막 값으로 변했기 때문.
# 이러한 이유로 값을 바로 넣는게 아닌, 값을 복사해서 넣는 것임. ex) command=lamda key=index : self.click(key) 이런 느낌으로 그냥 기억할 해둘 것.

# plus... tkinter에서 command= 는 함수 자체만 넣을 수 있어서 만일 매개변수가 있는 함수라면 "인자를 찾을 수 없음"이라는 경고가 뜸. 때문에 약간 캡슐화 느낌으로
# 함수 안에 함수를 넣어서 command 안에 함수를 넣을 수 있게 만드는 과정을 요약한 것이 lamda고, 둘 다 써도 지장 없음. 단 lamda를 반복문에서 쓸 땐 주의해야함.
# 반복문 안 변수 값을 참조하기 때문에 가장 마지막 값이 들어가서, 출력을 한다면 마지막 값이, 이벤트 호출시라면 해당 인덱스 이벤트만 호출되는 일이 생길 수 있음.
# 그렇기에 값을 그냥 넣는 것이 아닌, 값을 "복사" 해서 해당 값을 원래 인자를 받는 함수로 넘겨야 함. ex) command=lamda key=i:self.add(key)

# from tkinter import*를 했음에도 추가로 from tkinter import messagebox를 하는 이유는...
# 전자는 tkinter 모듈 안에 공개된 이름만 불러옴.
# messagebox는 tkinter의 서브 모듈에 가까워서...tkinter.messagebox라는 독립적인 모듈에 가깝기 때문에 import messagebox를 하는 것.
# from tkinter import* 만 하면, canvas, button, label, frame은 사용가능하지만, messagebox.showinfo() 사용 불가능함.

# 보통은... 
#   import tkinter as tk
#   from tkinter import messagebox

#   둘의 차이를 표현하자면 C++의 namespace 같은 느낌으로 보면 될 듯함. from tkinter import*를 하면 window = Tk() 이후에 Button으로 바로 쓸 수 있지만,
#   import tkinter as tk는 window = tk.TK() tk.Button 으로 tkinter에 접근해서 사용하는 느낌이고 from tkinter import*는 해당 내용을 현재 파일에 불러와서 쓰는 느낌임.
#   근데 왜 import tkinter as tk를 더 많이 사용하는가? 그 이유는 보통 클래스 이름이 중복되거나 내용이 덮어질 우려가 있어서임. 
#   여러 라이브러리를 불러올 때, label, button 같은 것들이 겹칠 수 있어서 별칭으로 가져오면...a.button, b.button 식으로 해당 우려가 없음.

# --- 26.06.01 11:54 --- #
#   계속 헷갈렸던 내용 파악. C#의 세션 기능을 응용해서 웹 페이지를 만든 기억이 있어서, 해당 앱의 동작 방식이 처음에는 이해가 되지 않았지만. 지금은 갈피가 잡힘.
#   --- 수업에서는 window, button을 이런 식으로 배웠지만 ---  #
# window
# ├── button0
# ├── button1
# ├── button2
# ...
# └── reset_button

#   --- 위 처럼 사용하면 window 에 버튼을 바로 넣는 것이어서, 창이 하나면 기능은 하지만, 창이 여러개라면 어느 소속의 버튼, 기능인지가 모호해짐. --- #
#   그래서 아래 처럼 frame을 이용하여 구분하는 것임.
#   ---     ---     ---     #
# window
# └── game_frame
#     ├── status_label
#     ├── board_frame
#     │   ├── cell_button0
#     │   ├── cell_button1
#     │   └── ...
#     ├── reset_button
#     └── exit_button

#   이렇게 하면, frame을 기준으로 창 변환, 작동 한다고 생각하면 됨.
#   처음에는 label, button을 어떻게 창이 바뀔 때마다 구현하는거지? C#처럼 페이지를 따로 설계하는 것이 아닌데? 로 생각했지만.
#   frame.destroy()로 창이 변경될 때마다 frame을 없애서, 다시 해당 타겟의 frame을 재 생성하는 과정이었던 것임.
#   즉, 버튼 이벤트가 발생하면 해당 버튼 클릭시 발생하는 frame 안에 들어간 함수  button, label 이 그때마다 생성되는 것임.
#   C#처럼 해당 내용을 세션처럼 유지할 수 있는지는 확인해보지는 않았음.

# 디자인 생성은 아직 미숙. HTML은 쓸 줄은 알지만...좌표나 위치 선정이 아직 미숙함. 그래서 디자인은 AI -> 내부는 직접 공부해서 작성하는 연습 중임.

APP_BG = "#14161f"
PANEL_BG = "#1f2330"
GRID_BG = "#2b3040"
TEXT = "#f5f1e8"
SUB_TEXT = "#aeb6c6"
ACCENT = "#48d1cc"
ACCENT_DARK = "#279f9c"
O_COLOR = "#ffd166"
X_COLOR = "#ef476f"
WIN_COLOR = "#58d68d"

WIN_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [2, 4, 6], [0, 4, 8],
]


class TicTacToeApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic Tac Toe")
        self.window.geometry("520x680")
        self.window.minsize(380, 520)
        self.window.configure(bg=APP_BG)

        self.turn = True
        self.move_count = 0
        self.button_list = []
        self.current_screen = None

        self.show_start_screen()

    def clear_screen(self):
        if self.current_screen is not None:
            self.current_screen.destroy()

    def make_button(self, parent, text, command, bg=ACCENT, fg=APP_BG):
        button = Button(
            parent,
            text=text,
            command=command,
            font=("Helvetica", 15, "bold"),
            bg=bg,
            fg=fg,
            activebackground=ACCENT_DARK,
            activeforeground=TEXT,
            relief=FLAT,
            bd=0,
            cursor="hand2",
            padx=18,
            pady=12,
        )
        return button

    def show_start_screen(self):
        self.clear_screen()

        frame = Frame(self.window, bg=APP_BG)
        frame.pack(fill=BOTH, expand=True)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=0)
        frame.rowconfigure(2, weight=1)
        frame.columnconfigure(0, weight=1)
        self.current_screen = frame

        hero = Frame(frame, bg=APP_BG)
        hero.grid(row=1, column=0, sticky="nsew", padx=36)
        hero.columnconfigure(0, weight=1)

        logo = Canvas(hero, width=220, height=220, bg=APP_BG, highlightthickness=0)
        logo.grid(row=0, column=0, pady=(0, 24))
        self.draw_logo(logo)

        title = Label(
            hero,
            text="Tic Tac Toe",
            font=("Helvetica", 38, "bold"),
            bg=APP_BG,
            fg=TEXT,
        )
        title.grid(row=1, column=0)

        subtitle = Label(
            hero,
            text="O와 X가 번갈아 두는 3 x 3 전략 게임",
            font=("Helvetica", 14),
            bg=APP_BG,
            fg=SUB_TEXT,
        )
        subtitle.grid(row=2, column=0, pady=(10, 34))

        start_button = self.make_button(hero, "시작하기", self.show_game_screen)
        start_button.grid(row=3, column=0, sticky="ew", padx=38)

        exit_button = self.make_button(
            hero,
            "종료",
            self.quit_game,
            bg="#303647",
            fg=TEXT,
        )
        exit_button.grid(row=4, column=0, sticky="ew", padx=38, pady=(12, 0))

    def draw_logo(self, canvas):
        line_options = {"fill": GRID_BG, "width": 8, "capstyle": ROUND}
        canvas.create_line(80, 26, 80, 194, **line_options)
        canvas.create_line(140, 26, 140, 194, **line_options)
        canvas.create_line(26, 80, 194, 80, **line_options)
        canvas.create_line(26, 140, 194, 140, **line_options)
        canvas.create_oval(33, 33, 67, 67, outline=O_COLOR, width=7)
        canvas.create_line(154, 34, 186, 66, fill=X_COLOR, width=7, capstyle=ROUND)
        canvas.create_line(186, 34, 154, 66, fill=X_COLOR, width=7, capstyle=ROUND)
        canvas.create_oval(153, 153, 187, 187, outline=O_COLOR, width=7)
        canvas.create_line(34, 154, 66, 186, fill=X_COLOR, width=7, capstyle=ROUND)
        canvas.create_line(66, 154, 34, 186, fill=X_COLOR, width=7, capstyle=ROUND)

    def show_game_screen(self):
        self.clear_screen()

        self.turn = True
        self.move_count = 0
        self.button_list = []

        frame = Frame(self.window, bg=APP_BG)
        frame.pack(fill=BOTH, expand=True, padx=22, pady=22)
        frame.rowconfigure(0, weight=0)
        frame.rowconfigure(1, weight=0)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=0)
        frame.columnconfigure(0, weight=1)
        self.current_screen = frame

        top_bar = Frame(frame, bg=APP_BG)
        top_bar.grid(row=0, column=0, sticky="ew", pady=(0, 18))
        top_bar.columnconfigure(0, weight=1)

        title = Label(
            top_bar,
            text="Tic Tac Toe",
            font=("Helvetica", 26, "bold"),
            bg=APP_BG,
            fg=TEXT,
        )
        title.grid(row=0, column=0, sticky="w")

        home_button = self.make_button(
            top_bar,
            "처음으로",
            self.show_start_screen,
            bg="#303647",
            fg=TEXT,
        )
        home_button.grid(row=0, column=1, sticky="e")

        self.status_label = Label(
            frame,
            text="O 차례",
            font=("Helvetica", 16, "bold"),
            bg=APP_BG,
            fg=O_COLOR,
        )
        self.status_label.grid(row=1, column=0, sticky="ew", pady=(0, 14))

        board = Frame(frame, bg=GRID_BG, padx=8, pady=8)
        board.grid(row=2, column=0, sticky="nsew", pady=(0, 8))

        for row in range(3):
            board.rowconfigure(row, weight=1, uniform="board")
        for column in range(3):
            board.columnconfigure(column, weight=1, uniform="board")

        for index in range(9):
            button = Button(
                board,
                text="",
                font=("Helvetica", 42, "bold"),
                bg=PANEL_BG,
                fg=TEXT,
                activebackground="#293044",
                activeforeground=TEXT,
                disabledforeground=TEXT,
                relief=FLAT,
                bd=0,
                command=lambda key=index: self.click(key),
            )
            row = index // 3
            column = index % 3
            button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
            self.button_list.append(button)

        controls = Frame(frame, bg=APP_BG)
        controls.grid(row=3, column=0, sticky="ew", pady=(14, 0))
        controls.columnconfigure(0, weight=1)
        controls.columnconfigure(1, weight=1)

        reset_button = self.make_button(controls, "리셋", self.reset_game)
        reset_button.grid(row=0, column=0, sticky="ew", padx=(0, 6))

        exit_button = self.make_button(
            controls,
            "종료",
            self.quit_game,
            bg="#303647",
            fg=TEXT,
        )
        exit_button.grid(row=0, column=1, sticky="ew", padx=(6, 0))

    def reset_game(self):
        self.turn = True
        self.move_count = 0
        self.status_label.config(text="O 차례", fg=O_COLOR)

        for button in self.button_list:
            button.config(
                text="",
                state=NORMAL,
                bg=PANEL_BG,
                fg=TEXT,
                disabledforeground=TEXT,
            )

    def quit_game(self):
        self.window.destroy()

    def check_winner(self, mark):
        for line in WIN_LINES:
            a, b, c = line
            if (
                self.button_list[a]["text"] == mark and
                self.button_list[b]["text"] == mark and
                self.button_list[c]["text"] == mark
            ):
                return line
        return None

    def click(self, key):
        mark = "O" if self.turn else "X"
        color = O_COLOR if mark == "O" else X_COLOR

        self.button_list[key].config(
            text=mark,
            state=DISABLED,
            disabledforeground=color,
        )
        self.move_count += 1

        win_line = self.check_winner(mark)
        if win_line:
            self.finish_game(mark, win_line)
            return

        if self.move_count == 9:
            self.status_label.config(text="무승부", fg=SUB_TEXT)
            messagebox.showinfo("Game Over", "무승부입니다!")
            return

        self.turn = not self.turn
        next_mark = "O" if self.turn else "X"
        next_color = O_COLOR if next_mark == "O" else X_COLOR
        self.status_label.config(text=next_mark + " 차례", fg=next_color)

    def finish_game(self, mark, win_line):
        self.status_label.config(text=mark + " 승리!", fg=WIN_COLOR)

        for index, button in enumerate(self.button_list):
            button.config(state=DISABLED)
            if index in win_line:
                button.config(bg="#243b35", disabledforeground=WIN_COLOR)

        messagebox.showinfo("Game Over", mark + " 승리!")


window = Tk()
app = TicTacToeApp(window)
window.mainloop()
