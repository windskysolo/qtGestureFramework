
from PyQt5.QtCore import QEvent


class GestureManager(object):
  '''
  Know when a gesture is active.
  
  Glorified state.
  
  Especially fixes a quirk of Qt on OSX: determine when a scrolling gesture starts on OSX.
  '''
  
  def __init__(self):
    self._isGestureActive = False
  
  def isGestureActive(self):
    '''
    Is a physical gesture started, including a pseudo 'scroll' gesture on OSX.
    '''
    return self._isGestureActive
  
  
  def monitorEventForGesture(self, event):
    '''
    Call this on every event.
    
    On OSX, a physical 2-finger pinch gesture also generates QWheelEvent (the scrolling component of the physical gesture)
    but often before a QGestureEvent having a QPinchGesture in the started state.
    But a TouchBegin event reliably indicates that a pinch gesture was started (with two fingers down.)
    
    This doesn't monitor QGestureEvent.
    Your app should be handling those, and calling setGestureActive().
    
    This may be fragile.
    '''
    # class is QTouchEvent, type is QEvent.TouchBegin
    if event.type() == QEvent.TouchBegin:
      print("setGestureActive")
      self.setGestureActive()
    
    
  def setGestureActive(self):
    '''
    Call this when your app receives a QGestureEvent having a gesture in the started state.
    '''
    self._isGestureActive = True
    
    
  def setGestureCanceledOrFinished(self):
    '''
    Call this when your app receives a QGestureEvent having a gesture in the finished or canceled state.
    '''
    self._isGestureActive = False
    
    
gestureMgr = GestureManager()