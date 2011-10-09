@module "cc", ->
  class @BuildProgress extends cc.lib.SocketIOWrapper
    constructor: (build_id, url, options) ->
      @build_id = build_id
      @currentStage = null
      @buildStages = $('#build-stages')
      @stages = {
        'setup':    $('#stage-setup', @buildStages),
        'build':    $('#stage-build', @buildStages),
        'teardown': $('#stage-teardown', @buildStages)
      }
      super(url, options)
      @connect(autoReconnect=false)

    on_connect: =>
      @subscribe("build_#{@build_id}_output")

    on_message: (data) =>
      @routeMessage(JSON.parse(data))

    setupStage: (stageName) =>
      @currentStage = stageName
      if stageName != 'setup'
        @stageSteps = $('.steps', @stages[@currentStage])
      else
        @stageConsole = $('.console', @stages[@currentStage])

    routeMessage: (data) =>
      if data.stage and @currentStage != data.stage
        @setupStage(data.stage)
      if data.type
        switch data.type
          when "console"
            @handle_console(data)
          when "build_steps"
            @handle_build_steps(data)
          when "step_start"
            @handle_step_start(data)
          when "step_complete"
            @handle_step_complete(data)
          when "refspec"
            return
            @handle_refspec(data)

    handle_console: (data) =>
      @stageConsole.append("<div>#{data.data}</div>").prop({
          scrollTop: @stageConsole.prop("scrollHeight")
      })

    handle_build_steps: (data) =>
      @steps = data.data
      stepMarkup = ''
      for step in @steps.build_steps
        [sha, cmd] = step
        stepMarkup += """
          <li id="build-stage-#{sha}" class="pending">
              <strong>#{cmd}</strong>
              <div class="console"></div>
          </li>
        """
      $('.steps', @stages['build']).append(stepMarkup)

    handle_step_start: (data) =>
      @currentStep = $("#build-stage-#{data.step_hash}", @stages[@currentStage])
      @currentStep.removeClass('pending').addClass('running')
      @stageConsole = $(".console", @currentStep)

    handle_step_complete: (data) =>
      @currentStep.removeClass('running').addClass('complete').addClass(data.state)


