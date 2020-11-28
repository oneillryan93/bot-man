from aws_cdk import (
    aws_iam as iam,
    aws_lambda as l,
    core
)


class InsiderStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        resource_layer = l.LayerVersion(
            self, 'ResourceLayer',
            code=l.Code.asset('./repos/resources'),
            compatible_runtimes=[l.Runtime.PYTHON_3_8],
            layer_version_name="resource_layer",
            license="MIT"
        )

        request_movers = l.Function(
            self, "RetrieveMovers",
            runtime=l.Runtime.PYTHON_3_8,
            code=l.Code.asset("./repos/python"),
            handler="retrieve_movers.handler",
            layers=[resource_layer],
        )

        request_movers.role.add_managed_policy(
            iam.ManagedPolicy.from_managed_policy_arn(self,
                                                      id="AWSLambda_FullAccess",
                                                      managed_policy_arn="arn:aws:iam::aws:policy/AWSLambda_FullAccess")
        )
