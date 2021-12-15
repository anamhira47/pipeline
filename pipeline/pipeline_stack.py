from aws_cdk import core
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from aws_cdk import pipelines




# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.



class PipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "PipelineQueue",
        #     visibility_timeout=cdk.Duration.seconds(300),
        # )

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()
        
        pipeline = pipelines.CdkPipeline(self, 'Pipeline',

            cloud_assembly_artifact=cloud_assembly_artifact,
            pipeline_name='trainerPipeline',

            source_action=cpactions.GitHubSourceAction(
                action_name='Github',
                output=source_artifact,
                oauth_token=core.SecretValue.secrets_manager('trainer-github-token'),
                owner='ic-crc', #"GITHUB-OWNER"
                repo='vrd20-postaccel', #"GITHUB-REPO",
                branch='main',
                trigger=cpactions.GitHubTrigger.POLL),

            synth_action=pipelines.SimpleSynthAction(
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assembly_artifact,
                install_command='npm install -g aws-cdk && pip install -r requirements.txt',
                synth_command= 'cdk synth'))

        #pipeline.add_application_stage(WebServiceStage(self,'Pre-Produc',env={

#  'account':'913822692686', #account
   # 'region': 'ca-central-1' #region
#}))

        



