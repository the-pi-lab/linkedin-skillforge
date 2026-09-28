"""Example tool adapter (stdlib only). Copy and replace stubs with real SDK calls.

Implements a subset of adapters/interfaces.json. Keeps interface names stable
so skills remain provider-agnostic.
"""
from __future__ import annotations
from datetime import datetime, timezone


class ExampleAdapter:
    """In-memory stub. Replace internals with LinkedIn API / CRM / DB calls."""

    def capabilities(self):
        return ["search", "get_profile", "get_company", "create_crm_record"]

    def search(self, query, filters=None):
        return [{
            "title": f"Illustrative result for {query}",
            "url": "https://www.linkedin.com/in/example",
            "snippet": "Replace with real provider call.",
            "source_ref": "tool:search:stub-1",
        }]

    def get_profile(self, handle_or_urn):
        now = datetime.now(timezone.utc).isoformat()
        return {
            "handle": handle_or_urn,
            "display_name": "Example Person (stub)",
            "headline": "Replace stub with real get_profile call",
            "fetched_at": now,
            "source_ref": f"tool:get_profile:{handle_or_urn}",
        }

    def get_company(self, slug_or_urn):
        return {
            "slug": slug_or_urn,
            "name": "Example Co (stub)",
            "source_ref": f"tool:get_company:{slug_or_urn}",
        }

    def create_crm_record(self, record):
        return {
            "ok": True,
            "provider": "stub",
            "id": "crm_stub_001",
            "at": datetime.now(timezone.utc).isoformat(),
        }
