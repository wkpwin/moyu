class EventTypes:
    """事件类型定义"""
    FILE_SELECTED = 'file_selected'  # 文件选择事件
    FILE_CONTENT_LOADED = 'file_content_loaded'  # 文件内容加载完成
    FILE_LOAD_ERROR = 'file_load_error'  # 文件加载错误
    
    # 阅读区域相关事件
    UPDATE_DISPLAY = 'update_display'  # 更新显示内容
    TOGGLE_VISIBILITY = 'toggle_visibility'  # 切换显示/隐藏
    CHANGE_OPACITY = 'change_opacity'  # 改变透明度
    
    # 悬浮球相关事件
    DRAG_START = 'drag_start'  # 开始拖动
    DRAG_END = 'drag_end'  # 结束拖动
    CLICK = 'click'  # 点击事件
