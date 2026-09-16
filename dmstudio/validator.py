'''
dmstudio.validator
------------------

Pre-flight CLI command parser linter and safe validator for Datamine Studio RM.

Inspects command strings prior to dispatching to COM Parsecommand to prevent
parser crashes, deadlocks, and silent execution errors.

Interface (seam):
    lint_command(command: str) -> list[str]
    validate_command(command: str, strict: bool = False) -> list[str]

No COM, threading, or external dependencies — safe to run in any context,
including offline unit tests without Datamine Studio RM installed.
'''

import re
import warnings

# Pattern matching parameter tokens (&file, *field, @param) preceded by alphanumeric, closing delimiter, or empty assignment
_ADJACENT_PARAM_PATTERN = re.compile(
    r'(?:(?<=[a-zA-Z0-9_\'"\)\}])([&*@][a-zA-Z_][a-zA-Z0-9_]*))|'
    r'(?:(?<==)([&@][a-zA-Z_][a-zA-Z0-9_]*))'
)


def lint_command(command):
    '''
    lint_command
    ------------

    Inspect a Datamine command string for common syntax errors and unsafe patterns
    that cause Parsecommand() crashes, silent failures, or COM server deadlocks.

    Checks:
    1. Windows backslashes ('\\') - causes Parsecommand() crashes or deadlocks.
    2. Missing whitespace before parameter tokens (&file, *field, @param)
       adjacent to preceding arguments or closing delimiters.

    Retrieval blocks and expressions enclosed in braces {...} are protected
    from false positives.

    Parameters:
    -----------
    command: str
        Raw Datamine CLI command string.

    Returns:
    --------
    list of str
        List of human-readable diagnostic issue descriptions with remediation advice.
        Empty list if no issues are found.
    '''
    if not isinstance(command, str):
        return ['Command must be a string, got ' + type(command).__name__ + '.']

    issues = []

    # 1. Inspect for Windows backslashes
    if '\\' in command:
        issues.append(
            'Windows backslash (\'\\\') detected in command string. Datamine\'s command parser '
            '(Parsecommand) does not support Windows file paths with backslashes and may deadlock or crash. '
            'Use logical file names residing in the active project directory, or register external files '
            'with the active project first using ActiveProject.AddFile(absolute_path).'
        )

    # 2. Inspect for missing whitespace before parameter tokens (&, *, @)
    # Mask out inner contents of retrieval blocks {...} while keeping braces intact
    def _mask_braces(m):
        content = m.group(0)
        if len(content) <= 2:
            return content
        return content[0] + (' ' * (len(content) - 2)) + content[-1]

    masked = re.sub(r'\{[^{}]*\}', _mask_braces, command)

    # Mask string literal contents while preserving quotes
    def _mask_quotes(m):
        content = m.group(0)
        if len(content) <= 2:
            return content
        return content[0] + (' ' * (len(content) - 2)) + content[-1]

    masked = re.sub(r'"[^"]*"', _mask_quotes, masked)
    masked = re.sub(r"'[^']*'", _mask_quotes, masked)

    for match in _ADJACENT_PARAM_PATTERN.finditer(masked):
        token = match.group(1) or match.group(2)
        start_idx = match.start()
        end_idx = match.end()
        snippet_start = max(0, start_idx - 12)
        snippet_end = min(len(command), end_idx + 12)
        context = command[snippet_start:snippet_end]
        issues.append(
            f"Missing whitespace before parameter token '{token}'. Datamine CLI parameters "
            f"(&file, *field, @param) must be separated by whitespace from adjacent arguments "
            f"(near '...{context}...'). Concatenated parameters cause silent parse failures or server freezes."
        )

    return issues


def validate_command(command, strict=False):
    '''
    validate_command
    ----------------

    Validate a Datamine command string before dispatching to Studio RM's COM Parsecommand.

    Parameters:
    -----------
    command: str
        Raw Datamine CLI command string.
    strict: bool, optional
        If True, raises ValueError when any issue is detected.
        If False (default), emits a UserWarning and returns the detected issues.

    Returns:
    --------
    list of str
        List of diagnostic issue descriptions. Empty if valid.

    Raises:
    -------
    ValueError
        If strict=True and one or more issues are detected.
    '''
    issues = lint_command(command)
    if issues:
        message = (
            f'Pre-flight command validation detected {len(issues)} issue(s):\n'
            + '\n'.join(f' - {issue}' for issue in issues)
        )
        if strict:
            raise ValueError(message)
        warnings.warn(message, UserWarning, stacklevel=2)
    return issues
