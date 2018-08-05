import os

from twisted.internet.defer import inlineCallbacks, returnValue
from labrad.wrappers import connectAsync

from server_tools.connections.connection import Connection

class SerialConnection(Connection):
    @inlineCallbacks
    def initialize(self, device):
        yield self.connect(device)
        self.server = yield self.connection[device.servername]
        yield self.server.select_interface(device.address)
        
        for attr in ['timeout', 'baudrate', 'stopbits', 'bytesize']:
            if hasattr(device, attr): 
                value = getattr(device, attr)
                yield getattr(self.server, attr)(value)
    
    @inlineCallbacks
    def baudrate(self, x=None):
        ans = yield self.server.baudrate(x)
        returnValue(ans)
   
    @inlineCallbacks
    def timeout(self, x=None):
        ans = yield self.server.timeout(x)
        returnValue(ans)
    
    @inlineCallbacks
    def write(self, x):
        ans = yield self.server.write(x)
        returnValue(ans)

    @inlineCallbacks
    def write_line(self, x):
        ans = yield self.server.write_line(x)
        returnValue(ans)
    
    @inlineCallbacks
    def write_lines(self, x):
        ans = yield self.server.write_lines(x)
        returnValue(ans)
    
    @inlineCallbacks
    def read(self, x=0):
        ans = yield self.server.read(x)
        returnValue(ans)
    
    @inlineCallbacks
    def read_line(self):
        ans = yield self.server.read_line()
        returnValue(ans)

    @inlineCallbacks
    def read_lines(self):
        ans = yield self.server.read_lines()
        returnValue(ans)

    @inlineCallbacks
    def close(self):
        yield self.server.close()
    
    @inlineCallbacks
    def flushinput(self):
        yield self.server.flushinput()
    
    @inlineCallbacks
    def flushoutput(self):
        yield self.server.flushoutput()
