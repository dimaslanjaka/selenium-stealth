from typing import List, Optional

from selenium.webdriver import Chrome as Driver

from .ansi import AnsiFormatter
from .chrome_app import chrome_app
from .chrome_runtime import chrome_runtime
from .hairline_fix import hairline_fix
from .iframe_content_window import iframe_content_window
from .main import stealth, stealth2
from .media_codecs import media_codecs
from .navigator_languages import navigator_languages
from .navigator_permissions import navigator_permissions
from .navigator_plugins import navigator_plugins
from .navigator_vendor import navigator_vendor
from .navigator_webdriver import navigator_webdriver
from .preferences import Preferences
from .user_agent_override import user_agent_override
from .utils import read_json_file, with_utils
from .webgl_vendor import webgl_vendor_override
from .window_outerdimensions import window_outerdimensions
