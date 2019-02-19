// variables
var condition = "B";
seconds_per_question = 15;


if ((condition == "A") || (condition == "B")) {
    check_info = 'their Player ID, or, the number of times they were chosen by others in Round 1.'
} else {
    check_info = 'their total score in Round 1, or, the number of times they were chosen by others in Round 1.'
}


// this function runs immediately once the page is loaded
$(document).ready(function() {

    // Hide divs that should not be initially visible
    $("#practice").hide();
    $("#round2div").hide();
    $("#round2div_check").hide();

    // Change functionality of the consent button
    $("#consent").click(function() {
        store.set("recruiter", dallinger.getUrlParameter("recruiter"));
        store.set("hit_id", dallinger.getUrlParameter("hit_id"));
        store.set("worker_id", dallinger.getUrlParameter("worker_id"));
        store.set("assignment_id", dallinger.getUrlParameter("assignment_id"));
        store.set("mode", dallinger.getUrlParameter("mode"));

        dallinger.allowExit();
        if (condition == "A") {
            window.location.href = '/instructions';
        } else { 
            window.location.href= '/instructionsB';
        }
    });

    // Add functionality to buttons controlling participantss answers
    // either option a, option b, or copy someone else.

    $("#submit-a").click(function() {
        submit_answer("#submit-a")
    });

    $("#submit-b").click(function() {
        submit_answer("#submit-b")
    });

    $("#submit-copy").click(function() {
        submit_answer("#submit-copy")
    });

    submit_answer = function(answer) {
        clearTimeout(answer_timeout);
        $("#countdown").hide();
        $("#countdown").html("");
        disable_answer_buttons();
        submit_response($(answer).text());
    }

    // Add functionality to buttons controlling participants' info choice

    $("#info-choice-a").click(function() {
        submit_choice("#info-choice-a");
    });

    $("#info-choice-b").click(function() {
        submit_choice("#info-choice-b");
    });

    submit_choice = function(choice) {
        disable_choice_buttons();   
        info_chosen = ($(choice).text());
        check_neighbors(info_chosen);
    }

    // Add functionality to the round 2 button
    // This means participants have acknowledge they are starting round 2
    // and they will be shown a quick test of this ability

    $("#round2okay").click(function() {
        $("#round2div_check").show();
        enable_R2_buttons();
        $("#round2div").hide();
    });

    // Add functionality to the practice button
    // this button starts the practice rounds

    $("#practiceButton").click(function() {
        $("#welcome_div").show();
        $("#submit_div").show();
        $("#neighbor_buttons").show();
        $("#info_choice_buttons").show();
        $("#round2div").hide();
        $("#round2div_check").hide();
        $("#practice").hide();
        display_question();
    });

    // Check AB/C are the buttons with one of the possible info choices
    // they are used to test participants attention to the instructions

    if (condition == "A" || condition == "B") {
        $("#check_AB").click(function() {
            update_ui_attention_check_passed();
        });
        $("#check_C").click(function() {
            update_ui_attention_check_failed();
        });
    } else if (condition == "C") {
        $("#check_AB").click(function(){
            update_ui_attention_check_failed();
        });
        $("#check_C").click(function() {
            update_ui_attention_check_passed();
        });
    }

    update_ui_attention_check_passed = function() {
        $("#round2div").hide();
        $("#round2div_check").hide();
        $("#welcome_div").show();
        $("#submit_div").show();
        $("#neighbor_buttons").show();
        $("#info_choice_buttons").show();
        display_question();
    }

    update_ui_attention_check_failed = function() {
        $("#wrong_check").html("WRONG ANSWER, PLEASE READ AGAIN");
        disable_R2_buttons();
        setTimeout(function() {
            $("#round2div_check").hide();
            $("#wrong_check").hide();
            $("#round2div").show();
        }, 2000);
    }

    // initially hide the buttons
    disable_answer_buttons();
    disable_choice_buttons();
    hide_pics();
});

