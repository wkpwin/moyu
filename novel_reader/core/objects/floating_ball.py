import tkinter as tk
from typing import Optional
from core.interfaces.event_interface import IEvent

class FloatingBall(IEvent):
    """悬浮球实现类"""
    
    def __init__(self, parent: Optional[tk.Toplevel] = None):
        self.parent = parent
        self.window = tk.Toplevel(parent) if parent else tk.Tk()
        self.window.overrideredirect(True)
        self.window.attributes("-alpha", 0.8)
        self.window.attributes("-topmost", True)
        
        # 初始化界面
        self.init_ui()
        
        # 绑定事件
        self.bind_events()
        
    def init_ui(self):
        """初始化悬浮球界面"""
        self.canvas = tk.Canvas(
            self.window,
            width=50,
            height=50,
            bg="lightblue",
            highlightthickness=0
        )
        self.canvas.pack()
        
        # 绘制圆形
        self.canvas.create_oval(
            5, 5, 45, 45,
            fill="lightblue",
            outline="blue"
        )
        
        # 设置初始位置
        self.window.geometry("+100+100")
        
    def bind_events(self):
        """绑定事件处理"""
        self.canvas.bind("<Button-1>", self._on_mouse_down)
        self.canvas.bind("<B1-Motion>", self._on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_mouse_up)
        
    def _on_mouse_down(self, event):
        """鼠标按下事件"""
        self.start_x = event.x
        self.start_y = event.y
        
    def _on_mouse_drag(self, event):
        """鼠标拖动事件"""
        x = self.window.winfo_x() + (event.x - self.start_x)
        y = self.window.winfo_y() + (event.y - self.start_y)
        self.window.geometry(f"+{x}+{y}")
        
    def _on_mouse_up(self, event):
        """鼠标释放事件"""
        pass
        
    def toggle_visibility(self) -> None:
        """切换可见性"""
        if self.window.state() == "normal":
            self.window.withdraw()
        else:
            self.window.deiconify()
            
    def set_transparency(self, value: float) -> None:
        """设置透明度"""
        self.window.attributes("-alpha", value)
        
    def toggle_topmost(self) -> None:
        """切换置顶状态"""
        current = self.window.attributes("-topmost")
        self.window.attributes("-topmost", not current)
        
    # IEvent接口实现
    def trigger_event(self, event_type: str, *args, **kwargs) -> None:
        """触发事件"""
        if event_type == "toggle_visibility":
            self.toggle_visibility()
        elif event_type == "set_transparency":
            self.set_transparency(*args)
        elif event_type == "toggle_topmost":
            self.toggle_topmost()
            
    def has_event(self, event_type: str) -> bool:
        """检查是否支持指定事件类型"""
        return event_type in ["toggle_visibility", "set_transparency", "toggle_topmost"]
