@module "cc", ->
  class @BuildQueue extends cc.lib.Websocket
    constructor: ->
      @builderStatus = $('#builder-status')
      @buildQueue = $('#build-queue')
      @initListeners()
      super()
      @connect()

    initListeners: =>
      $('body')
        .bind('build_queue_connecting', =>
          @builderStatus.removeAttr('class').addClass('connecting')
          @setStatus('Connecting')
        )
        .bind('build_queue_connected', =>
          @builderStatus.removeAttr('class').addClass('connected')
          @setStatus('Connected')
        )
        .bind('build_queue_disconnected', =>
          @builderStatus.removeAttr('class').addClass('disconnected')
          @setStatus('Disconnected')
        )

    on_connecting: =>
      $('body').trigger('build_queue_connecting')

    on_connect: =>
      cc.socket.subscribe('build_queue')
      $('body').trigger('build_queue_connected')

    on_message: (data) =>
      @parseMessage(JSON.parse(data))

    on_disconnect: (event) =>
      $('body').trigger('build_queue_disconnected')

    setStatus: (status) =>
      @builderStatus.html("#{status}")

    parseMessage: (data) =>
      if data.building
        @setStatus("Building")
      else
        @setStatus("Idle")
      if data.queue
        if data.queue.active
          @buildQueue.find('.empty').fadeOut(250, =>
            @buildQueue.append("""
              <li>
                <strong>#{data.queue.active.project}</strong>
                <br>
                #{data.queue.active.created_datetime}
              </li>
            """)
          )
