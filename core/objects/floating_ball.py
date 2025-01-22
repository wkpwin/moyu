import tkinter as tk
from core.events.event_bus import EventBus

class FloatingBall:
    """悬浮球实现"""
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.window = tk.Toplevel()
        self._setup_ui()
        self._bind_events()
        self._drag_data = {"x": 0, "y": 0}

    def _setup_ui(self):
        """初始化UI"""
        self.window.overrideredirect(True)  # 去除窗口边框
        self.window.attributes('-alpha', 0.8)  # 设置透明度
        self.window.attributes('-topmost', True)  # 置顶
        
        # 悬浮球主体
        self.canvas = tk.Canvas(
            self.window,
            width=50,
            height=50,
            bg='#87CEEB',
            highlightthickness=0
        )
        self.canvas.pack()
        
        # 绘制圆形
        self.canvas.create_oval(
            5, 5, 45, 45,
            fill='#87CEEB',
            outline='#4682B4',
            width=2
        )
        
        # 初始位置
        self.window.geometry("50x50+100+100")

    def _bind_events(self):
        """绑定事件"""
        self.canvas.bind("<ButtonPress-1>", self._on_drag_start)
        self.canvas.bind("<B1-Motion>", self._on_drag_move)
        self.canvas.bind("<ButtonRelease-1>", self._on_drag_end)
        self.canvas.bind("<Button-1>", self._on_click)

    def _on_drag_start(self, event):
        """开始拖动"""
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        self.event_bus.emit('drag_start')

    def _on_drag_move(self, event):
        """拖动中"""
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        x = self.window.winfo_x() + delta_x
        y = self.window.winfo_y() + delta_y
        self.window.geometry(f"+{x}+{y}")

    def _on_drag_end(self, event):
        """结束拖动"""
        self.event_bus.emit('drag_end')

    def _on_click(self, event):
        """点击事件"""
        self.event_bus.emit('click')
