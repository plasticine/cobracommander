@module "cc", ->
  class @BuildQueue extends cc.lib.Websocket
    constructor: (url) ->
      @builderStatus = $('#builder-status')
      @buildQueue = $('#build-queue')
      super(url)
      @initListeners()
      @connect()

    initListeners: =>
      $('body')
        .bind('build_queue_connecting', =>
          @builderStatus.removeAttr('class').addClass('connecting')
          @setStatus('Connecting')
        )
        .bind('build_queue_connected', =>
          @builderStatus.removeAttr('class').addClass('connected')
        )
        .bind('build_queue_disconnected', =>
          @builderStatus.removeAttr('class').addClass('disconnected')
        )

    onconnecting: =>
      $('body').trigger('build_queue_connecting')

    onopen: =>
      $('body').trigger('build_queue_connected')

    onmessage: (event) =>
      @parseMessage(JSON.parse(event.data))

    onclose: (event) =>
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
