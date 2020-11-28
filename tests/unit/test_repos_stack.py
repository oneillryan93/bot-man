import json
import pytest

from aws_cdk import core
from repos.insider_stack import InsiderStack


def get_template():
    app = core.App()
    InsiderStack(app, "repos")
    return json.dumps(app.synth().get_stack("repos").template)


def test_lambda_created():
    assert("AWS::Lambda::Function" in get_template())


def test_lambda_layer_created():
    assert("AWS::Lambda::LayerVersion" in get_template())
