from memory.short_term.conversation import ConversationMemory
from memory.short_term.working_context import WorkingContext
from memory.long_term.user_profile import UserProfile
from memory.long_term.preferences import Preferences
from memory.long_term.facts import FactsStore
from memory.episodic.events import EventLog
from memory.episodic.actions import ActionLog
from memory.episodic.outcomes import OutcomeLog
from memory.semantic.concepts import ConceptStore
from memory.semantic.relations import RelationStore

class MemoryManager:
    def __init__(self):
        self.conversation = ConversationMemory()
        self.context = WorkingContext()

        self.profile = UserProfile()
        self.preferences = Preferences()
        self.facts = FactsStore()

        self.events = EventLog()
        self.actions = ActionLog()
        self.outcomes = OutcomeLog()

        self.concepts = ConceptStore()
        self.relations = RelationStore()

    def snapshot(self) -> dict:
        return {
            "conversation": self.conversation.get(),
            "context": self.context.snapshot(),
            "profile": self.profile.get(),
            "preferences": self.preferences.all(),
            "facts": self.facts.list(),
            "events": self.events.list(),
            "actions": self.actions.list(),
            "outcomes": self.outcomes.list(),
            "concepts": self.concepts.all(),
            "relations": self.relations.list()
        }
