#!/usr/bin/python
# Filename: nbstream_readerwriter.py

import shutil
from threading import Thread
from Queue import Queue, Empty
from assert_variable_type import *

class NonBlockingStreamReaderWriter:
    """A non-blocking stream reader/writer
    """

    def __init__(self, stream, print_stream=True, log_file=None):
        """Initialize the stream reader/writer

        Positional arguments:
        stream -- the stream to read from.
                  Usually a process' stdout or stderr.
        log_file -- the file to write the stream output to
        """
        # Queue to hold stream
        self._q = Queue()
        # string to hold cumulative output
        self._output = ""
        # verify arguments
        assert_variable_type(log_file, [str, NoneType])
        assert_variable_type(stream, FileType)

        def _populate_queue(stream, queue, log_file):
            """ Collect lines from 'stream', put them in 'queue'.
            Write the stream output to the log_file if it was supplied.
            """
            while True:
                line = stream.readline()
                if line:
                    queue.put(line)
                    if print_stream:
                        print(line)
                    self._output += line + "\r\n"
                    if log_file is not None:
                        with open(log_file, 'a') as f:
                            f.write(line)
                else:
                    return

        self._t = Thread(target = _populate_queue,
                         args = (stream, self._q, log_file))
        self._t.daemon = True
        self._t.start() #start collecting lines from the stream

    def get_all_output(self):
        return self._output

    def readline(self, timeout = 0.1):
        """Try to read a line from the stream queue.
        """
        try:
            return self._q.get(block = timeout is not None,
                               timeout = timeout)
        except Empty:
            return None

class UnexpectedEndOfStream(Exception): pass
