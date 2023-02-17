import React, { useState } from 'react';

function RegistrationForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleRegistration = () => {
    fetch('http://127.0.0.1:5000/register', {
      method: 'POST',
      headers: {
        'Authorization': `Basic ${btoa(`${username}:${password}`)}`
      }
    })
      .then(response => {
        if (response.ok) {
          setMessage('Registration successful');
        } else {
          setMessage('Registration failed');
        }
      });
  };

  return (
    <div>
      <h2>Register</h2>
      <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
      <button onClick={handleRegistration}>Register</button>
      <p>{message}</p>
    </div>
  );
}

export default RegistrationForm;