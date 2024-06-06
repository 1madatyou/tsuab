function togglePasswordVisibility() {
    const toggleButtons = document.querySelectorAll('.toggle-eye')


    for (var i = 0; i < toggleButtons.length; i++) {
        toggleButtons[i].addEventListener("click", function() {
            this.classList.toggle('toggle-eye--active')
            const input = this.previousElementSibling
            if (input.getAttribute('type') === 'password') {
                input.setAttribute('type', 'text')
            } else {
                input.setAttribute('type', 'password')
            }
        });
    }
}

function toggleVisuallyImpairedMode() {
    const toggleButtons = document.querySelectorAll('.special-button')
    const specialButton = document.querySelector('#specialButton')

    for (var i = 0; i < toggleButtons.length; i++) {
        toggleButtons[i].addEventListener("click", function() {
            specialButton.click()
        });
    }
}

function toggleCommentRepliesDisplaying(e) {
    const currentComment = e.target.parentElement.parentElement
    const currentCommentReplyList = currentComment.querySelector('.comment__replies')

    currentCommentReplyList.classList.toggle('active')
}

function toggleCommentRepliesFormDisplaying(e) {
    const currentComment = e.target.parentElement.parentElement
    const currentCommentReplyForm = currentComment.querySelector('.comment__reply-form')

    currentCommentReplyForm.classList.toggle('active')
}



window.addEventListener('DOMContentLoaded', () => {
    togglePasswordVisibility();
    toggleVisuallyImpairedMode();

    // nav form
    const navForm = document.querySelector('.nav__dropdown-form');
    const btnsSubmit = navForm.querySelectorAll('.nav__dropdown-submit');

    const replyShowButtons = document.querySelectorAll('.comment__show-replies-button')
    const replyButtons = document.querySelectorAll('.comment__reply-button')

    btnsSubmit.forEach(item => {
        item.addEventListener('click', (e) => {
            navForm.submit();
        });
    });

    replyShowButtons.forEach(item => {
        item.addEventListener('click', toggleCommentRepliesDisplaying);
    });

    replyButtons.forEach(item => {
        item.addEventListener('click', toggleCommentRepliesFormDisplaying);
    });



});