import os
import yaml


class ConfigLoader:
    """Advanced configuration loader for managing YAML files and environment variables."""

    def __init__(self, config_file="config.yaml", env_prefix="AETHER_"):
        """
        Initialize the configuration loader.
        :param config_file: Path to the YAML configuration file.
        :param env_prefix: Prefix for environment variables (default: 'AETHER_').
        """
        self.config_file = config_file
        self.env_prefix = env_prefix
        self.config = self._load_config()

    def _load_config(self):
        """Load configuration from the YAML file and merge with environment variables."""
        try:
            with open(self.config_file, "r") as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Warning: Configuration file '{self.config_file}' not found. Using environment variables only.")
            config = {}

        # Merge with environment variables
        return self._merge_with_env(config)

    def _merge_with_env(self, config):
        """Merge configuration with environment variables."""
        for key, value in config.items():
            if isinstance(value, dict):
                config[key] = self._merge_with_env(value)
            else:
                env_key = f"{self.env_prefix}{key.upper()}"
                config[key] = os.getenv(env_key, value)
        return config

    def get(self, key, default=None):
        """Retrieve a configuration value."""
        return self._nested_get(self.config, key, default)

    def _nested_get(self, config, key, default):
        """Retrieve nested keys from the configuration."""
        keys = key.split(".")
        for k in keys:
            if isinstance(config, dict):
                config = config.get(k)
            else:
                return default
        return config or default

    def set(self, key, value):
        """Set a configuration value dynamically."""
        keys = key.split(".")
        cfg = self.config
        for k in keys[:-1]:
            cfg = cfg.setdefault(k, {})
        cfg[keys[-1]] = value

    def reload(self):
        """Reload the configuration file."""
        self.config = self._load_config()