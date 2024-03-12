import React, { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux'; // Import useDispatch hook
import { useNavigate } from 'react-router-dom';

import { fetchUserDetails } from '../../../redux/reducers/userReducer';
import { login } from '../../../services/authAPIs';
import { AppIcon } from '../../atoms/index';
import { LoadingOverlay, LoginForm } from '../../organisms/index';
import './Login.css';

const Login = () => {

    const [isloading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const dispatch = useDispatch(); // Initialize dispatch
    const navigator = useNavigate();

    useEffect(() => {
        // if user is already logged in, redirect to dashboard
        if (localStorage.getItem('token')) {
            dispatch(fetchUserDetails())
                .then(
                    () => {
                        navigator('/dashboard');
                    }
                )
                .catch((error) => {
                });
        }
    }, [dispatch, navigator]);

    const handleSubmit = async (e, username, password) => {
        e.preventDefault();
        setLoading(true);
        try {
            await login(username, password); // Call login function
            dispatch(fetchUserDetails())
                .then(
                    () => {
                        setLoading(false);
                        navigator('/dashboard');
                    }
                )
                .catch((error) => {
                    console.error('Error fetching user data:', error.message);
                    setError('Error fetching user data');
                });

        } catch (error) {
            console.error('Error logging in:', error.message);
            setError('Invalid username or password');
        }
        finally {
            setLoading(false);
        }
    };


    return (
        <>
            {isloading && <LoadingOverlay />}
            <div className="pic min-h-screen flex justify-center items-center">
                <div className="container mx-auto w-1/3 p-24 bg-white rounded-lg shadow-lg">
                    <AppIcon />
                    {error && <p className="text-red-500">{error}</p>}
                    <LoginForm handleSubmit={handleSubmit} />

                    <div className="mb-4 text-center">
                        <p>Don't have an account? <a href="/signup" className="text-blue-500">Sign up</a></p>
                    </div>
                    <div className="text-center">
                        <p>Forgot your password? <a href="/password_reset" className="text-blue-500">Reset password</a></p>
                    </div>
                </div>
            </div>
        </>
    );
};

export default Login;
