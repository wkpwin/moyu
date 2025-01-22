import tkinter as tk
from tkinter import filedialog
import json
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
        try:
            with open('history.json', 'r', encoding='utf-8') as f:
                history = json.load(f)
                for file_path in history:
                    self.history_listbox.insert(0, file_path)
        except (FileNotFoundError, json.JSONDecodeError):
            # 文件不存在或格式错误时初始化空列表
            self.history_listbox.delete(0, tk.END)

    def _add_to_history(self, file_path: str):
        """添加文件到历史记录"""
        # 如果文件已存在则先移除
        items = self.history_listbox.get(0, tk.END)
        if file_path in items:
            index = items.index(file_path)
            self.history_listbox.delete(index)
        
        # 插入到最前面
        self.history_listbox.insert(0, file_path)
        
        # 保存到文件
        items = self.history_listbox.get(0, tk.END)
        history = list(items)[:100]  # 最多保存100条记录
        with open('history.json', 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

    def run(self):
        """启动主循环"""
        self.root.mainloop()
