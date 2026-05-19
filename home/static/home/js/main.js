const messageForm = document.querySelector('#messageForm');
const messageOutput = document.querySelector('#messageOutput');

if (messageForm && messageOutput) {
    messageForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const formData = new FormData(messageForm);
        const name = formData.get('name')?.trim() || 'friend';

        messageOutput.textContent = `Hello, ${name}! Your Django website is working.`;
        messageForm.reset();
    });
}
