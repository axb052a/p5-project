import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import SuccessMessage from './SuccessMessage';

function SignUp() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [passwordConfirmation, setPasswordConfirmation] = useState('');
  const [error, setError] = useState(null);
  const [successMessage, setSuccessMessage] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validation for user, email, password and password confirmation
    if (!username || !email || !password || !passwordConfirmation) {
      setError('All fields are required');
      return;
    }

    // Validation for password
    if (password !== passwordConfirmation) {
      setError('Password and confirmation do not match');

      setTimeout(() => {
        setError(null);
      }, 3000);

      return;
    }

    // Fetch request
    fetch('/api/signup', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        email,
        password,
        password_confirmation: passwordConfirmation,
      }),
    })
      .then((response) => {
        if (response.ok) {
          // User creation successful
          setSuccessMessage(`${username} has been created. Please log in.`);
          // Clear the form
          setUsername('');
          setEmail('');
          setPassword('');
          setPasswordConfirmation('');

          setTimeout(() => {
            setSuccessMessage(null);
          }, 5000);
        } else {
          response.json().then((data) => {
            setError(data.error || 'An error occurred during signup.');
          });
        }
      })
      .catch((error) => {
        console.error('Error during signup:', error);
        // Handle errors as needed
        setError('An error occurred during signup.');
      });
  };

  return (
    <Paper
      elevation={3}
      style={{
        padding: '20px',
        margin: '20px',
        backgroundImage: 'url("https://i.pinimg.com/originals/40/82/dc/4082dceb7e4ec3a35e8a617d8ea1f69a.jpg")',
        backgroundSize: 'cover',
        minHeight: '100vh',
        display: 'center',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      {successMessage && (
        <SuccessMessage
          message={successMessage}
          timeout={4000}
          redirectPath="/login"
        />
      )}
      <Typography variant="h4" gutterBottom style={{ color: 'black' }}>
        Sign Up
      </Typography>
      {error && <Typography variant="body2" style={{ color: 'red' }}>{error}</Typography>}
      <form onSubmit={handleSubmit} style={{ width: '300px', textAlign: 'center' }}>
        <TextField
          type="text"
          label="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          fullWidth
          margin="normal"
          required
        />
        <TextField
          type="text"
          label="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          fullWidth
          margin="normal"
          required
        />
        <TextField
          type="password"
          label="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          fullWidth
          margin="normal"
          required
        />
        <TextField
          type="password"
          label="Password Confirmation"
          value={passwordConfirmation}
          onChange={(e) => setPasswordConfirmation(e.target.value)}
          fullWidth
          margin="normal"
          required
        />
        <Button type="submit" variant="contained" color="primary" style={{ marginTop: '20px' }}>
          Sign Up
        </Button>
      </form>
    </Paper>
  );
}

export default SignUp;
