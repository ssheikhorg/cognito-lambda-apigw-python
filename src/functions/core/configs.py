from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings, Field


class ServerConfig(BaseSettings):
    host: str = Field(None, env="HOST")
    port: int = Field(None, env="PORT")
    app_name: str = Field(None, env="APP_NAME")
    debug: bool = Field(None, env="DEBUG")


class IDriveConfig(BaseSettings):
    reseller_api_key: str = Field(None, env="IDRIVE_RESELLER_API_KEY")
    reseller_base_url: str = Field(None, env="IDRIVE_RESELLER_BASE_URL")


class AwsConfig(BaseSettings):
    aws_access_key: str = Field(None, env="AWS_ACCESS_KEY")
    aws_secret_key: str = Field(None, env="AWS_SECRET_KEY")
    aws_default_region: str = Field(None, env="AWS_DEFAULT_REGION")
    aws_account_id: str = Field(None, env="AWS_ACCOUNT_ID")


class VPCConfig(BaseSettings):
    vpc_id: str = Field(None, env="VPC_ID")
    vpc_security_group_id: str = Field(None, env="SECURITY_GROUP_ID")


class UserPoolConfig(BaseSettings):
    up_id: str = Field(None, env="UP_ID")
    up_client_id: str = Field(None, env="UP_CLIENT_ID")
    up_client_secret: str = Field(None, env="UP_CLIENT_SECRET")
    up_arn: str = Field(None, env="UP_ARN")

    # user group settings
    ug_admin_arn: str = Field(None, env="UG_ADMIN_ARN")
    ug_user_arn: str = Field(None, env="UG_USER_ARN")
    # temporary callback urls
    cognito_callback_url: str = Field(None, env="COGNITO_CALLBACK_URL")
    cognito_logout_url: str = Field(None, env="COGNITO_LOGOUT_URL")


class FactoryConfig(ServerConfig, IDriveConfig, AwsConfig, UserPoolConfig, VPCConfig):
    class Config:
        env_file = ".env" if Path(".env").exists() else "src/.env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return FactoryConfig()


settings = get_settings()