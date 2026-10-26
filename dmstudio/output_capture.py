import os
import re
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Generator, List, Optional, Tuple


@dataclass
class ExecutionResult:
    '''
    ExecutionResult
    ---------------
    Structured diagnostic result representing the execution of a Datamine process or workflow.
    '''
    success: bool = True
    output: str = ''
    duration: float = 0.0
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    command: str = ''

    def __bool__(self) -> bool:
        return self.success

    def __str__(self) -> str:
        return self.output


TIMESTAMP_PREFIX = re.compile(r'^\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}:\d{2}\s*:\s*')

ERROR_PATTERNS = [
    re.compile(r'>>>\s*ERROR.*', re.IGNORECASE),
    re.compile(r'Fatal\s*:.*', re.IGNORECASE),
    re.compile(r'Process failed.*', re.IGNORECASE),
    re.compile(r'Error\s*:.*', re.IGNORECASE),
    re.compile(r'.*DOES NOT EXIST.*', re.IGNORECASE),
    re.compile(r'.*CANNOT OPEN FILE.*', re.IGNORECASE),
    re.compile(r'.*SYNTAX ERROR.*', re.IGNORECASE),
    re.compile(r'.*INVALID FIELD.*', re.IGNORECASE),
    re.compile(r'.*INVALID PARAMETER.*', re.IGNORECASE),
]

WARNING_PATTERNS = [
    re.compile(r'>>>\s*WARNING.*', re.IGNORECASE),
    re.compile(r'Warning\s*:.*', re.IGNORECASE),
]

SUCCESS_PATTERNS = [
    re.compile(r'>>>\s*[\w\d_]+\s+Complete\s*<<<', re.IGNORECASE),
    re.compile(r'Process complete', re.IGNORECASE),
]


def classify_log_delta(text: str) -> Tuple[bool, List[str], List[str]]:
    '''
    classify_log_delta
    ------------------
    Inspects Datamine Command Window / Command.log text delta to determine
    whether the command succeeded, and extracts error or warning messages.

    Parameters:
    -----------
    text: str
        Raw log slice generated during command execution.

    Returns:
    --------
    Tuple[bool, List[str], List[str]]:
        (success, errors_list, warnings_list)
    '''
    errors: List[str] = []
    warnings: List[str] = []
    has_success_token = False

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        matched_err = False
        for pattern in ERROR_PATTERNS:
            if pattern.search(line):
                cleaned = TIMESTAMP_PREFIX.sub('', line)
                errors.append(cleaned)
                matched_err = True
                break

        if not matched_err:
            for pattern in WARNING_PATTERNS:
                if pattern.search(line):
                    cleaned = TIMESTAMP_PREFIX.sub('', line)
                    warnings.append(cleaned)
                    break

        if not has_success_token:
            for pattern in SUCCESS_PATTERNS:
                if pattern.search(line):
                    has_success_token = True
                    break

    if errors:
        success = False
    elif has_success_token:
        success = True
    else:
        success = True

    return success, errors, warnings


class CommandLogCapture:
    '''
    CommandLogCapture
    -----------------
    Monitors and captures real-time log output streamed by Studio RM into Command.log.
    '''

    def __init__(self, log_path: Optional[str] = None):
        if log_path is None:
            self.log_path = self.default_log_path()
        else:
            self.log_path = log_path
        self._start_offset = 0

    @staticmethod
    def default_log_path() -> str:
        appdata = os.environ.get('APPDATA', '')
        return os.path.join(appdata, 'Datamine', 'StudioRM', 'Command.log')

    def mark(self) -> None:
        '''Record the current end-of-file seek offset.'''
        if os.path.exists(self.log_path):
            try:
                self._start_offset = os.path.getsize(self.log_path)
            except OSError:
                self._start_offset = 0
        else:
            self._start_offset = 0

    def get_delta(self) -> str:
        '''
        Return any newly appended text in Command.log since the last mark().
        '''
        if not os.path.exists(self.log_path):
            return ''

        try:
            current_size = os.path.getsize(self.log_path)
            if current_size <= self._start_offset:
                return ''

            with open(self.log_path, 'r', encoding='utf-8', errors='replace') as f:
                f.seek(self._start_offset)
                content = f.read()
            return content
        except OSError:
            return ''


@contextmanager
def command_capture(capture: Optional[CommandLogCapture] = None) -> Generator[ExecutionResult, None, None]:
    '''
    command_capture
    ---------------
    Context manager to capture and classify Datamine Command Window logs produced during a block.

    Usage:
    ------
    >>> with command_capture() as res:
    ...     dmc.mgsort(in_i='collars', out_o='sorted', keys_f=['BHID'])
    >>> print(res.success, res.output)
    '''
    if capture is None:
        capture = CommandLogCapture()

    res = ExecutionResult()
    start_time = time.time()
    capture.mark()

    try:
        yield res
    finally:
        delta = capture.get_delta()
        res.duration = time.time() - start_time
        res.output = delta
        res.success, res.errors, res.warnings = classify_log_delta(delta)
