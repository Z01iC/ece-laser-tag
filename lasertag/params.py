### Trigger and firing ###
#trigger
p_trigger = 19
trigger_reset_time = 0.25
trigger_check_time = 0.015
#IR emitter LED + laser
p_emitter = 23
emitter_freq = 36000
emitter_duration = 0.25
emitter_duty_cycle = 50


### Hit detection and lives ###
#IR receivers
p_detection = 24
#hit display LEDs and piezo
p_hit = 26
hit_immunity_time = 1
hit_feedback_duration = 0.75
hit_check_time = 0.005
#life display LEDs
p_life = (16, 20, 21)
max_lives = 3

### Feedback buzzer ###
p_buzzer = 4

### Feedback vibrator ###
p_vibrator = 17

### Reset and game controls ###
#reset button
p_reset = 13