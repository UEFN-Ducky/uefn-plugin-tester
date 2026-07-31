"""Tester — Store desktop plugin (gates core tool modules)."""

from __future__ import annotations


def register(api) -> None:
    """Import gated MCP tools onto the shared FastMCP instance."""
    import backend.tools.tester.suite  # noqa: F401
    api.log("tester tools registered")
