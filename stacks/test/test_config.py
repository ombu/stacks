import unittest
import os

from stacks.config import (
    config_load,
    config_get_account_id,
    config_get_project_name,
    config_get_stack_region,
)


class TestConfig(unittest.TestCase):
    def setUp(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.config = config_load(os.path.join(path, "test_config.yaml"))

    def test_config_get_account_id(self):
        self.assertEqual(
            config_get_account_id(self.config, "instance", "testing1"), "637300000123"
        )

    def test_config_get_project_name(self):
        self.assertEqual(config_get_project_name(self.config), "stacks")

    def test_get_cluster_region(self):
        region = config_get_stack_region(self.config, "cluster", "core")
        self.assertEqual("us-west-2", region)

    def test_get_instance_region(self):
        region = config_get_stack_region(self.config, "application", "testing1")
        self.assertEqual("us-east-1", region)


if __name__ == "__main__":
    unittest.main()
