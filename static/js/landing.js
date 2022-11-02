document.addEventListener('DOMContentLoaded', () => {
  const registerButton = document.querySelector('#register-btn');
  const modal = document.querySelector('#modal');

  registerButton?.addEventListener('click', async () => {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
    document.body.classList.add('overflow-hidden');

    modal.classList.remove('hidden');
    modal.classList.add('flex');

    const response = await fetch('/auth/registration');
    const data = await response.text();

    modal.innerHTML = data;

    const alert = document.querySelector('#alert');
    const cancelButton = document.querySelector('#cancel-registration');
    const registrationForm = document.querySelector('#registration-form');

    registrationForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const formData = {
        username: document.querySelector('#id_username').value,
        phone: document.querySelector('#id_phone').value,
        address: document.querySelector('#id_address').value,
        email: document.querySelector('#id_email').value,
        password1: document.querySelector('#id_password1').value,
        password2: document.querySelector('#id_password2').value,
      };

      const response = await fetch('/auth/registration', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
          'X-CSRFToken': getCSRFToken(),
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (data.success) {
        alert.classList.remove('hidden');
        alert.classList.add('flex');
        alert.classList.add('bg-green-600');
        alert.innerHTML += data.message;
      } else {
        alert.classList.remove('hidden');
        alert.classList.add('flex');
        alert.classList.add('bg-red-600');
        alert.innerHTML += data.message;
      }
    });

    cancelButton.addEventListener('click', () => {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
      document.body.classList.remove('overflow-hidden');
    });
  });
});
