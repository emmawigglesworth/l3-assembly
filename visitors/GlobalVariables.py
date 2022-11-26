import ast
from asyncio.windows_events import NULL


class GlobalVariableExtraction(ast.NodeVisitor):
    """ 
        We extract all the left hand side of the global (top-level) assignments
    """

    def __init__(self) -> None:
        super().__init__()
        self.results = dict()

    def visit_Assign(self, node):
        if len(node.targets) != 1:
            raise ValueError("Only unary assignments are supported")
        if type(node.value) == ast.Constant:  # if int value is known
            self.results[node.targets[0].id] = node.value.value
        else:
            self.results[node.targets[0].id] = None

    def visit_FunctionDef(self, node):
        """We do not visit function definitions, they are not global by definition"""
        pass
