"""Tester pipeline tiles — catalog + register, no app imports."""

from __future__ import annotations

import json
from pathlib import Path

from . import automations


def test_plugin_json_lists_playtest_nodes():
    data = json.loads((Path(__file__).resolve().parents[1] / "plugin.json").read_text(encoding="utf-8"))
    ids = {n["id"] for n in data["contributes"]["automations"]["nodes"]}
    assert ids == {
        "uefn.game.start",
        "uefn.player.wait",
        "uefn.player.teleport",
        "uefn.log.expect",
    }


def test_register_nodes():
    names: list[str] = []

    class Api:
        def register_automation_node(self, name, _fn):
            names.append(name)

    automations.register_nodes(Api())
    assert names == [
        "uefn.game.start",
        "uefn.player.wait",
        "uefn.player.teleport",
        "uefn.log.expect",
    ]
