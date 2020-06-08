/* Operates the modal return mail function on newsletter request */
/*Calls the function*/
function sendMail(contactForm) {
    emailjs.send("gmail", "skoot-routes-registration", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
    })
        .then(
            function (response) {
                console.log("SUCCESS", response); /*On success it will return this message*/
            },
            function (error) {
                console.log("FAILED", error); /*When the function encounters an error it will return Failed*/
            }
        );
    return false;  // To block from loading a new page
}

/* Submitting a form and hiding it/ Hides the modal on users click of sign up */

$(document).ready(function () {
    $("#onSubmit").on('submit', function (e) {
        e.preventDefault();
        $('#elegantModalForm').modal('hide');
    });
});