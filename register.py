from functools import wraps
from typing import Callable, List, Tuple

_registered_funcs = []


def MonitorFunc(service_name: str, module_name: str, run_cron: str) -> Callable:
    """将函数注册为监控函数

    Args:
        service_name (str, optional): 服务名称
        module_name (str): 服务模块名称
        run_cron (str, optional): 运行规则 cron 表达式

    Returns:
        Callable: 原函数
    """
    def outer(func: Callable):
        @wraps(func)
        def inner(service_name, module_name, run_cron):
            _registered_funcs.append((service_name, module_name, run_cron, func))
            return func
        return inner(service_name, module_name, run_cron)
    return outer


def GetAllRegisteredFuncs() -> List[Tuple[str, str, str, Callable]]:
    """获取注册的监控函数列表

    Returns:
        List[Tuple[str, str, str, Callable]]: 注册的监控函数列表
    """
    return _registered_funcs
