require [
  'lib/module',
  'lib/Template',
  'lib/SocketIO',
  'app/build_queue'
], ->
  @module "cc", -> cc.version = "0.1"
