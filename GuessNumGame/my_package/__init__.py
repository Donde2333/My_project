# my_package/__init__.py


# 导入包内模块，简化外部访问
from .logic import guess_number_game
from .ranking import RankingManager
from .user import User


# 包级变量
__version__ = "1.0.0"
package_name = "My Package"

# 当使用 from package import * 时的行为
__all__ = ['guess_number_game', 'RankingManager', 'User']
