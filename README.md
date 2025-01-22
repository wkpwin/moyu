# 桌面小说阅读器

## 项目概述
本项目是一个简单的Windows桌面小说阅读应用，支持用户不安装任何依赖即可使用。应用具备悬浮球功能，用于控制阅读区域的显示和属性设置。

## 主要功能
- 主界面支持打开txt格式小说文件，并显示历史文件列表，点击文件名进入阅读模式
- 阅读模式
  - 阅读区域显示用户点击的文件进行显示，每次点击更换显示内容
  - 悬浮球全局显示
- 生命周期
  - 三个对象只初始化一次，直到关闭程序。阅读区域只通过通讯模块更改显示内容，不需要重复加载。


## 技术栈
- 编程语言: Python
  - 版本要求: Python 3.7+
  - 优势: 开发效率高，跨平台支持
- GUI库: Tkinter
  - 可行性验证:
    * 支持Toplevel窗口实现悬浮球
    * 支持窗口透明度设置(attributes('-alpha'))
    * 支持全局置顶(attributes('-topmost'))
    * 支持窗口拖动功能
- 打包工具: PyInstaller
  - 可行性验证:
    * 支持打包为独立exe文件
    * 支持包含资源文件
    * 支持隐藏控制台窗口(--windowed)
- 数据存储: JSON
  - 可行性验证:
    * 适合存储简单的键值对数据
    * Python标准库支持
    * 易于读写和维护

## 架构设计
### 模块划分
1. **对象模块** - 独立对象开发
2. **事件模块** - 事件总线管理 
4. **通信模块** - 文件传输实现


## 主要功能
- 支持打开和阅读txt格式小说文件
- 悬浮球控制阅读区域
  - 调整阅读区域透明度
  - 显示/隐藏阅读区域
  - 全局置顶功能
- 阅读历史记录
  - 自动记录上次阅读位置
  - 在文件历史列表中突出显示最近阅读的文件

## 技术栈
- 编程语言: Python
  - 版本要求: Python 3.7+
  - 优势: 开发效率高，跨平台支持
- GUI库: Tkinter
  - 可行性验证:
    * 支持Toplevel窗口实现悬浮球
    * 支持窗口透明度设置(attributes('-alpha'))
    * 支持全局置顶(attributes('-topmost'))
    * 支持窗口拖动功能
- 打包工具: PyInstaller
  - 可行性验证:
    * 支持打包为独立exe文件
    * 支持包含资源文件
    * 支持隐藏控制台窗口(--windowed)
- 数据存储: JSON
  - 可行性验证:
    * 适合存储简单的键值对数据
    * Python标准库支持
    * 易于读写和维护


### 核心对象规范
1. **独立对象声明**
   ```python
   # 主界面对象（main_interface.py）
   class MainInterface:
       def __init__(self):
           self._init_ui()
           self._bind_events()

   # 阅读区域对象（reading_area.py） 
   class ReadingArea:
       def __init__(self):
           self._setup_display()
           self._load_default_style()

   # 悬浮球对象（floating_ball.py）
   class FloatingBall:
       def __init__(self):
           self._create_widget()
           self._enable_drag()
   ```

2. **对象独立性要求**
   - 三个对象分别存储在独立文件
   - 无父子/嵌套关系
   - 通过事件总线进行通信
   - 生命周期与程序共存亡

### 通信机制
1. **文件选择事件流**
   ```mermaid
   sequenceDiagram
   MainInterface->>EventBus: emit_file_selected(path)
   EventBus->>ReadingArea: handle_file_content(path)
   ReadingArea->>core/interface/file_transfer_interface: get_file_content(path)
   core/interface/file_transfer_interface->>core/communication/file_transfer: execute
   core/communication/file_transfer-->>ReadingArea: return content
   ReadingArea->>ReadingArea: update_display(content)
   ```

2. **通信约束**
   - 仅通过event_types预定义事件通信
   - 使用event_bus进行消息路由
   - 禁止直接对象引用

### 代码规范
1. 已删除/废弃内容：
   - 旧版嵌套式UI组件
   - 冗余的事件中转层
   - 废弃的跨进程通信模块
   - 重复的工具类实现

2. 尽可能简化代码，不做不必要的修改，寻求最简方案
 

### 主界面 (MainInterface类)
- 文件上传和选择功能
- 展示打开过的文件历史记录

### 阅读区域 (ReadingArea类)
- 显示小说内容

### 悬浮球 (FloatingBall类)
- 可拖动/并全局置顶

## 使用方法
1. 运行应用后在主界面上传本地的txt文件，在文件列表（显示历史所有打开过的文件）中选择一个文件打开，进入阅读模式
2. 阅读区域显示选中的文件内容
3. 关闭应用时会自动保存，历史列表和阅读进度

## 开发环境
- Python 3.x
- Tkinter (Python标准库)
- PyInstaller

## 打包说明
使用PyInstaller打包成独立可执行文件：
```bash
pyinstaller --onefile --windowed main.py
```

## 未来扩展
- 支持更多文件格式


## 注意事项
对象/事件/通信，分别为独立模块，不可混淆


## 项目结构
```

├── history.json            # 阅读历史记录
├── progress.json           # 阅读进度记录
├── main.py                 # 主程序入口
├── core/                   # 核心功能模块
│   ├── communication/      # 通信模块
│   │   └── file_transfer.py # 文件传输接口
│   ├── events/             # 事件系统模块
│   │   ├── event_bus.py    # 事件总线
│   │   ├── event_manager.py # 事件管理器
│   │   ├── event_handlers.py # 事件处理器
│   │   └── event_types.py  # 事件类型定义
│   └── objects/            # 界面对象模块
│       ├── floating_ball.py # 悬浮球控制
│       ├── main_interface.py # 主界面
│       └── reading_area.py  # 阅读区域
```

## 贡献指南
欢迎提交issue和pull request
