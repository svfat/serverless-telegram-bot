from dataclasses import dataclass


@dataclass
class Config:
    """
    Configuration settings for the CDK application.
    """

    env_name: str
    aws_account_id: str
    delivery_context: str
    resource_prefix: str
    region_full: str
    log_retention: int
