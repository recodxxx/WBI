class WBI:
    def __init__(self, modules):
        self.consciousness = SelfAwarenessModule()
        self.intuition = HeuristicPatternRecognitionModule()
        self.imagination = CounterfactualSimulatorModule()
        self.emotion = ValueAffectionModule()
        self.sociality = EmpathicInteractionModule()

        self.integration = GlobalWorkspaceTheoryModule()
        self.adaptation = LearningFromExperienceModule()

        self.modules = dict(zip(['con', 'int', 'ima', 'emp', 'soc'], [self.consciousness, self.intuition, self.imagination,
                                self.emotion, self.sociality]))
        self.global_workspace = list(modules.values())

    def perceive(self, stimulus):
        processed_stimuli = [mod.encode(stimulus) for _, mod in self.modules.items()]
        return self.integration.fuse(*processed_stimuli)

    def decide(self, goals):
        candidate_decisions = [mod.generate_option(goals) for _, mod in self.modules.items()]
        chosen_decision = self.integration.select(candidate_decisions)
        return chosen_decision

    def execute(self, choice):
        executed_choice = self.modules[list(self.modules.keys())[self.integration.focus]].implement(choice)
        self.adaptation.learn(executed_choice)
        return executed_choice

wbi = WBI([SelfAwarenessModule(), HeuristicPatternRecognitionModule(),
             CounterfactualSimulatorModule(), ValueAffectionModule(),
             EmpathicInteractionModule(), GlobalWorkspaceTheoryModule(),
             LearningFromExperienceModule()])

input_stimulus = collect_sensor_information()
desired_goals = formulate_aspirations()
selected_action = wbi.perceive(input_stimulus).decide(desired_goals).execute()
