# %%
# The next two lines take care of auto-reloading modules that are included.
#! %load_ext autoreload
#! %autoreload 2
import sys

sys.path.insert(0, "../../")
# %%
from {{ cookiecutter.project_name.lower().replace('-', '_') }}.Animal import Animal

tiger = Animal("Tiger", "roooar")
tiger.speak()
