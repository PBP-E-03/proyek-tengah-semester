document.addEventListener('DOMContentLoaded', () => {
  const loginButton = document.querySelector('#login-btn');
  const modal = document.querySelector('#modal');
  const dropdownButton = document.querySelector('#dropdown-btn');
  const dropdown = document.querySelector('#dropdown');
  let isDroppedDown = false;

  dropdownButton?.addEventListener('click', () => {
    if (!isDroppedDown) {
      dropdown.classList.remove('hidden');
      dropdown.classList.add('flex');
      isDroppedDown = !isDroppedDown;

      const logoutButton = document.querySelector('#logout-btn');
      logoutButton.addEventListener('click', async () => {
        await fetch('/auth/logout');
        location.reload();
      });
    } else {
      dropdown.classList.add('hidden');
      dropdown.classList.remove('flex');
      isDroppedDown = !isDroppedDown;
    }
  });

  loginButton?.addEventListener('click', async () => {
    document.body.classList.add('overflow-hidden')
    modal.classList.remove('hidden');
    modal.classList.add('flex');

    const response = await fetch('/auth/login');
    const data = await response.text();

    modal.innerHTML = data;

    const alert = document.querySelector('#alert');
    const cancelButton = document.querySelector('#cancel-login');
    const loginForm = document.querySelector('#login-form');
    const registrationAnchor = document.querySelector('#registration-anchor');

    registrationAnchor.addEventListener('click', async () => {
      const response = await fetch('/auth/registration');
      const data = await response.text();

      modal.innerHTML = data;

      const cancelButton = document.querySelector('#cancel-registration');
      const registrationForm = document.querySelector('#registration-form');
      const alert = document.querySelector('#alert');

      cancelButton.addEventListener('click', () => {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
        document.body.classList.remove('overflow-hidden')
      });

      registrationForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = {
          name: document.querySelector('#id_name').value,
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
    });

    cancelButton.addEventListener('click', () => {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
      document.body.classList.remove('overflow-hidden')
    });

    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const formData = {
        email: document.querySelector('#id_email').value,
        password: document.querySelector('#id_password').value,
        remember_me: document.querySelector('#id_remember_me').checked,
      };

      const response = await fetch('/auth/login', {
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
        location.reload();
      } else {
        alert.classList.remove('hidden');
        alert.classList.add('flex');
        alert.classList.add('bg-red-600');
        alert.innerHTML = data.message;
      }
    });
  });
});

const getCSRFToken = () => {
  const name = 'csrftoken';
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
};
