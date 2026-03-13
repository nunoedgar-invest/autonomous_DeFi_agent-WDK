"""
Strategy Loader for Autonomous DeFi Agent

Responsible for discovering and loading strategy modules
from the /strategies directory.

All strategies must inherit from BaseStrategy.
"""

import os
import importlib
import inspect
from typing import List

from strategies.base_strategy import BaseStrategy


class StrategyLoader:

    def __init__(self, strategies_path: str = "strategies"):
        """
        Initialize the strategy loader.

        Args:
            strategies_path (str): directory containing strategy modules
        """
        self.strategies_path = strategies_path
        self.strategies: List[BaseStrategy] = []

    def discover_strategy_modules(self):
        """
        Discover strategy files inside the strategies directory.
        """

        modules = []

        for file in os.listdir(self.strategies_path):

            if not file.endswith(".py"):
                continue

            if file.startswith("_"):
                continue

            if file == "base_strategy.py":
                continue

            module_name = file[:-3]
            modules.append(module_name)

        return modules

    def load_module(self, module_name: str):
        """
        Import a strategy module dynamically.
        """

        module_path = f"{self.strategies_path}.{module_name}"

        try:
            module = importlib.import_module(module_path)
            return module

        except Exception as e:
            print(f"[StrategyLoader] Failed to import {module_name}: {e}")
            return None

    def find_strategy_classes(self, module):
        """
        Find classes that inherit from BaseStrategy.
        """

        classes = []

        for _, obj in inspect.getmembers(module, inspect.isclass):

            if issubclass(obj, BaseStrategy) and obj is not BaseStrategy:
                classes.append(obj)

        return classes

    def instantiate_strategies(self, classes):
        """
        Instantiate strategy classes.
        """

        instances = []

        for strategy_class in classes:

            try:
                instance = strategy_class()
                instances.append(instance)

                print(f"[StrategyLoader] Loaded strategy: {instance.name}")

            except Exception as e:
                print(f"[StrategyLoader] Failed to instantiate {strategy_class}: {e}")

        return instances

    def load_strategies(self):
        """
        Full strategy loading pipeline.
        """

        modules = self.discover_strategy_modules()

        print(f"[StrategyLoader] Found modules: {modules}")

        for module_name in modules:

            module = self.load_module(module_name)

            if not module:
                continue

            classes = self.find_strategy_classes(module)

            instances = self.instantiate_strategies(classes)

            self.strategies.extend(instances)

        print(f"[StrategyLoader] Total strategies loaded: {len(self.strategies)}")

        return self.strategies


