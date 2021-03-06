qtGestureFramework
==================

Copyright 2014 Lloyd Konneker
Licensed GPLv3

Classes supporting gestures for Python3, PyQt5

Useful for learning, experimentation, testing when you don't actually have a trackpad or touchscreen.

Includes
========

The main package gestureable.
class GestureAble, a mixin for QGraphicsView that hides the details of subscribing to gestures and handling gesture events.  
class PinchGesturable that defines an app's handlers for state changes of pinch gestures.
class GestureManager that knows when a gesture is active

A package customGesture for testing.
A custom gesture and recognizer simulating a two-finger pinch from the mouse.

A simple app/test program that uses framework

Other classes such as EventDumper


Discussion
==========
The pinch gesture is important to recognize since many laptop trackpads recognize it.
Apple Desktop HIG suggests that your app handle it: users expect it to work in most apps.


Qt quirks that testgesture.py demonstrates
==========================================

Gestures from Qt on OSX are a little strange: a pinch gesture generates wheelEvents out of order, for the scrolling component of the gesture.

On OSX, a QPinchGesture never changes its center (scrolling component comes as QWheelEvents.)

A QGraphicsView should not subscribe to gestures and receive gestures, instead its viewport should.  Otherwise, gestures are in a child of the subscriber, and you need to mess with GestureOverride event?

Ignoring gesture in started state does not prevent future gesture events (despite what the documentation says.)