submit_response = function(response, copy=false, info_chosen="NA") {
    dallinger.createInfo(my_node_id, {
        contents: response,
        info_type: "LottyInfo",
        property1: JSON.stringify({
            "number": number,
            "copying": copy,
            "score": (response == Rwer)*1,
            "info_chosen": info_chosen,
            "round": round,
            "human": 'true'
        })
    }).done(function (resp) {
        setTimeout(function() {
            get_transmissions();
        }, 1000);
    });
}

// Create the agent.
// This is called by the exp.html page to start the experiment.
create_agent = function() {
    dallinger.createAgent()
    .done(function (resp) {
        my_node_id = resp.node.id;
        $("#welcome").html("Welcome to our quiz, you are player " +
                           JSON.parse(resp.node.property1).name);
        get_transmissions(my_node_id);
    })
    .fail(function (rejection) {
      // A 403 is our signal that it's time to go to the questionnaire
        if (rejection.status === 403) {
            dallinger.allowExit();
            dallinger.goToPage('questionnaire');
        } else {
            dallinger.error(rejection);
        }
    });
};

// get any pending incoming transmissions
// this function is called repeatedly while we are waiting for other to catch up.
// You should only ever get one transmission at a time, so if you get > 1 the 
// experiment just hangs.
get_transmissions = function() {
    dallinger.getTransmissions(my_node_id, {
        status: "pending"
    })
    .done(function (resp) {
        transmissions = resp.transmissions;
        if (transmissions.length > 0) {
            if (transmissions.length > 1) {
                console.log("More than one transmission - unexpected!");
            } else {
                get_info(transmissions[0].info_id);
            }
        } else {
            setTimeout(function(){
                get_transmissions();
            }, 1000);
        }
    })
    .fail(function (rejection) {
        console.log(rejection);
        $('body').html(rejection.html);
    });
}

// get a specific info
// use to get the contents of an info you have been sent.
var get_info = function(info_id) {
    dallinger.getInfo(my_node_id, info_id)
    .done(function(resp) {
        process_info(resp.info);
    })
    .fail(function (rejection) {
        console.log(rejection);
        $('body').html(rejection.html);
    });
}

// Process an info.
// 
var process_info = function(info) {
    // a contents of "Bad Luck" indicates that everyone copied.
    // participants are forced to answer "Bad Luck" which is always wrong.
    if (info.contents == "Bad Luck") {
        $("#question").html("Sorry, everyone chose to Ask Someone Else, so no one can score points for this question");
        setTimeout(function() {
            submit_response("Bad Luck");
        }, 3000);

    // a contents of "Good luck" indicates you chose to copy, but not everyone else did.
    // depending on the round and condition different things will happen
    } else if (info.contents == "Good Luck") {
        if (round == 2) {
            info_choice();    
        } else if (condition == "A") {
            info_chosen = "Player ID";
            check_neighbors(info_chosen);
        } else if (condition == "B" || condition == "C") {
            info_chosen = "Total Score";
            check_neighbors(info_chosen);
        }

    // Any other contents indicates its a question from the source.
    } else {
        // get question details
        parse_question(info);

        // if its q1, show the round 1 warning
        if (number == 1) {
            display_round_warning(1);
        }

        // if its q41, show the round 2 warning
        else if (number == 41) {
            display_round_warning(2);
        }

        // if its q101, go to the questionnaire.
        else if (number ==101) {
            dallinger.allowExit();
            dallinger.goToPage('questionnaire');
        }

        // display the question
        else {
            display_question();
        }
    }
};

// Extract the relevant information from a question Info.
parse_question = function(question) {
    question_json = JSON.parse(question.contents);
    round = question_json.round;
    question_text = question_json.question;
    Wwer = question_json.Wwer;
    Rwer = question_json.Rwer;
    number = question_json.number;
    topic = question_json.topic;
    round = question_json.round;
    pic = question_json.pic;
}

