"""Check for new / old style related problems."""
from __future__ import annotations
from typing import TYPE_CHECKING
import astroid
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import has_known_bases, node_frame_class, only_required_for_messages
from pylint.typing import MessageDefinitionTuple
if TYPE_CHECKING:
    from pylint.lint import PyLinter
MSGS: dict[str, MessageDefinitionTuple] = {'E1003': ('Bad first argument %r given to super()', 'bad-super-call', 'Used when another argument than the current class is given as first argument of the super builtin.')}

class NewStyleConflictChecker(BaseChecker):
    """Checks for usage of new style capabilities on old style classes and
    other new/old styles conflicts problems.

    * use of property, __slots__, super
    * "super" usage
    """
    name = 'newstyle'
    msgs = MSGS
    options = ()

    @only_required_for_messages('bad-super-call')
    def visit_functiondef(self, node: nodes.FunctionDef) -> None:
        """Check use of super."""
        pass
    visit_asyncfunctiondef = visit_functiondef