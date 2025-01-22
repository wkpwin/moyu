import tkinter as tk
from tkinter import filedialog
from core.events.event_bus import EventBus

class MainInterface:
    """主界面实现"""
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.root = tk.Tk()
        self._init_ui()
        self._bind_events()

    def _init_ui(self):
        """初始化UI"""
        self.root.title("桌面小说阅读器")
        self.root.geometry("400x300")
        
        # 文件选择按钮
        self.select_button = tk.Button(
            self.root,
            text="选择小说文件",
            command=self._on_file_select
        )
        self.select_button.pack(pady=20)
        
        # 历史文件列表
        self.history_listbox = tk.Listbox(self.root)
        self.history_listbox.pack(expand=True, fill=tk.BOTH, padx=20)
        
        # 加载历史记录
        self._load_history()

    def _bind_events(self):
        """绑定事件"""
        self.history_listbox.bind('<<ListboxSelect>>', self._on_history_select)

    def _on_file_select(self):
        """处理文件选择"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")]
        )
        if file_path:
            self.event_bus.emit('file_selected', file_path)
            self._add_to_history(file_path)

    def _on_history_select(self, event):
        """处理历史记录选择"""
        selection = self.history_listbox.curselection()
        if selection:
            file_path = self.history_listbox.get(selection[0])
            self.event_bus.emit('file_selected', file_path)

    def _load_history(self):
        """加载历史记录"""
        # TODO: 从history.json加载历史记录
        pass

    def _add_to_history(self, file_path: str):
        """添加文件到历史记录"""
        self.history_listbox.insert(0, file_path)
        # TODO: 保存到history.json

    def run(self):
        """启动主循环"""
        self.root.mainloop()