// show participants the warning that they are starting the experiment proper
display_round_warning = function(round) {
    $("#welcome_div").hide();
    $("#submit_div").hide();
    $("#neighbor_buttons").hide();
    $("#info_choice_buttons").hide();
    if (round == 1) {
        $("#round2div").hide();
        $("#practice").show();
        $("#practiceInfo").html('The first three questions were practice questions. You are now starting the real quiz and your score will be counted');
    }
    if (round == 2) {
        $("#round2div").show();
        $("#r2info").html('You are now starting Round 2.<br><br>You will now be given two choices each time you choose to "Ask Someone Else".<br><br>You will be able to choose between seeing either ' + check_info);
    }
}

// display the question
display_question = function() {
    $("#question").html(question_text);
    if (round != 0) {
        $("#question_number").html("You are in the " + topic + " topic, on question " + number + "/100");
    } else {
        $("#question_number").html("You are in the " + topic + " Round, on question " + number + "/3");
    }
    if (pic == true) {
        show_pics(number);
    } else {
        hide_pics();
    }
    if (Math.random() <0.5) {
        $("#submit-a").html(Wwer);
        $("#submit-b").html(Rwer);
    } else {
        $("#submit-b").html(Wwer);
        $("#submit-a").html(Rwer);
    }
    enable_answer_buttons();
    countdown = 15;
    start_answer_timeout();
}

start_answer_timeout = function() {
    $("#countdown").show();
    answer_timeout = setTimeout(function() {
        countdown = countdown - 1;
        $("#countdown").html(countdown);
        if (countdown <= 0) {
            disable_answer_buttons();
            $("#countdown").hide();
            $("#countdown").html("");
            submit_response(Wwer);
            lotty_info.property1.human = 'false';
        } else {
            start_answer_timeout();
        }
    }, 1000);
}


var info_choice = function() {
    $("#question").html("What information do you want to see about the other players?");
    assign_choice_buttons();
    enable_choice_buttons();
};


var check_neighbors = function(info_chosen) {
    // get your neighbors
    dallinger.get(
        "/node/" + my_node_id + "/neighbors",
        {
            connection: "from",
            node_type: "LottyNode"
        }
    ).done(function (resp) {
        neighbors = resp.nodes;
        process_neighbors();
    })
}

process_neighbors = function() {
    // update question text
    if (neighbors.length == 1) {
        $("#question").html("You have " + neighbors.length + " player to copy from, please select a player to copy");
    } else {
        $("#question").html("You have " + neighbors.length + " players to copy from, please select a player to copy");
    }

    // update question1 text
    if (info_chosen == "Player ID") { 
        $("#question1").html("Below are their Player IDs");

    } else if (info_chosen == "Times chosen in Round 1") {
        $("#question1").html("Below are how many times they were chosen in Round 1 by other players");

    } else if (info_chosen == "Total Score") {
        $("#question1").html("Below is how many questions they have answered correctly themselves");
    }
    $("#question1").show();

    // update neighbor buttons
    current_button = 1;
    neighbors.forEach(function(entry) {
        update_neighbor_button(current_button, entry)        
        current_button = current_button + 1;
    });

    // show the buttons
    $("#neighbor_buttons").show();
};

update_neighbor_button = function(number, neighbor) {
    // get neighbor properties, and button details
    neighbor_properties = JSON.parse(neighbor.property1);
    button_id = "#neighbor_button_" + current_button;
    neighbor_image = "<img src='/static/images/stick.png' height='90' width='50'><br>";

    // update button and question display according to info_chosen
    if (info_chosen == "Player ID") { 
        $(button_id).html(neighbor_image + "player ID: " + neighbor_properties.name);

    } else if (info_chosen == "Times chosen in Round 1") {
        $(button_id).html(neighbor_image + "chosen " + neighbor_properties.n_copies + " times");

    } else if (info_chosen == "Total Score") {
        $(button_id).html(neighbor_image + neighbor_properties.asoc_score + " correct");
    }
    
    // add button functionality
    $(button_id).click(function() {
        console.log("im here 7");
        submit_response(neighbor.id, true, info_chosen);
        disable_neighbor_buttons();
        $("#question1").hide();
    });
    $(button_id).prop("disabled", false);
    $(button_id).show();
};

