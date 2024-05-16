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

togglePasswordVisibility()
toggleVisuallyImpairedMode()