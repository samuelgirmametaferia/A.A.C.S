global story_state

story_state = "start"

show_text = function() {
    show_message(story_text[story_state]);
}

choice_1 = function() {
    story_state = "choice_1_path";
    show_text();
}

choice_2 = function() {
    story_state = "choice_2_path";
    show_text();
}

create_event() {
    story_text = {
        "start": "The adventure begins...",
        "choice_1_path": "You encounter a fork in the road...",
        "choice_2_path": "You stumble upon a hidden cave..."
    }
    show_text();
}