disable_R2_buttons = function() {
    $("#check_AB").addClass('disabled');
    $("#check_C").addClass('disabled');
}

enable_R2_buttons = function() {
    $("#check_AB").removeClass('disabled');
    $("#check_C").removeClass('disabled');
}

disable_answer_buttons = function() {
    $("#submit-a").addClass('disabled');
    $("#submit-b").addClass('disabled');
    $("#submit-copy").addClass('disabled');
    $("#submit-a").hide();
    $("#submit-b").hide();
    $("#submit-copy").hide();
    $("#question").html("Waiting for other players to catch up.");
}

disable_choice_buttons = function() {
    $("#info-choice-a").addClass('disabled');
    $("#info-choice-b").addClass('disabled');
    $("#info-choice-c").addClass('disabled');
    $("#info-choice-a").hide();
    $("#info-choice-b").hide();
    $("#info-choice-c").hide();
    $("#question").html("Waiting for other players to catch up.");
}

disable_neighbor_buttons = function() {
    $("#neighbor_buttons").hide();
    for (i = 1; i <= group_size-1; i++) {
        button_string = "#neighbor_button_" + i;
        $(button_string).html("");
        $(button_string).hide();
        $(button_string).prop("disabled",true);
        $(button_string).off("click");
    }
    $("#question").html("Waiting for other players to catch up.");
}

disable_all_buttons = function() {
    disable_answer_buttons();
    disable_choice_buttons();
    disable_neighbor_buttons();
}

hide_pics = function() {
    $("#pics").hide();
}

show_pics = function(number) {
    $("#pics").attr("src", "/static/images/" + number + ".png");
    $("#pics").show();
}

enable_answer_buttons = function() {
    $("#submit-a").removeClass('disabled');
    $("#submit-b").removeClass('disabled');
    $("#submit-copy").removeClass('disabled');
    $("#submit-a").show();
    $("#submit-b").show();
    $("#submit-copy").show();
}

assign_choice_buttons = function() {
    if (condition == "A" || condition == "B") {
        info_choice_a = "Player ID"
    } else {
        info_choice_a = "Total Score"
    }
    if (Math.random() < 0.5) {
        $("#info-choice-a").html(info_choice_a);
        $("#info-choice-b").html("Times chosen in Round 1")
    } else {
        $("#info-choice-a").html("Times chosen in Round 1");
        $("#info-choice-b").html(info_choice_a);
    }
}

enable_choice_buttons = function() {
    $("#countdown").hide();
    $("#info-choice-a").removeClass('disabled');
    $("#info-choice-b").removeClass('disabled');
    $("#info-choice-a").show();
    $("#info-choice-b").show();
}


// This is called by the exp.html page, it creates a set of buttons for your current
// group size.
add_neighbor_buttons = function() {
    dallinger.getExperimentProperty("group_size")
    .done(function (resp) {
        group_size = resp.group_size;
        start = '<button id="neighbor_button_';
        stop = '" type="button" class="btn btn-success"></button>';
        button_string = '';
        for (i = 1; i <= group_size-1; i++) {
            button_string = button_string.concat(start);
            button_string = button_string.concat(i);
            button_string = button_string.concat(stop);
        }
        $("#neighbor_buttons").html(button_string);
        $("#neighbor_buttons").hide();
        $(button_string).prop("disabled",true);
        for (i = 1; i <= group_size-1; i++) {
            button_string = "#neighbor_button_" + i;
            $(button_string).css({
                "margin-right": "14px"
            });
        }
        disable_neighbor_buttons();
    });
}





