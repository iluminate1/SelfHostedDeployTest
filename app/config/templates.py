from pathlib import Path

from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig

from app.config.constants import TEMPLATES_PATH

template_config = TemplateConfig(
    directory=Path(__file__).parent.parent / TEMPLATES_PATH,
    engine=JinjaTemplateEngine,
)
"""Template config for app."""
