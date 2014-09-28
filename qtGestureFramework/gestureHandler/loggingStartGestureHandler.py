

from qtGestureFramework.gestureHandler.gestureHandler import GestureHandler


class LoggingStartGestureHandler(GestureHandler):
  '''
  Override GestureHandler to print only the start of a gesture.
  
  Ignores every gesture state change, but logs start so you know gesture is being ignored.
  '''
  
  def start(self, gesture):
    self._logGestureStateChange("Start", gesture)
    return False
  
  '''
  Other methods inherited.
  '''

  def _logGestureStateChange(self, gesture, state):
    print(state, " gesture: ", gesture.type())
    