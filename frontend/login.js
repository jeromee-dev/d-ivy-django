const BASE_URL = 'http://127.0.0.1:8000';

const form = document.getElementById('login-form');

form.addEventListener('submit', e => {
  e.preventDefault();
  const formData = {
    username: form.username.value,
    password: form.password.value
  };

  fetch(`${BASE_URL}/api/users/token/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(formData)
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    if (data.access) {
      localStorage.setItem('token', data.access);
      window.location = 'http://127.0.0.1:5500/projects-list.html'
    } else {
      alert('The information you entered was incorrect');
    }
  })
});