#Narduino Project by Ahmet YILDIRIM
#homepage:www.mclightning.com
#Code Licence: GNU General Public Licence v3

import appuifw
from socket import *
from graphics import *
import e32
w=True
onceki=''
from key_codes import *
server_socket = socket(AF_BT, SOCK_STREAM)
p = bt_rfcomm_get_available_server_channel(server_socket)
server_socket.bind(("", p))
print "bind done",p
server_socket.listen(1)
bt_advertise_service( u"Ahmet", server_socket, True, RFCOMM)
set_security(server_socket, AUTH)
print "I am listening"
(sock, peer_addr) = server_socket.accept()
print "Connection from %s"%peer_addr
class Keyboard(object):
    def __init__(self,onevent=lambda:None):
        self._keyboard_state={}
        self._downs={}
        self._onevent=onevent
    def handle_event(self,event):
        if event['type'] == appuifw.EEventKeyDown:
            code=event['scancode']
            if not self.isd(code):
                self._downs[code]=self._downs.get(code,0)+1
            self._keyboard_state[code]=1
        elif event['type'] == appuifw.EEventKeyUp:
            self._keyboard_state[event['scancode']]=0
        self._onevent()
    def isd(self,scancode):
        return self._keyboard_state.get(scancode,0)
    def isp(self,scancode):
        if self._downs.get(scancode,0):
            self._downs[scancode]-=1
            return True
        return False
keyboard=Keyboard()
appuifw.app.screen='full'
img=None
def handle_redraw(rect):
    if img:
        canvas.blit(img)
appuifw.app.body=canvas=appuifw.Canvas(
    event_callback=keyboard.handle_event,
    redraw_callback=handle_redraw)
img=Image.new(canvas.size)

running=1
def quit():
    global running
    sock.close()
    global w
    w=False
    running=0
appuifw.app.exit_key_handler=quit
a=0
b=0
c=0
t=''
while running:
    img.clear(0)
    if keyboard.isd(EScancode6):
        b=2
    if keyboard.isd(EScancode4):
        b=1
    if keyboard.isd(EScancode2):
        a=2
    if keyboard.isd(EScancode8):
        a=1
    if keyboard.isd(EScancode5):
        b=0
    if keyboard.isd(EScancode1):
        c=1
    if keyboard.isd(EScancode8)==0 and keyboard.isd(EScancode2)==0:
        a=0
    if keyboard.isd(EScancode1)==0:
        c=0
    t='<'+'a='+str(a)+'b='+str(b)+'c='+str(c)+'>'
    img.text((10,60),u'Connection='+unicode(p),fill=0xffff00)
    img.text((10,80),u'Message='+unicode(t),fill=0xffff00)
    img.text((10,32),u'a='+unicode(a),fill=0xffff00)
    img.text((30,32),u'b='+unicode(b),fill=0xffff00)
    img.text((50,32),u'c='+unicode(c),fill=0xffff00)
    img.rectangle((60,120,180,280),(255,255,255))
    if(c==1):
        img.point((70,150),0x0000ff,width=30)
        img.point((170,150),0x0000ff,width=30)
        img.point((70,250),0x0000ff,width=30)
        img.point((170,250),0x0000ff,width=30)
    if(a==2):
        img.point((120,100),(255,0,0),width=10)
    if(a==1):
        img.point((120,300),(255,0,0),width=10)
    if(b==1):
        img.point((50,200),(255,0,0),width=10)
    if(b==2):
        img.point((190,200),(255,0,0),width=10)
    if(b==0):
        img.point((120,200),(255,0,0),width=10)

    if t!=onceki:
        sock.send(t)
    handle_redraw(())
    e32.ao_yield()
    onceki=t
