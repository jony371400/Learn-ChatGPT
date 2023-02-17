import React, { useState } from 'react';

function DeletionForm() {
  const [username, setUsername] = useState('');
  const [message, setMessage] = useState('');

  const handleDeletion = () => {
    fetch(`http://127.0.0.1:5000/users/${username}`, {
      method: 'DELETE',
      headers: {
        // 'Authorization': `Basic ${btoa(`${username}:${password}`)}`
        'Authorization': `Basic ${btoa(`${username}`)}`
      }
    })
      .then(response => {
        if (response.ok) {
          setMessage('Deletion successful');
        } else {
          setMessage('Deletion failed');
        }
      });
  };

  return (
    <div>
      <h2>Delete account</h2>
      <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} />
      <button onClick={handleDeletion}>Delete</button>
      <p>{message}</p>
    </div>
  );
}

export default DeletionForm;
