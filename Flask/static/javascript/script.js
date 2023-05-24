function validated()
{
    document.getElementById("form").classList.add("was-validated");
    age = document.getElementById("age");
    if(age.validity.rangeOverflow || age.validity.rangeUnderflow)
    {
        age.setCustomValidity("Age must be in the range 20-60.");
        document.getElementById("age-error-message").innerHTML="Age must be in the range 20-60.";
    }
    else
    {
        age.setCustomValidity("");
    }

    ntrainings = document.getElementById("no_of_trainings");
    if(ntrainings.validity.rangeOverflow || ntrainings.validity.rangeUnderflow)
    {
        ntrainings.setCustomValidity("Value must be in the range 1-10.");
        document.getElementById("training-error-message").innerHTML="Value must be in the range 1-10.";
    }
    else
    {
        ntrainings.setCustomValidity("");
    }

    service_length = document.getElementById("length_of_service");
    if(service_length.validity.rangeOverflow || service_length.validity.rangeUnderflow)
    {
        service_length.setCustomValidity("Value must be in the range 1-37.");
        document.getElementById("length-error-message").innerHTML="Value must be in the range 1-37.";
    }
    else
    {
        service_length.setCustomValidity("");
    }

    prev_rating = document.getElementById("previous_year_rating");
    if(prev_rating.validity.rangeOverflow || prev_rating.validity.rangeUnderflow)
    {
        prev_rating.setCustomValidity("Value must be in the range 1-5.");
        document.getElementById("previous-rating-error-message").innerHTML="Value must be in the range 1-5.";
    }
    else
    {
        prev_rating.setCustomValidity("");
    }

    avg_training_score = document.getElementById("avg_training_score");
    if(avg_training_score.validity.rangeOverflow || avg_training_score.validity.rangeUnderflow)
    {
        avg_training_score.setCustomValidity("Value must be in the range 0-100.");
        document.getElementById("score-error-message").innerHTML="Value must be in the range 0-100.";
    }
    else
    {
        avg_training_score.setCustomValidity("");
    }
}

function checkValid(id)
{
    element = document.getElementById(id);
    if(!element.validity.rangeOverflow && !element.validity.rangeUnderflow)
    {
        element.setCustomValidity("");
    }
}