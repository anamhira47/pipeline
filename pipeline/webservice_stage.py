from aws_cdk import core

from pipeline.pipeline_stack import PipelineStack


class WebServiceStage(core.Stage):
  def __init__(self, scope: core.Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    service = PipelineStack(self, 'WebService')

    