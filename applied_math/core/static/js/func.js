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

window.addEventListener('DOMContentLoaded', () => {
    togglePasswordVisibility();
    toggleVisuallyImpairedMode();

    // nav form
    const navForm = document.querySelector('.nav__dropdown-form');
    const btnsSubmit = navForm.querySelectorAll('.nav__dropdown-submit');
    const inputLang = navForm.querySelector('[name="language"]');

    btnsSubmit.forEach(item => {
        item.addEventListener('click', (e) => {
            navForm.submit();
        });
    });
});