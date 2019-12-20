## greet not new user
* greet
    - utter_first_guidance
    - action_check_userinfo
    - slot{"new_user" : true}
    - utter_new_user_guide
> check_new_user

## greet old user 1
* greet
    - utter_first_guidance
    - action_check_userinfo
    - slot{"new_user" : false}
    - utter_old_user_guide

## terminology call
* terminology
    - terminology_form
    - form{"name" : "terminology"}
    - form{"name" : null}
    - action_explain_terminology
    - action_deactivate_form
    

## terminology thanks
* terminology
    - terminology_form
    - form{"name" : "terminology"}
    - form{"name" : null}
    - action_explain_terminology
    - action_deactivate_form
* thanks
    - utter_thanks

## new user deny
> check_new_user
* say_no
    - utter_youneedaccount


## start daily routine
* say_yes OR ready OR start
    - utter_great
    - action_load_user_routine
> check_routine_suggestion

## accept routine
> check_routine_suggestion
* say_yes OR good OR start
    - utter_tellme1
    - utter_tellme2
> check_routine_started

## decline routine simple
> check_routine_suggestion
* say_no
    - utter_notimplemented
    - action_restart


## inquire routine1
> check_routine_suggestion
* terminology
    - terminology_form
    - form{"name" : "terminology"}
    - form{"name" : null}
    - action_explain_terminology
    - action_deactivate_form
> check_routine_suggested

## inquire routine2
> check_routine_suggestion
* hard+terminology
    - terminology_form
    - form{"name" : "terminology"}
    - form{"name" : null}
    - action_explain_terminology
    - action_deactivate_form
> check_routine_suggested

## inquire routine3
> check_routine_suggestion
* hard
    - utter_which
* choose{"which": "terminology"}
    - slot{"which": "terminology"}
    - terminology_form
    - form{"name" : "terminology"}
    - form{"name" : null}
    - action_explain_terminology
    - action_deactivate_form
> check_routine_suggested

## change routine1
> check_routine_suggestion
* change
    - change_form
    - form{"name" : "change_form"}
    - form{"name" : null }
    - action_change_routine
    - action_deactivate_form
> check_routine_suggested

## change routine2
> check_routine_suggestion
* hard+change
    - change_form
    - form{"name" : "change_form"}
    - form{"name" : null }
    - action_change_routine
    - action_deactivate_form
> check_routine_suggested

## change routine3
> check_routine_suggestion
* hard
    - utter_which
* choose{"which": "exercise"}
    - slot{"which": "exercise"}
    - change_form
    - form{"name" : "change_form"}
    - form{"name" : null }
    - action_change_routine
    - action_deactivate_form
> check_routine_suggested

## inquired routine
> check_routine_suggested
- action_load_user_routine
> check_routine_suggestion

## fin
> check_routine_started
* done
    - utter_final_check
* say_yes
    - action_record_daily
    - utter_seeyou
    - action_restart

## problem_routine
> check_routine_started
> check_another_problem
* problem
    - problem_form
    - form{"name" : "problem_form"}
    - form{"name" : null}
    - action_problem_search
    - action_deactivate_form
> check_problem_suggested

## another problem
> check_problem_suggested
- utter_anything_else
> check_another_problem

## problem free
> check_another_problem
* say_no
- action_record_daily
- utter_seeyou
- action_restart


## exercise recommendation
* inquire_exercise_recommendation
    - action_exercise_recommendation
    
    
## exercise recommendation thanks
* inquire_exercise_recommendation
    - action_exercise_recommendation
* thanks
    - utter_thanks

## routine recommendation accept
* inquire_routine_recommendation
    - action_routine_recommendation
* say_yes OR good 
    - action_routine_register
    - utter_routine_registration_complete
    - action_restart







## new user registration1
> check_new_user
* say_yes OR make_account
    - utter_registration_start
    - utter_prev_exp
* choose{"previous_exp": "high"}
    - slot{"previous_exp": "high"}
    - utter_objective
* choose
    - utter_property1
    - utter_property2
* choose
    - action_registration
    - utter_registration_complete
    - action_restart

## new user registration2
> check_new_user
* say_yes OR make_account
    - utter_registration_start
    - utter_prev_exp
* choose{"previous_exp": "middle"}
    - slot{"previous_exp": "middle"}
    - utter_objective
* choose
    - utter_property1
    - utter_property2
* choose
    - action_registration
    - utter_registration_complete
    - action_restart

## new user registration3
> check_new_user
* say_yes OR make_account
    - utter_registration_start
    - utter_prev_exp
* choose{"previous_exp": "low"}
    - slot{"previous_exp": "low"}
    - utter_objective
* choose
    - utter_property1
    - utter_property2
* choose
    - action_registration
    - utter_registration_complete
    - action_restart


## change1
* change
    - change_form
    - form{"name" : "change_form"}
    - form{"name" : null }
    - action_change_routine
    - action_deactivate_form
* thanks
    - utter_thanks
    

## change2
* change
    - change_form
    - form{"name" : "change_form"}
    - form{"name" : null }
    - action_change_routine
    - action_deactivate_form
    
## routine check
* check_routine
    - action_check_routine
    - action_restart

## withdraw userinfo
* delete_user
    - action_delete_user
    - action_restart
    
## interactive_story_1
* greet
    - utter_first_guidance
    - action_check_userinfo
    - slot{"new_user": false}
    - utter_old_user_guide
* start
    - utter_great
    - action_load_user_routine
* change
    - change_form
    - form{"name": "change_form"}
    - form{"name": null}
    - action_change_routine
    - action_deactivate_form
    - action_load_user_routine
> check_routine_suggestion
