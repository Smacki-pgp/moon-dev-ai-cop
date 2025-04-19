"""
🌙 Moon Dev's Custom Strategies Package
"""
from src.strategies.base_strategy import BaseStrategy
from .example_strategy import ExampleStrategy
from .private_flux_vwap import FluxVWAPStrategy

__all__ = ['ExampleStrategy', 'MyStrategy'] 