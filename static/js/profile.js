document.addEventListener('DOMContentLoaded', () => {
  const profileForm = document.querySelector('#profile-form');
  const passwordForm = document.querySelector('#password-form');

  profileForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = {
      username: document.querySelector('#id_profile_username').value,
      email: document.querySelector('#id_profile_email').value,
      phone: document.querySelector('#id_profile_phone').value,
      address: document.querySelector('#id_profile_address').value,
    };

    await fetch('/profile/update', {
      method: 'PUT',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken(),
      },
      body: JSON.stringify(formData),
    });
  });

  passwordForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = {
      new_password: document.querySelector('#id_profile_new_password').value,
      current_password: document.querySelector('#id_profile_current_password')
        .value,
      password_confirmation: document.querySelector(
        '#id_profile_password_confirmation'
      ).value,
    };

    await fetch('/profile/update-password', {
      method: 'PUT',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken(),
      },
      body: JSON.stringify(formData),
    });
  });
});
