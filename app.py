#!/usr/bin/env python3

import aws_cdk as cdk

from infrastructure.be3_stack import Be3cloudApi
from src.functions.core.config import settings as c

app = cdk.App()
env_eu = cdk.Environment(account=c.aws_account_id, region=c.aws_default_region)

Be3cloudApi(app, f"be3-stack-{c.env_state}", env=env_eu)

app.synth()
