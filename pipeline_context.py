# pipeline_context.py
MODULE_NAME = "PIPELINE_CONTEXT"

class PipelineContext:
    def __init__(self):
        self.request_id = None
        self.start_perf_counter = None
        self.start_time = None
        
        self.base_prompt = None
        self.system_prompt = None
        self.model_configurations = None
        self.stages = None
        self.evaluation_stage = None
        self.scoring_stage = None

        self.current_stage = None
        self.current_stage_data = None

        self.stages_output = {}

        self.initial_structured = None
        self.consensus_structured = None
        self.scoring_structured = None
        self.weighted_scores = None
        
        self.winner_details = None
        self.end_time = None
        self.execution_time = None

    
    def set_stage_output(self, stage_name, outputs=None, structured=None):
        if stage_name not in self.stages_output:
            self.stages_output[stage_name] = {
                "outputs": None,
                "structured": None
            }

        if outputs is not None:
            self.stages_output[stage_name]["outputs"] = outputs

        if structured is not None:
            self.stages_output[stage_name]["structured"] = structured