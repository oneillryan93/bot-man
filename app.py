#!/usr/bin/env python3

from aws_cdk import core
from repos.insider_stack import InsiderStack


app = core.App()
InsiderStack(app, "InsiderStack", env=core.Environment(account="344304453900", region="us-east-1"))

app.synth()
