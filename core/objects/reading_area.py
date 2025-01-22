import tkinter as tk
from core.events.event_bus import EventBus

class ReadingArea:
    """阅读区域实现"""
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.window = tk.Toplevel()
        self._setup_display()
        self._load_default_style()
        self._register_handlers()

    def _setup_display(self):
        """初始化显示区域"""
        self.window.title("阅读区域")
        self.window.geometry("600x400")
        self.window.attributes('-alpha', 0.9)  # 设置透明度
        self.window.attributes('-topmost', True)  # 置顶
        
        # 文本显示区域
        self.text_area = tk.Text(
            self.window,
            wrap=tk.WORD,
            font=("宋体", 12),
            spacing1=5,
            spacing2=2,
            spacing3=5
        )
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # 滚动条
        scrollbar = tk.Scrollbar(self.window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_area.yview)

    def _load_default_style(self):
        """加载默认样式"""
        self.text_area.config(
            bg='#F5F5DC',  # 背景色
            fg='#000000',  # 前景色
            insertbackground='black',  # 光标颜色
            selectbackground='#ADD8E6'  # 选中背景色
        )

    def _register_handlers(self):
        """注册事件处理器"""
        self.event_bus.register('file_content_loaded', self.update_display)
        self.event_bus.register('toggle_visibility', self.toggle_visibility)
        self.event_bus.register('change_opacity', self.change_opacity)

    def update_display(self, content: str):
        """更新显示内容"""
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, content)

    def toggle_visibility(self):
        """切换显示/隐藏"""
        if self.window.winfo_viewable():
            self.window.withdraw()
        else:
            self.window.deiconify()

    def change_opacity(self, opacity: float):
        """改变透明度"""
        self.window.attributes('-alpha', opacity)
