#!/usr/bin/env python3

"""
Runtime Decision Trace Utility

Used during testing to print decision flow inside SNASHGPT.
This is NOT used in production messaging.
"""

TRACE_ENABLED = True


def trace(step, value):
    if not TRACE_ENABLED:
        return
    print(f"[TRACE] {step}: {value}")
