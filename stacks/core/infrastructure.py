"""
Serverless Telegram Bot - Infrastructure
-------------------------

This module contains the :py:class:`CoreStack` class for creating all required service resources in the stack.

Classes:
    - :py:class:`CoreStack`: Creates the required service resources.

Author: Stan Fateev
Project: Serverless Telegram Bot
"""

from aws_cdk import (
    App,
    Aws,
    Environment,
    DefaultStackSynthesizer,
    PermissionsBoundary,
    Stack,
    Tags,
)
from config.settings import Config
from config.constants import PROJECT_NAME


class CoreStack(Stack):
    def __init__(
        self,
        scope: App,
        id: str,
        config: Config,
        env: Environment,
    ):
        super().__init__(
            scope=scope,
            id=id,
            description="Contains the core resources for Serverless Telegram Bot.",
            permissions_boundary=PermissionsBoundary.from_name(
                f"cdk-{DefaultStackSynthesizer.DEFAULT_QUALIFIER}-permissions-boundary-{Aws.ACCOUNT_ID}-{Aws.REGION}"
            ),
            env=env,
        )
        Tags.of(self).add(
            key="project",
            value=PROJECT_NAME,
        )
        Tags.of(self).add(
            key="environment",
            value=config.env_name,
        )
        Tags.of(self).add(
            key="delivery-context",
            value=config.delivery_context,
        )
        Tags.of(self).add(
            key="location",
            value=config.region_full,
        )
        Tags.of(self).add(
            key="stack-name",
            value=self.stack_name,
        )
