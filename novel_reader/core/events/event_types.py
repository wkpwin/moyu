from enum import Enum

class EventType(Enum):
    """事件类型枚举"""
    
    # 文件相关事件
    FILE_OPENED = "file_opened"  # 文件打开事件
    FILE_CLOSED = "file_closed"  # 文件关闭事件
    
    # 阅读相关事件
    READING_STARTED = "reading_started"  # 开始阅读
    READING_PAUSED = "reading_paused"    # 暂停阅读
    READING_RESUMED = "reading_resumed"  # 恢复阅读
    READING_FINISHED = "reading_finished"  # 完成阅读
    
    # 进度相关事件
    PROGRESS_UPDATED = "progress_updated"  # 阅读进度更新
    PROGRESS_SAVED = "progress_saved"      # 进度保存
    PROGRESS_LOADED = "progress_loaded"    # 进度加载
    
    # 界面相关事件
    WINDOW_SHOWN = "window_shown"        # 窗口显示
    WINDOW_HIDDEN = "window_hidden"      # 窗口隐藏
    WINDOW_TOGGLED = "window_toggled"    # 窗口切换状态
    TRANSPARENCY_CHANGED = "transparency_changed"  # 透明度改变
    
    # 系统相关事件
    APP_STARTED = "app_started"          # 应用启动
    APP_EXITING = "app_exiting"          # 应用退出
