// Login.js
import React, { useState } from 'react';
import { useAuth } from '../AuthContext';

import logo from '../../assets/images/logo-short.png';
import './Login.css';

const Login = () => {
    const { login } = useAuth(); // Access login function from AuthContext
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            await login(username, password); // Call login function from AuthContext
            console.log('Login successful');
            // Redirect the user to the dashboard
            window.location.href = '/dashboard';
        } catch (error) {
            console.error('Error logging in:', error.message);
            setError('Invalid username or password');
        }
    };

    return (
        <div className="pic min-h-screen flex justify-center items-center">
            <div className="container mx-auto w-1/3 p-24 bg-white rounded-lg shadow-lg">
                <div className="text-center">
                    <a href="/profile"><img src={logo} alt="logo" className="mx-auto my-5" width="100px" /></a>
                </div>
                <form onSubmit={handleSubmit}>
                    {error && <p className="text-red-500">{error}</p>}
                    <div className="mb-4">
                        <input type="text" className="w-full px-4 py-2 rounded-lg border focus:outline-none focus:border-blue-500" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} required />
                    </div>
                    <div className="mb-4">
                        <input type="password" className="w-full px-4 py-2 rounded-lg border focus:outline-none focus:border-blue-500" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
                    </div>
                    <div className="mb-4">
                        <button type="submit" className="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 focus:outline-none">Login</button>
                    </div>
                </form>
                <div className="mb-4 text-center">
                    <p>Don't have an account? <a href="/signup" className="text-blue-500">Sign up</a></p>
                </div>
                <div className="text-center">
                    <p>Forgot your password? <a href="/password_reset" className="text-blue-500">Reset password</a></p>
                </div>
            </div>
        </div>
    );
};

export default Login;
