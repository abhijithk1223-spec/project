const themeButton = document.querySelector('#themeButton');
const messageForm = document.querySelector('#messageForm');
const messageOutput = document.querySelector('#messageOutput');

themeButton.addEventListener('click', () => {
    document.body.classList.toggle('cool-theme');
});

messageForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const formData = new FormData(messageForm);
    const name = formData.get('name')?.trim() || 'friend';

    messageOutput.textContent = `Hello, ${name}! Your Django website is working.`;
    messageForm.reset();
});
