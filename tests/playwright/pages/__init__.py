# -*- coding: utf-8 -*-
"""Location: ./tests/playwright/pages/__init__.py
Copyright 2025
SPDX-License-Identifier: Apache-2.0
Authors: Mihai Criveti

Page objects for Playwright tests.
"""

# Local
from .admin_page import AdminPage
from .agents_page import AgentsPage
from .base_page import BasePage
from .gateways_page import GatewaysPage
from .login_page import LoginPage
from .mcp_registry_page import MCPRegistryPage
from .metrics_page import MetricsPage
from .prompts_page import PromptsPage
from .resources_page import ResourcesPage
from .sandbox_page import SandboxPage
from .servers_page import ServersPage
from .team_page import TeamPage
from .tokens_page import TokensPage
from .tools_page import ToolsPage
from .version_page import VersionPage

__all__ = [
    "BasePage",
    "LoginPage",
    "AdminPage",
    "AgentsPage",
    "GatewaysPage",
    "TeamPage",
    "TokensPage",
    "ToolsPage",
    "MetricsPage",
    "ResourcesPage",
    "PromptsPage",
    "SandboxPage",
    "ServersPage",
    "VersionPage",
    "MCPRegistryPage",
]
